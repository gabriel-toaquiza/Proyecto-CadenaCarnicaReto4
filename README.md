# De la vaca al plato, sin perder el hilo · Reto 04 · Niveles 1 y 2

Registro de custodia de la cadena cárnica en blockchain para el lote de faenamiento **LF-2026-0188**
(Hackathon Blockchain · caso ficticio San Ramón de Altamira). Cada traspaso —arete → canal → pieza →
caja → despacho → cliente— queda anclado con su actor, y el contrato **rechaza lo físicamente
imposible**: no puede salir más carne de la que entró. Una página pública le permite al consumidor
consultar y comprobar su compra desde el código de la etiqueta, y le advierte si el producto está bajo
retiro sanitario.

> Todos los datos son sintéticos (predios, animales, personas y clientes no existen).

## Contratos desplegados (Ethereum Sepolia, chainId 11155111)

| Contrato | Dirección | Contenido |
|---|---|---|
| `CadenaCarnica` (Nivel 1) | [`0xE78e4382984014D8b15B001ff9054aE9790a79ce`](https://sepolia.etherscan.io/address/0xE78e4382984014D8b15B001ff9054aE9790a79ce) | Lote cargado: 60 animales · 57 canales (55 despostadas) · 364 cajas · 12 despachos · 264 ventas |
| `RetirosSanitarios` (Nivel 2) | [`0x4dAFa0621745559a636333898726A85Dee48c7Ec`](https://sepolia.etherscan.io/address/0x4dAFa0621745559a636333898726A85Dee48c7Ec) | Orden RS-2026-004 registrada sobre la canal CN-0188-012 |

Compilados con solc 0.8.34 y el optimizador activado (200 runs).

**Consulta del consumidor:** https://lambent-blancmange-7e26ae.netlify.app/
- Caja bajo retiro: [`?codigo=QR-0294-1639`](https://lambent-blancmange-7e26ae.netlify.app/?codigo=QR-0294-1639) (QR en `docs/qr_QR-0294-1639.png`)
- Caja sin retiro: [`?codigo=QR-0288-5222`](https://lambent-blancmange-7e26ae.netlify.app/?codigo=QR-0288-5222) (QR en `docs/qr_QR-0288-5222.png`)

## Los cinco criterios del Nivel 1

| # | Criterio | Cómo se cumple |
|---|---|---|
| 1 | **Hacia atrás**: caja `CJ-0188-0294` → animal | `trazarCaja(294)` devuelve en una llamada la caja, el despacho, las canales 10, 11 y 12 con su dictamen, sello y curva de frío, los animales (arete, predio, dictamen ante-mortem) y el operario de cada pieza |
| 2 | **Hacia adelante**: canal `CN-0188-012` → cajas y clientes en < 1 s | `trazarCanal(12)` devuelve en una llamada las 14 cajas directas y, aparte, las 55 de carne molida (mezcla de lote), con cliente y minorista |
| 3 | **Balance de masa**: rechazar las 6 cajas de lomo fino sin piezas | El contrato revierte con `CAJA SIN PIEZAS`; juntas sumarían 278 kg contra un tope físico del lote de 205 kg (`topeCorte(1)`) |
| 4 | **Cadena de frío** recalculada desde la telemetría | Por despacho se ancla la huella (hash) de las lecturas y su resumen; la app recalcula desde las lecturas y marca en rojo `DSP-0188-006` (135 min sin lectura, aunque declara cumplir) |
| 5 | **Privacidad** | La cadena solo guarda números, códigos seudónimos y hashes. La app audita la historia de las 364 cajas buscando 98 nombres y direcciones: 0 encontrados. El consumidor verifica su compra con el código de la etiqueta (`verificarCompra(keccak256("QR-0294-1639"))`) |

## Nivel 2: la consulta del consumidor

`consulta/index.html` se abre desde el código de la etiqueta (`?codigo=QR-0294-1639`, con el lector QR
o escribiéndolo), **sin instalar nada, sin cuenta y sin wallet**. Lee directo de la blockchain con un RPC
público y responde:

- **Retiro sanitario primero:** si la caja está alcanzada por una orden de retiro, una alerta roja dice que
  no se consuma. Si la venta se registró después de la orden, lo dice: "el registro comercial dice que la
  venta se concretó, pero el producto no debía venderse". Es el criterio de aceptación del Nivel 2.
- De dónde vino (predio), cuándo se faenó, el dictamen ante y post-mortem, la **fecha real de empaque** y
  si se mantuvo el frío.
- **Comprobación propia:** la página recalcula en el teléfono la huella de las lecturas de frío y la compara
  con la anclada, e indica qué funciones consultar en Etherscan para repetir la verificación sin pasar por el camal.

El retiro vive en un contrato aparte, `RetirosSanitarios`, que **lee** `CadenaCarnica` sin modificarlo.
Solo la wallet que lo despliega (la autoridad) puede registrar órdenes, y `cajaBajoRetiro(caja)` decide
en la cadena si una caja está alcanzada: si contiene una pieza de la canal retirada o si es carne molida
cuya mezcla la incluye. Con el lote real alcanza **69 cajas** (14 directas + 55 de molida). De las 14
directas, 3 se vendieron después de la orden (CJ-0251, CJ-0276 y CJ-0294), y también 38 ventas de molida.
No bloquea ventas: el retiro automático es el Nivel 3.

`consulta/datos_publicos.json` trae solo lo publicable (cortes, predios y lecturas de frío): ningún
nombre de persona ni de cliente ni dirección.

## Interfaz

Tema negro y dorado "Camal Metropolitano". La **App Admin** (`app/index.html`) pide inicio de sesión del
administrador y ofrece, además de los cinco criterios y el retiro sanitario:

- **Buscador global** en la barra superior: entiende cajas (`CJ-…`), canales (`CN-…`), despachos (`DSP-…`)
  y códigos de venta (`QR-…`) y lleva a la consulta correcta.
- **Alertas del lote** (campana y panel de Inicio), calculadas desde los contratos: retiro vigente, ventas
  posteriores a la orden, despachos con frío no demostrado y cajas rechazadas.
- **Catálogo de cortes**: rendimiento de referencia de los 15 cortes frente al tope físico que calcula el contrato.
- **Etiqueta y QR**: etiqueta de trazabilidad de una venta, imprimible, con el QR hacia la consulta pública.
- **Lista de clientes a notificar** del retiro hacia adelante, descargable en CSV.
- Tarjeta de **wallet** conectada y estado de Sepolia con el número de bloque.

Si existe una foto de un corte (`app/corte.jpg`), se muestra sobre la portada. La consulta del consumidor
(`consulta/`) usa el mismo tema y se adapta a celular y computadora.

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
contracts/CadenaCarnica.sol       Nivel 1: custodia y regla física (Solidity ^0.8.20)
contracts/RetirosSanitarios.sol   Nivel 2: órdenes de retiro sobre el lote
app/index.html                    App Admin: conexión, carga del lote, los 5 criterios y el retiro
app/lote_nivel1.json              datos del lote para la App Admin (generado; incluye nombres, no se publica)
consulta/index.html               página pública del consumidor (Nivel 2)
consulta/datos_publicos.json      datos publicables para la consulta (generado)
scripts/preparar_lote.py          genera los dos JSON desde los CSV del reto
tests/probar_contrato.py          prueba de punta a punta de ambos contratos con el lote real
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
   La App Admin pide **iniciar sesión**: solo el administrador entra, con su correo y contraseña o firmando
   con la wallet admin en MetaMask. Es un control de acceso a la interfaz; lo que protege los datos son
   los contratos.
4. **Cargar el lote** (solo en un contrato nuevo): *Conectar MetaMask* → *Cargar lote* (unas 37
   transacciones, unos 58 M de gas). La carga es reanudable.
5. **Demo del Nivel 1**: recorrer las secciones 1 a 5 del menú. Las consultas funcionan sin wallet (RPC público).
6. **Nivel 2**: desplegar `contracts/RetirosSanitarios.sol` en Remix (optimizador activado), pasándole en
   el constructor la dirección de `CadenaCarnica`. Pegar su dirección en `contratoRetirosDireccion`
   (`app/index.html`) y en `contratoRetiros` (`consulta/index.html`). En la App Admin, sección *Retiro
   sanitario* → registrar la orden, con la misma wallet que desplegó el contrato.
7. **Publicar la consulta**: arrastrar la carpeta `consulta/` a [Netlify Drop](https://app.netlify.com/drop)
   y abrir `https://<sitio>.netlify.app/?codigo=QR-0294-1639` desde el celular.

**Prueba automática del contrato:**
```
pip install -r tests/requirements.txt
python tests/probar_contrato.py
```
Despliega los contratos en una EVM local, carga el lote completo con la misma lógica que la app,
comprueba los cinco criterios del Nivel 1, registra el retiro y verifica qué cajas alcanza.

## Alcance

Este repositorio implementa los **Niveles 1 y 2** del brief. Queda fuera el Nivel 3: sensores que firman,
habilitación en origen y retiro automático.
Supuestos, limitaciones y costos: ver [docs/laminas.md](docs/laminas.md).
