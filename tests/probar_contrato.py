"""Prueba de punta a punta de los contratos con el lote LF-2026-0188.

Despliega CadenaCarnica en una EVM local (eth-tester), carga el lote completo
por grupos con la misma lógica que la App Admin y comprueba los cinco
criterios del Nivel 1. Después despliega RetirosSanitarios, registra la orden
RS-2026-004 y comprueba lo que necesita la consulta del consumidor (Nivel 2).

Requiere:  pip install py-solc-x web3 py-evm eth-tester
Uso:       python tests/probar_contrato.py
"""

import json
import sys
import time
from datetime import datetime
from pathlib import Path

import solcx
from eth_tester.exceptions import TransactionFailed
from eth_utils import keccak
from web3 import Web3
from web3.exceptions import ContractLogicError

RAIZ = Path(__file__).resolve().parent.parent
CONTRATOS = RAIZ / "contracts"
LOTE = RAIZ / "app" / "lote_nivel1.json"

fallos = []


def comprobar(condicion, mensaje):
    print(("  OK   " if condicion else "  FALLA ") + mensaje)
    if not condicion:
        fallos.append(mensaje)


def compilar(nombre):
    solcx.install_solc("0.8.20")
    archivo = nombre + ".sol"
    salida = solcx.compile_standard({
        "language": "Solidity",
        "sources": {archivo: {"content": (CONTRATOS / archivo).read_text(encoding="utf-8")}},
        "settings": {
            "optimizer": {"enabled": True, "runs": 200},
            "outputSelection": {"*": {"*": ["abi", "evm.bytecode.object", "evm.deployedBytecode.object"]}},
        },
    }, solc_version="0.8.20")
    c = salida["contracts"][archivo][nombre]
    tamano = len(c["evm"]["deployedBytecode"]["object"]) // 2
    comprobar(tamano <= 24576, f"tamaño de {nombre} con optimizador: {tamano} bytes (límite 24576)")
    return c["abi"], c["evm"]["bytecode"]["object"]


# ---------------------------------------------------------------
# Las mismas conversiones que hace la App Admin antes de enviar
# ---------------------------------------------------------------

def mascara(canales):
    m = 0
    for n in canales:
        m |= 1 << n
    return m


def resumen_frio(despacho):
    """Recalcula la cadena de frío del trayecto desde la telemetría."""
    lecturas = despacho["lecturas"]
    tiempos = [despacho["salida"]]
    tiempos += [int(datetime.fromisoformat(r[1]).timestamp()) for r in lecturas]
    tiempos += [despacho["llegada"]]
    sin_lectura = 0
    for a, b in zip(tiempos, tiempos[1:]):
        hueco = (b - a) // 60
        if hueco > 15:
            sin_lectura += hueco - 15
    fuera = 15 * sum(1 for r in lecturas if float(r[2]) > float(r[3]))
    maxima = max((round(float(r[2]) * 10) for r in lecturas), default=0)
    texto = "\n".join("|".join(r) for r in lecturas)
    return {
        "tempMaxDecimas": maxima,
        "minutosFuera": fuera,
        "minutosSinLectura": sin_lectura,
        "lecturas": len(lecturas),
        "hashLecturas": keccak(text=texto),
    }


def tupla_animal(a):
    return (a["arete"], a["predio"], a["fechaIngreso"], a["pesoVivoG"], a["dictamenAM"], a["mviAM"],
            a["actor"], keccak(text=a["documentos"]))


def tupla_canal(c):
    return (c["numero"], c["arete"], c["fechaSacrificio"], c["pesoCalienteG"], c["dictamenPM"], c["mviPM"],
            c["codigoSello"], c["fechaSello"], c["actor"], c["curvaDecimas"])


def tupla_desposte(d):
    return (d["pesosG"], d["operarios"], d["pesoFrioG"], d["huesoG"], d["grasaG"], d["mermasG"],
            d["fechaDesposte"], d["actor"])


def tupla_caja(c):
    return (c["numero"], c["corte"], False, mascara(c["canales"]), c["pesoG"], c["fechaEmpaqueReal"],
            c["operario"], 0, 0, 0)


def tupla_despacho(d, cajas):
    r = resumen_frio(d)
    return (d["numero"], d["cliente"], d["salida"], d["llegada"], r["tempMaxDecimas"], r["minutosFuera"],
            r["minutosSinLectura"], r["lecturas"], d["cumpleDeclarado"], d["despachador"], r["hashLecturas"],
            cajas)


def tupla_venta(v):
    return (keccak(text=v["codigoConsulta"]), v["caja"], v["minorista"], v["fecha"], v["unidades"])


def motivo(funcion):
    try:
        funcion.call()
        return None
    except (ContractLogicError, TransactionFailed) as e:
        return str(e).replace("execution reverted: ", "")


def main():
    abi, bytecode = compilar("CadenaCarnica")
    w3 = Web3(Web3.EthereumTesterProvider())
    w3.eth.default_account = w3.eth.accounts[0]
    tx = w3.eth.contract(abi=abi, bytecode=bytecode).constructor().transact()
    direccion = w3.eth.wait_for_transaction_receipt(tx).contractAddress
    contrato = w3.eth.contract(address=direccion, abi=abi)
    lote = json.loads(LOTE.read_text(encoding="utf-8"))

    gas_total = 0
    transacciones = 0
    rechazos = []

    def enviar(funcion):
        nonlocal gas_total, transacciones
        recibo = w3.eth.wait_for_transaction_receipt(funcion.transact())
        gas_total += recibo.gasUsed
        transacciones += 1
        return recibo.gasUsed

    def cargar_por_grupos(nombre, items, tamano, armar, codigo):
        """Envía en grupos; si un grupo revierte, el contrato decide qué ítem rechazar."""
        for i in range(0, len(items), tamano):
            grupo = items[i:i + tamano]
            if motivo(armar(grupo)):
                validos = []
                for item in grupo:
                    razon = motivo(armar(validos + [item]))
                    if razon:
                        rechazos.append((nombre, codigo(item), razon))
                    else:
                        validos.append(item)
                grupo = validos
            if grupo:
                enviar(armar(grupo))

    print("\nCarga del lote")
    cargar_por_grupos("animal", lote["animales"], 30,
                      lambda g: contrato.functions.registrarAnimales([tupla_animal(a) for a in g]),
                      lambda a: a["codigo"])
    cargar_por_grupos("canal", lote["canales"], 20,
                      lambda g: contrato.functions.registrarCanales([tupla_canal(c) for c in g]),
                      lambda c: c["codigo"])
    cargar_por_grupos("desposte", lote["despostes"], 14,
                      lambda g: contrato.functions.registrarDespostes(
                          [d["numero"] for d in g], [tupla_desposte(d) for d in g]),
                      lambda d: d["codigo"])

    fantasmas = [c for c in lote["cajas"] if not c["canales"]]
    reales = [c for c in lote["cajas"] if c["canales"]]
    cargar_por_grupos("caja", reales + fantasmas, 40,
                      lambda g: contrato.functions.registrarCajas([tupla_caja(c) for c in g]),
                      lambda c: c["codigo"])

    for d in lote["despachos"]:
        cajas = []
        for n in d["cajas"]:
            razon = motivo(contrato.functions.registrarDespacho(tupla_despacho(d, cajas + [n])))
            if razon:
                rechazos.append(("despacho " + d["codigo"], f"CJ-0188-{n:04d}", razon))
            else:
                cajas.append(n)
        enviar(contrato.functions.registrarDespacho(tupla_despacho(d, cajas)))

    r = lote["redistribuciones"]
    for i in range(0, len(r), 75):
        g = r[i:i + 75]
        enviar(contrato.functions.registrarRedistribuciones(
            [x["caja"] for x in g], [x["minorista"] for x in g], [x["fecha"] for x in g]))
    cargar_por_grupos("venta", lote["ventas"], 66,
                      lambda g: contrato.functions.registrarVentas([tupla_venta(v) for v in g]),
                      lambda v: v["codigoConsulta"])

    print(f"  {transacciones} transacciones · gas total {gas_total:,}")
    for gwei in (1, 3, 10):
        print(f"  costo estimado a {gwei} gwei: {gas_total * gwei / 1e9:.4f} ETH")
    for nombre, codigo, razon in rechazos:
        print(f"  rechazado por el contrato · {nombre} {codigo}: {razon}")

    totales = contrato.functions.totales().call()
    comprobar(list(totales) == [60, 57, 55, 364, 12, 264],
              f"totales en cadena (animales, canales, despostadas, cajas, despachos, ventas) = {list(totales)}")

    print("\nCriterio 1 · hacia atrás desde CJ-0188-0294")
    caja, despacho, canales, animales, pesos, operarios = contrato.functions.trazarCaja(294).call()
    comprobar([c[0] for c in canales] == [10, 11, 12], f"canales de origen: {[c[0] for c in canales]}")
    comprobar(all(a[0] == c[1] for a, c in zip(animales, canales)), "cada canal llega a su arete y predio")
    comprobar(len(canales[2][9]) == 5, f"curva de frío de CN-012: {canales[2][9]}")
    comprobar(despacho[0] == 5, f"despacho DSP-0188-{despacho[0]:03d}, operarios del desposte {operarios}")

    print("\nCriterio 2 · hacia adelante desde CN-0188-012")
    inicio = time.perf_counter()
    directas, clientes, mezcla, clientes_mezcla = contrato.functions.trazarCanal(12).call()
    ms = (time.perf_counter() - inicio) * 1000
    numeros = sorted(c[0] for c in directas)
    esperadas = sorted(c["numero"] for c in lote["cajas"] if 12 in c["canales"] and c["corte"] != 15)
    comprobar(numeros == esperadas and len(numeros) == 14, f"{len(numeros)} cajas directas: {numeros}")
    comprobar(len(mezcla) == 55, f"{len(mezcla)} cajas de mezcla de lote (molida)")
    comprobar(ms < 1000, f"consulta en {ms:.0f} ms (EVM local)")
    minoristas = sorted({c[8] for c in directas if c[8]})
    print(f"        clientes directos {sorted(set(clientes))} · minoristas por redistribución {minoristas}")

    print("\nCriterio 3 · balance de masa: las 6 cajas de lomo fino sin piezas")
    for c in fantasmas:
        razon = motivo(contrato.functions.registrarCajas([tupla_caja(c)]))
        comprobar(razon == "CAJA SIN PIEZAS", f"{c['codigo']} rechazada: {razon}")
    empacado, tope = contrato.functions.topeCorte(1).call()
    extra = sum(c["pesoG"] for c in fantasmas)
    comprobar(empacado + extra > tope,
              f"lomo fino: empacado {empacado / 1000:.2f} kg + cajas fantasma {extra / 1000:.2f} kg "
              f"= {(empacado + extra) / 1000:.2f} kg > tope físico del lote {tope / 1000:.2f} kg")
    falsa = dict(fantasmas[0], canales=[12])
    razon = motivo(contrato.functions.registrarCajas([tupla_caja(falsa)]))
    comprobar(razon == "PIEZA YA EMPACADA", f"si declara la pieza de CN-012 (ya empacada): {razon}")

    print("\nCriterio 4 · cadena de frío recalculada desde la telemetría")
    rojos = []
    for d in lote["despachos"]:
        en_cadena = contrato.functions.obtenerDespacho(d["numero"]).call()
        recalculado = resumen_frio(d)
        cumple = recalculado["minutosFuera"] == 0 and recalculado["minutosSinLectura"] == 0
        comprobar(en_cadena[10] == recalculado["hashLecturas"], f"{d['codigo']} hash de lecturas coincide")
        if not cumple:
            rojos.append((d["codigo"], recalculado["minutosSinLectura"], d["cumpleDeclarado"]))
    comprobar(rojos == [("DSP-0188-006", 135, True)], f"en rojo: {rojos} (minutos sin lectura, declara cumplir)")

    print("\nCriterio 5 · privacidad y verificación del consumidor")
    sensibles = []
    for grupo in lote["fueraDeCadena"].values():
        for registro in grupo.values():
            if isinstance(registro, dict):
                sensibles += [v for k, v in registro.items() if k != "codigo" and isinstance(v, str)]
    datos_cadena = b""
    for n in contrato.functions.listarCajas().call():
        datos_cadena += w3.eth.call({"to": direccion, "data": contrato.encode_abi("trazarCaja", [n])})
    encontrados = [s for s in sensibles if s.encode("utf-8") in datos_cadena]
    comprobar(not encontrados, f"{len(sensibles)} nombres/direcciones buscados en la cadena: {len(encontrados)} encontrados")
    venta = contrato.functions.verificarCompra(keccak(text="QR-0294-1639")).call()
    comprobar(venta[1] == 294, f"el código QR-0294-1639 lleva a la caja CJ-0188-{venta[1]:04d}")

    print("\nNivel 2 · retiro sanitario RS-2026-004 en un contrato aparte")
    abi_r, bytecode_r = compilar("RetirosSanitarios")
    tx = w3.eth.contract(abi=abi_r, bytecode=bytecode_r).constructor(direccion).transact()
    retiros = w3.eth.contract(address=w3.eth.wait_for_transaction_receipt(tx).contractAddress, abi=abi_r)
    orden = lote["retiros"][0]
    argumentos = (orden["codigo"], orden["canal"], orden["fechaNotificacion"], orden["fechaOrden"],
                  keccak(text=orden["resultado"]))
    razon = motivo(retiros.functions.registrarRetiro(*argumentos))
    otra = w3.eth.accounts[1]
    try:
        retiros.functions.registrarRetiro(*argumentos).call({"from": otra})
        ajena = None
    except (ContractLogicError, TransactionFailed) as e:
        ajena = str(e).replace("execution reverted: ", "")
    comprobar(ajena == "SOLO LA AUTORIDAD SANITARIA", f"otra wallet no puede registrar retiros: {ajena}")
    comprobar(razon is None, "la autoridad registra la orden")
    enviar(retiros.functions.registrarRetiro(*argumentos))
    comprobar(motivo(retiros.functions.registrarRetiro(*argumentos)) == "CANAL YA RETIRADA",
              "la misma canal no se puede retirar dos veces")

    alcanzada, por_mezcla, retiro = retiros.functions.cajaBajoRetiro(294).call()
    comprobar(alcanzada and not por_mezcla and retiro[0] == "RS-2026-004",
              f"CJ-0188-0294 bajo retiro {retiro[0]} (directa)")
    molida = next(c["numero"] for c in lote["cajas"] if c["corte"] == 15 and 12 not in c["canales"])
    alcanzada, por_mezcla, _ = retiros.functions.cajaBajoRetiro(molida).call()
    comprobar(alcanzada and por_mezcla, f"molida CJ-0188-{molida:04d} (sin pieza de CN-012) alcanzada por mezcla")
    comprobar(not retiros.functions.cajaBajoRetiro(1).call()[0], "CJ-0188-0001 (canales 1–5) no está alcanzada")

    alcanzadas = [n for n in contrato.functions.listarCajas().call() if retiros.functions.cajaBajoRetiro(n).call()[0]]
    comprobar(len(alcanzadas) == 69, f"{len(alcanzadas)} cajas alcanzadas (14 directas + 55 de molida)")
    tardias = sorted((v["codigoConsulta"], v["caja"]) for v in lote["ventas"]
                     if v["caja"] in alcanzadas and v["fecha"] > orden["fechaOrden"])
    directas_tardias = [t for t in tardias if t[1] in (3, 15, 34, 56, 83, 108, 128, 147, 158, 189, 225, 251, 276, 294)]
    comprobar(len(directas_tardias) == 3, f"ventas de cajas directas después de la orden: {directas_tardias}")
    print(f"        ventas de molida después de la orden: {len(tardias) - len(directas_tardias)}")

    print("\nResultado:", "TODO OK" if not fallos else f"{len(fallos)} FALLAS")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
