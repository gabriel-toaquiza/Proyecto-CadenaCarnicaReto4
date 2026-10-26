# Dataset — Lote de faenamiento `LF-2026-0188`

Material para el **Reto 04 — De la vaca al plato, sin perder el hilo**.

Todo es **sintético**. Predios, animales, aretes, personas, clientes y la empresa pública
(EPM-RASRA, Camal Metropolitano de San Ramón de Altamira, República de Andania) son ficticios.
Pueden publicarlo, transformarlo y subirlo a una testnet sin ninguna restricción.

El proceso está descrito paso a paso en el manual
`MP-RAS-TRZ-001 V1.0 Trazabilidad de la cadena carnica.pdf`. **Léanlo primero**, y con especial
atención a la sección 5, el **factor de trazabilidad**, que define qué atributos debe llevar toda
unidad de producto para considerarse trazable. Esa sección es la especificación del reto.

## El caso

| | |
|---|---|
| Lote de faenamiento | `LF-2026-0188` |
| Ingreso del ganado | 2026-08-10 · Faenamiento 2026-08-11 · Desposte 2026-08-12 |
| Animales ingresados | 60 bovinos, de 9 predios y 4 introductores |
| Dictamen ante-mortem | 57 aptos · 2 retenidos · 1 decomiso |
| Canales obtenidas | 57 · aprobadas 54 · decomiso parcial 1 · decomiso total 2 |
| Piezas despostadas | 825, sobre 15 cortes de la carta |
| Cajas empacadas | 370 |
| Despachos | 12, a 5 mayoristas y 10 minoristas |
| Ventas al consumidor | 262 registros con código de consulta |
| Retiro sanitario | `RS-2026-004`, por Salmonella en la canal `CN-0188-012` |

Límites del manual: canal a **≤7 °C dentro de 24 horas**; cámaras y transporte entre **0 y 4 °C**;
sala de desposte a **≤12 °C**; balance de masa por canal con tolerancia de **±2%**; vida útil
contada desde la **fecha real de empaque**.

## Cómo se encadena la trazabilidad

```
arete SIGAN  →  canal  →  media canal  →  pieza de corte  →  caja  →  despacho
                                                              ↓
                              mayorista  →  minorista  →  venta al consumidor
```

El punto difícil de este reto, y lo que lo separa de una trazabilidad de bultos, es que la cadena
**se divide y se vuelve a juntar**. Un animal produce una canal, que produce 15 cortes distintos,
que se reparten en cajas. La mayoría de las cajas provienen de una sola canal, pero la carne molida
(`CT-15`) es **mezcla autorizada de lote**: no se puede remontar a un animal, solo al lote. Un
diseño que asuma una relación uno a uno entre animal y producto no va a funcionar aquí.

## Archivos

### `predios.csv` · `personal.csv` · `clientes.csv` · `carta_cortes.csv`
Los catálogos. `carta_cortes.csv` trae el **rendimiento de referencia de cada corte como porcentaje
de la canal**: es lo que permite saber si un corte rinde más kilos de los que físicamente puede.
`personal.csv` trae el cargo, el turno y **las fechas en que cada persona estuvo en turno**.

### `animales.csv` — 60 filas
Arete SIGAN, predio, introductor, transportista, guía de movilización, certificado sanitario,
fechas y **vigencia de vacunación contra aftosa y brucelosis**, sexo, edad, peso vivo, fecha y hora
de ingreso, corral.

### `inspeccion_ante_mortem.csv` — 60 filas
Dictamen (`APTO` / `RETENIDO` / `DECOMISO`), causa, veterinario que lo suscribe, hora y horas de
reposo cumplidas.

### `canales.csv` — 57 filas
Número de canal, arete de origen, hora de sacrificio, peso caliente, dictamen post-mortem, causa de
decomiso, **veterinario que selló, código de sello y hora exacta del sellado**, cámara de oreo.

### `temperatura_canales.csv` — 285 filas
Curva de descenso térmico por canal, a las 0, 6, 12, 18 y 24 horas, con el límite y el
cumplimiento. Dos canales no alcanzan el límite: es una desviación operativa registrada, no una
trampa.

### `cortes.csv` — 825 filas
Cada pieza obtenida: canal de origen, tipo de corte, peso, **operario que lo ejecutó**, hora, puesto
de trabajo y temperatura de la sala en ese momento.

### `balance_masa.csv` — 55 filas
Por canal: peso caliente, peso frío, suma de cortes, hueso, grasa, recortes y mermas, diferencia
porcentual y si está dentro de tolerancia.

### `cajas.csv` — 370 filas
La unidad de venta. Código de caja, corte, categoría, **canales de origen**, piezas contenidas,
peso, `fecha_empaque_real`, `fecha_empaque_etiqueta`, `fecha_vencimiento`, operario y cámara.
Que existan dos campos de fecha de empaque no es un descuido del dataset.

### `despachos.csv` · `despacho_cajas.csv` — 12 y ~368 filas
Vehículo, equipo de frío, precinto, despachador, horas de salida y llegada, temperaturas en ambos
extremos, integridad del precinto y cumplimiento declarado de cadena de frío. Y el detalle de qué
caja fue en qué despacho.

### `telemetria_frio.csv` — ~675 filas
Lecturas cada 15 minutos de los sensores de las dos cámaras y de cada vehículo en ruta, con
temperatura, límite y estado. **Comparen la telemetría contra el cumplimiento declarado en
`despachos.csv`, y fíjense también en lo que no está.**

### `redistribucion.csv` · `ventas_consumidor.csv`
El traspaso de cada caja del mayorista al minorista con temperatura de recepción, y la venta al
consumidor final con su código de consulta y las unidades en que se fraccionó.

### `analisis_laboratorio.csv` · `retiro_sanitario.csv`
Dos análisis microbiológicos, uno positivo, y la orden de retiro que se emitió en consecuencia, con
las cajas alcanzadas, las declaradas retiradas y el estado del retiro.

### `bitacora_eventos.csv` — ~440 filas
Cada evento con `timestamp`, `actor`, `rol`, `accion`, `entidad_afectada`, `referencia` y `detalle`.
Acciones: `REGISTRAR_INGRESO`, `DICTAMEN_ANTE_MORTEM`, `SACRIFICAR`, `DICTAMEN_POST_MORTEM`,
`SELLAR_CANAL_LOTE`, `REGISTRAR_BALANCE`, `EMPACAR`, `EDITAR_FECHA_ETIQUETA`, `DESPACHAR`,
`RECIBIR`, `REANUDAR_REGISTRO`, `RESULTADO_LABORATORIO`, `ORDENAR_RETIRO`.

El `hash_evento` se calcula sobre cada evento por separado y **no encadena con el anterior**.

### `lote_LF-2026-0188.json`
Todo junto, por si prefieren cargarlo de una vez.

## Por dónde empezar

1. Reconstruyan la cadena completa de una caja cualquiera hasta el animal, y de un animal hasta
   todas sus cajas. Si eso no corre, nada más importa.
2. Sumen los kilos despachados de cada corte y compárenlos con el rendimiento de referencia
   aplicado a las canales del lote.
3. Recalculen el cumplimiento de cadena de frío desde la telemetría, no desde el campo que lo
   declara. Cuenten también los minutos sin lecturas.
4. Contrasten las fechas de vacunación con las fechas de ingreso.
5. Cuenten cuántas canales selló cada veterinario y en cuánto tiempo, y crucen con sus turnos.
6. Comparen `fecha_empaque_real` contra `fecha_empaque_etiqueta`.
7. Busquen cajas que aparezcan en más de un despacho.
8. Tomen la orden de retiro y verifiquen si todas las cajas alcanzadas dejaron de venderse.

Hay **siete inconsistencias sembradas a propósito**. A diferencia de los otros retos, varias de
estas no cuestan dinero: cuestan salud pública.
