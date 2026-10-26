# De la vaca al plato, sin perder el hilo · Reto 04 · Nivel 1

Registro de custodia de la cadena cárnica en blockchain para el lote de faenamiento **LF-2026-0188**
(Hackathon Blockchain · caso ficticio San Ramón de Altamira). Cada traspaso —arete → canal → pieza →
caja → despacho → cliente— queda anclado con su actor, y el contrato **rechaza lo físicamente
imposible**: no puede salir más carne de la que entró.

> Todos los datos son sintéticos (predios, animales, personas y clientes no existen).

## Contrato desplegado

| | |
|---|---|
| Red | Ethereum **Sepolia** (chainId 11155111) |
| Dirección | [`0xE78e4382984014D8b15B001ff9054aE9790a79ce`](https://sepolia.etherscan.io/address/0xE78e4382984014D8b15B001ff9054aE9790a79ce) |
| Compilador | solc 0.8.34, optimizador activado (200 runs) |
| Estado | Lote cargado: 60 animales · 57 canales (55 despostadas) · 364 cajas · 12 despachos · 264 ventas |

## Los cinco criterios del Nivel 1

| # | Criterio | Cómo se cumple |
|---|---|---|
| 1 | **Hacia atrás**: caja `CJ-0188-0294` → animal | `trazarCaja(294)` devuelve en una llamada la caja, el despacho, las canales 10, 11 y 12 con su dictamen, sello y curva de frío, los animales (arete, predio, dictamen ante-mortem) y el operario de cada pieza |
| 2 | **Hacia adelante**: canal `CN-0188-012` → cajas y clientes en < 1 s | `trazarCanal(12)` devuelve en una llamada las 14 cajas directas y, aparte, las 55 de carne molida (mezcla de lote), con cliente y minorista |
| 3 | **Balance de masa**: rechazar las 6 cajas de lomo fino sin piezas | El contrato revierte con `CAJA SIN PIEZAS`; juntas sumarían 278 kg contra un tope físico del lote de 205 kg (`topeCorte(1)`) |
| 4 | **Cadena de frío** recalculada desde la telemetría | Por despacho se ancla la huella (hash) de las lecturas y su resumen; la app recalcula desde las lecturas y marca en rojo `DSP-0188-006` (135 min sin lectura, aunque declara cumplir) |
| 5 | **Privacidad** | La cadena solo guarda números, códigos seudónimos y hashes. La app audita la historia de las 364 cajas buscando 98 nombres y direcciones: 0 encontrados. El consumidor verifica su compra con el código de la etiqueta (`verificarCompra(keccak256("QR-0294-1639"))`) |

## Cómo maneja la división y la mezcla

- Una canal produce 15 piezas, una por corte: se registran juntas en el **desposte** de la canal, con su
  balance de masa (cortes + hueso + grasa + mermas = peso frío, ±2 %).
- Una caja guarda su corte y una **máscara de bits** de las canales cuyas piezas contiene (muchos a muchos).
- El contrato lleva, por corte, qué piezas ya se empacaron y cuántos kilos. Una caja se rechaza si:
  no tiene piezas (`CAJA SIN PIEZAS`), usa una pieza inexistente (`PIEZA NO EXISTE`) o ya empacada
  (`PIEZA YA EMPACADA`), pesa más que sus piezas (`PESO EXCEDE PIEZAS`) o supera el rendimiento de
  referencia del lote (`EXCEDE RENDIMIENTO DEL LOTE`).
- La carne molida (CT-15) es **mezcla autorizada de lote**: la consulta hacia adelante la devuelve
  completa para cualquier canal que aportó a la mezcla, porque no puede separarse por animal.
- Una caja solo puede constar en un despacho (`CAJA YA DESPACHADA`): así se detectó la `CJ-0188-0321`
  repetida en DSP-001 y DSP-002.

## Estructura

```
contracts/CadenaCarnica.sol   contrato (Solidity ^0.8.20)
app/index.html                App Admin: conexión, carga del lote y los 5 criterios
app/lote_nivel1.json          datos del lote listos para el contrato (generado)
scripts/preparar_lote.py      genera lote_nivel1.json desde los CSV del reto
tests/probar_contrato.py      prueba de punta a punta del contrato con el lote real
docs/                         láminas de arquitectura y honestidad, y guion de la demo
Reto 04 - Camal/              manual, brief y dataset del reto
```

## Cómo correrlo

**Requisitos:** navegador con MetaMask en Sepolia, VS Code con la extensión Live Server y Python 3.

1. **Datos** (ya generados; solo si cambian los CSV):
   ```
   python scripts/preparar_lote.py
   ```
2. **Contrato** (ya desplegado; para uno nuevo): en [Remix](https://remix.ethereum.org) pegar
   `contracts/CadenaCarnica.sol` → *Solidity Compiler* → *Advanced Configurations* → **Enable optimization**
   (200) → compilar → *Deploy* con *Browser Extension / Sepolia – MetaMask*. Sin optimizador el contrato
   pesa 35 KB y supera el límite de 24 KB. Pegar la dirección en `contratoDireccion` dentro de `app/index.html`.
3. **App**: en VS Code, clic derecho sobre `app/index.html` → *Open with Live Server*. Tiene que servirse
   desde `app/`, junto a `lote_nivel1.json`.
4. **Cargar el lote** (solo en un contrato nuevo): *Conectar MetaMask* → *Cargar lote* (unas 37
   transacciones, unos 58 M de gas). La carga es reanudable.
5. **Demo**: recorrer las secciones 1 a 5 del menú. Las consultas funcionan sin wallet (RPC público).

**Prueba automática del contrato:**
```
pip install -r tests/requirements.txt
python tests/probar_contrato.py
```
Despliega el contrato en una EVM local, carga el lote completo con la misma lógica que la app y
comprueba los cinco criterios.

## Alcance

Este repositorio implementa **solo el Nivel 1** del brief. Quedan fuera la página del consumidor sin
wallet (Nivel 2) y los sensores firmados, la habilitación en origen y el retiro automático (Nivel 3).
Supuestos, limitaciones y costos: ver [docs/laminas.md](docs/laminas.md).
