"""Prepara app/lote_nivel1.json a partir de los CSV del dataset del Reto 04.

Convierte cada registro a las unidades que espera el contrato CadenaCarnica:
gramos enteros, fechas Unix, temperaturas en décimas de grado y códigos de
actor numéricos. Lo que contiene nombres o direcciones queda en la sección
"fueraDeCadena": la app lo usa para mostrar y para la auditoría de privacidad,
pero nunca se envía al contrato.

Uso:  python scripts/preparar_lote.py
"""

import csv
import json
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / "Reto 04 - Camal" / "datos"
SALIDA = RAIZ / "app" / "lote_nivel1.json"
SALIDA_PUBLICA = RAIZ / "consulta" / "datos_publicos.json"

DICTAMEN_AM = {"APTO": 1, "RETENIDO": 2, "DECOMISO": 3}
DICTAMEN_PM = {"APROBADA": 1, "DECOMISO PARCIAL": 2, "DECOMISO TOTAL": 3}

# Estaciones sin código de persona en el dataset
BASCULA, LINEA, SALA = 401, 402, 403


def leer(nombre):
    with open(DATOS / nombre, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def unix(texto):
    """'2026-08-11T06:00:00-05:00' o '2026-08-11' → segundos Unix."""
    if "T" not in texto:
        texto += "T00:00:00-05:00"
    return int(datetime.fromisoformat(texto).timestamp())


def gramos(kg):
    return round(float(kg) * 1000)


def decimas(grados):
    return round(float(grados) * 10)


def actor(codigo):
    """MV-03 → 103 · OP-21 → 221 · DS-01 → 301 · CL-M01 → 1001 · CL-R05 → 2005."""
    prefijo, numero = codigo.rsplit("-", 1)
    base = {"MV": 100, "OP": 200, "DS": 300, "CL-M": 1000, "CL-R": 2000}
    if prefijo == "CL":
        prefijo, numero = "CL-" + numero[0], numero[1:]
    return base[prefijo] + int(numero)


def numero(codigo):
    """CN-0188-012 → 12 · CJ-0188-0294 → 294 · DSP-0188-006 → 6 · PR-063 → 63."""
    return int(codigo.rsplit("-", 1)[1])


def main():
    carta = leer("carta_cortes.csv")
    corte_de = {c["corte_id"]: numero(c["corte_id"]) for c in carta}

    # ---------------- 1. Animales e inspección ante-mortem
    ante = {a["arete_sigan"]: a for a in leer("inspeccion_ante_mortem.csv")}
    animales = []
    for a in leer("animales.csv"):
        am = ante[a["arete_sigan"]]
        documentos = "|".join([
            a["guia_movilizacion"], a["certificado_sanitario"],
            "aftosa:" + a["fecha_vacunacion_aftosa"],
            "vigencia_aftosa:" + a["vigencia_aftosa_hasta"],
            "brucelosis:" + a["fecha_vacunacion_brucelosis"],
        ])
        animales.append({
            "codigo": a["arete_sigan"],
            "arete": int(a["arete_sigan"]),
            "predio": numero(a["predio_id"]),
            "fechaIngreso": unix(a["fecha_hora_ingreso"]),
            "pesoVivoG": gramos(a["peso_vivo_kg"]),
            "dictamenAM": DICTAMEN_AM[am["dictamen"]],
            "mviAM": actor(am["mvi"]),
            "documentos": documentos,
            "actor": BASCULA,
        })

    # ---------------- 2. Canales y curva de descenso térmico
    curvas = {}
    for t in leer("temperatura_canales.csv"):
        curvas.setdefault(t["canal_id"], []).append(
            (int(t["horas_post_sacrificio"]), decimas(t["temperatura_interna_c"])))

    canales = []
    for c in leer("canales.csv"):
        sello = c["codigo_sello"].split("-")
        canales.append({
            "codigo": c["canal_id"],
            "numero": numero(c["canal_id"]),
            "arete": int(c["arete_sigan"]),
            "fechaSacrificio": unix(c["fecha_hora_sacrificio"]),
            "pesoCalienteG": gramos(c["peso_canal_caliente_kg"]),
            "dictamenPM": DICTAMEN_PM[c["dictamen_post_mortem"]],
            "mviPM": actor(c["mvi_sello"]),
            "codigoSello": int(sello[1]) * 1000 + int(sello[2]),
            "fechaSello": unix(c["fecha_hora_sello"]),
            "curvaDecimas": [v for _, v in sorted(curvas[c["canal_id"]])],
            "actor": LINEA,
        })

    # ---------------- 3. Desposte: 15 piezas por canal + balance de masa
    piezas = {}
    canal_de_pieza = {}
    for p in leer("cortes.csv"):
        piezas.setdefault(p["canal_id"], []).append(p)
        canal_de_pieza[p["corte_pieza_id"]] = numero(p["canal_id"])

    despostes = []
    for b in leer("balance_masa.csv"):
        lista = sorted(piezas[b["canal_id"]], key=lambda p: corte_de[p["corte_id"]])
        despostes.append({
            "codigo": b["canal_id"],
            "numero": numero(b["canal_id"]),
            "pesoFrioG": gramos(b["peso_canal_frio_kg"]),
            "pesosG": [gramos(p["peso_kg"]) for p in lista],
            "operarios": [actor(p["operario"]) for p in lista],
            "huesoG": gramos(b["hueso_kg"]),
            "grasaG": gramos(b["grasa_kg"]),
            "mermasG": gramos(b["recortes_mermas_kg"]),
            "fechaDesposte": min(unix(p["fecha_hora_corte"]) for p in lista),
            "actor": SALA,
        })

    # ---------------- 4. Cajas (las canales de origen salen de las piezas)
    cajas = []
    for c in leer("cajas.csv"):
        ids = [p for p in c["piezas"].split("|") if p]
        cajas.append({
            "codigo": c["caja_id"],
            "numero": numero(c["caja_id"]),
            "corte": corte_de[c["corte_id"]],
            "canales": sorted({canal_de_pieza[p] for p in ids if p in canal_de_pieza}),
            "pesoG": gramos(c["peso_kg"]),
            "fechaEmpaqueReal": unix(c["fecha_empaque_real"]),
            "operario": actor(c["operario_empaque"]),
        })

    # ---------------- 5. Despachos con sus lecturas de telemetría (crudas)
    detalle = {}
    for d in leer("despacho_cajas.csv"):
        detalle.setdefault(d["despacho_id"], []).append(numero(d["caja_id"]))

    lecturas = {}
    for t in leer("telemetria_frio.csv"):
        if t["origen"] == "TRANSPORTE":
            lecturas.setdefault(t["referencia"], []).append(
                [t["sensor"], t["fecha_hora"], t["temperatura_c"], t["limite_c"]])

    despachos = []
    for d in leer("despachos.csv"):
        despachos.append({
            "codigo": d["despacho_id"],
            "numero": numero(d["despacho_id"]),
            "cliente": actor(d["cliente_id"]),
            "salida": unix(d["fecha_hora_salida"]),
            "llegada": unix(d["fecha_hora_llegada"]),
            "cumpleDeclarado": d["cumple_cadena_frio"] == "SI",
            "despachador": actor(d["despachador"]),
            "cajasDeclaradas": int(d["cajas"]),
            "cajas": detalle[d["despacho_id"]],
            "lecturas": sorted(lecturas.get(d["despacho_id"], []), key=lambda r: r[1]),
        })

    # ---------------- 6. Redistribución y 7. ventas al consumidor
    redistribuciones = [{
        "caja": numero(r["caja_id"]),
        "minorista": actor(r["hacia_cliente"]),
        "fecha": unix(r["fecha_hora"]),
    } for r in leer("redistribucion.csv")]

    ventas = [{
        "codigoConsulta": v["codigo_consulta_consumidor"],
        "caja": numero(v["caja_id"]),
        "minorista": actor(v["minorista"]),
        "fecha": unix(v["fecha_hora_venta"]),
        "unidades": int(v["unidades_fraccionadas"]),
    } for v in leer("ventas_consumidor.csv")]

    # ---------------- Nivel 2: orden de retiro sanitario y su resultado de laboratorio
    laboratorio = {a["analisis_id"]: a for a in leer("analisis_laboratorio.csv")}
    retiros = []
    for r in leer("retiro_sanitario.csv"):
        analisis = laboratorio[r["motivo"].split("análisis ")[-1].strip()]
        retiros.append({
            "codigo": r["orden_retiro_id"],
            "canal": numero(r["canal_id"]),
            "fechaNotificacion": unix(r["fecha_hora_notificacion"]),
            "fechaOrden": unix(r["fecha_hora_orden"]),
            "resultado": "|".join([analisis["analisis_id"], analisis["canal_id"], analisis["tipo"],
                                   analisis["resultado"], analisis["fecha_resultado"]]),
            "motivo": r["motivo"],
        })

    # ---------------- Datos que NUNCA van a la cadena
    fuera = {
        "personal": {actor(p["persona_id"]): {"codigo": p["persona_id"], "nombre": p["nombre"],
                                             "cargo": p["cargo"]} for p in leer("personal.csv")},
        "clientes": {actor(c["cliente_id"]): {"codigo": c["cliente_id"], "razonSocial": c["razon_social"],
                                             "tipo": c["tipo"], "direccion": c["direccion"]}
                     for c in leer("clientes.csv")},
        "predios": {numero(p["predio_id"]): {"codigo": p["predio_id"], "nombre": p["nombre"],
                                            "ubicacion": p["ubicacion"], "introductor": p["introductor"]}
                    for p in leer("predios.csv")},
        "estaciones": {BASCULA: "Báscula de ingreso", LINEA: "Línea de faenamiento",
                       SALA: "Sala de desposte"},
    }

    lote = {
        "lote": "LF-2026-0188",
        "cortes": {corte_de[c["corte_id"]]: {"codigo": c["corte_id"], "nombre": c["nombre"],
                                            "categoria": c["categoria"],
                                            "rendimientoPct": float(c["rendimiento_referencia_pct"])}
                   for c in carta},
        "animales": animales,
        "canales": canales,
        "despostes": despostes,
        "cajas": cajas,
        "despachos": despachos,
        "redistribuciones": redistribuciones,
        "ventas": ventas,
        "retiros": retiros,
        "fueraDeCadena": fuera,
    }

    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_text(json.dumps(lote, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{SALIDA}: {len(animales)} animales, {len(canales)} canales, {len(despostes)} despostes, "
          f"{len(cajas)} cajas, {len(despachos)} despachos, {len(redistribuciones)} redistribuciones, "
          f"{len(ventas)} ventas, {len(retiros)} retiros")

    # ---------------- Nivel 2: datos públicos para la página del consumidor.
    # Solo lo publicable: cortes, predios (fincas, no personas) y las lecturas
    # de frío de cada despacho, para que el consumidor recalcule su huella.
    # Sin nombres de operarios ni de clientes, ni direcciones.
    publicos = {
        "lote": "LF-2026-0188",
        "cortes": lote["cortes"],
        "predios": {n: {"codigo": p["codigo"], "nombre": p["nombre"], "ubicacion": p["ubicacion"]}
                    for n, p in fuera["predios"].items()},
        "lecturas": {d["numero"]: d["lecturas"] for d in despachos},
    }
    SALIDA_PUBLICA.parent.mkdir(exist_ok=True)
    SALIDA_PUBLICA.write_text(json.dumps(publicos, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{SALIDA_PUBLICA}: {len(publicos['predios'])} predios, {len(publicos['lecturas'])} despachos con lecturas")


if __name__ == "__main__":
    main()
