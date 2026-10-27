# BRIEF PARA CLAUDE WEB · Presentación del proyecto «De la vaca al plato, sin perder el hilo»

> **Cómo usar este archivo.** Súbelo a Claude web junto con las 18 imágenes de la carpeta `imagenes/` (lista en la sección 11) y escribe: *«Lee BRIEF_PRESENTACION.md completo y construye la presentación tal como lo pide. Entrégame un archivo .pptx de 16:9, editable, con notas del orador. Antes de empezar, dime en tres líneas qué entendiste y qué datos te faltan.»*

---

## 1. La tarea

Construye una **presentación en PowerPoint (.pptx, 16:9, 13,33 × 7,5 in)** para un pitch de **15 minutos**, con:

- **Estructura y rigor de consultora McKinsey**: titulares que son conclusiones, una idea por diapositiva, evidencia en cada una, fuentes al pie.
- **Dramaturgia de *Shark Tank***: abrir con un golpe, probar con una demostración, justificar con números, defenderse de objeciones y cerrar con una petición clara.
- **La estética exacta de nuestras páginas web** (sección 4): carbón verdoso y oro, tipografía IBM Plex.
- **Capturas reales de nuestras páginas** como pruebas (sección 11), no maquetas inventadas.

**Entregables**
1. `.pptx` con **16 diapositivas principales** + **6 de apéndice** (sección 6 y 7). Texto editable, gráficos y tablas nativos, nunca imágenes de texto.
2. **Notas del orador** en cada diapositiva: lo que se dice (frase por frase), el tiempo asignado y la señal para pasar a la siguiente.
3. Si no puedes generar `.pptx`, entrega un artefacto HTML paginado con el mismo contenido.
4. Al final, una lista corta de **suposiciones que hiciste** y de **datos que tuve que completar yo** (sección 10).

Idioma: **español neutro**, directo y sin jerga innecesaria. Los títulos de diapositiva en oración, no en mayúsculas.

---

## 2. Contexto del evento

- **Qué es:** el Reto 04 de un hackathon de blockchain (caso ficticio: Camal Metropolitano de San Ramón de Altamira, empresa pública EPM-RASRA, República de Andania). **Todos los datos son sintéticos.**
- **Formato de exposición (lo fija el docente):** pitch de **15 min**, **10 min de preguntas** del jurado y **5 min de respuestas**, estilo *Shark Tank*. Las diapositivas deben servir también para **responder preguntas** (de ahí el apéndice).
- **Cómo nos evalúan** (rúbrica del reto):

| Criterio | Peso | Dónde lo atacamos |
|---|---:|---|
| Prototipo funcional | 30 % | Demo en vivo + capturas (diap. 7–11) |
| Manejo de la división y la mezcla de la cadena | 20 % | Diap. 5 y 7 (molida = mezcla de lote) |
| Pertinencia de blockchain y problema del oráculo | 15 % | Diap. 6 y 14 |
| Utilidad para el consumidor | 15 % | Diap. 11 |
| Viabilidad y adopción | 10 % | Diap. 13 |
| Presentación | 10 % | Todo este archivo |

- **Lo que el jurado NO quiere ver:** un QR con la foto de una vaca sin verificación real; nombres o direcciones en una cadena pública; un token sin razón funcional; exigir lectores especiales en las tercenas; **prometer que blockchain resuelve el «problema del oráculo»** (que alguien teclee un dato falso). Evita todo eso, también en el discurso.
- **Alcance real del proyecto:** Nivel 1 (custodia + verificador en los dos sentidos + regla física) y Nivel 2 (consulta pública del consumidor con alerta de retiro) **completos y desplegados**. Nivel 3 (sensores que firman, credenciales verificables, retiro automático) **no implementado**: va como hoja de ruta. No lo presentes como hecho.

---

## 3. Estilo: McKinsey × Shark Tank

### Reglas McKinsey (aplícalas siempre)
1. **Titular de acción:** cada título es una oración completa con la conclusión («El contrato rechaza 91 kg de lomo fino que no existen»), máximo **2 líneas**. Quien lea solo los títulos debe entender la historia completa.
2. **Respuesta primero:** el resumen ejecutivo va en la diapositiva 3, no al final. Estructura SCQA: Situación → Complicación → Pregunta → Respuesta.
3. **Una idea por diapositiva.** Si necesitas dos ideas, son dos diapositivas.
4. **Evidencia visible:** cada afirmación se apoya en un gráfico, una tabla o una captura. Gráficos con título, unidades y fuente.
5. **Recuadro «Implicación»** (una línea, abajo a la derecha en las diapositivas de contenido): qué significa esto para el jurado.
6. **Pie de diapositiva:** «Fuente: …» a 9 pt, número de diapositiva «n / 16» y el rótulo de sección (*tracker*) arriba a la izquierda, en versalitas con espaciado: `01 · EL PROBLEMA`.
7. **Estructura MECE** en listas: sin solapes ni huecos; 3 o 4 puntos por lista, nunca más de 5.
8. **Sin adornos:** nada de clip art, sombras exageradas ni íconos decorativos. El color significa algo.

### Reglas Shark Tank (dramaturgia)
1. **Abrir con el golpe, no con el logo.** La primera frase hablada es la de la diapositiva 2.
2. **Un número para recordar: «514 porciones».** Debe aparecer en la apertura, en el problema y en el cierre.
3. **Demostrar, no contar.** Las diapositivas 7 a 11 se acompañan de **demo en vivo** (guion en sección 9). Las capturas son el plan B y el apoyo visual.
4. **Defenderse con humildad.** Hay una diapositiva de honestidad (14) antes de la petición: los «tiburones» respetan a quien dice sus límites antes de que se los pregunten.
5. **Cerrar con una petición concreta** (diapositiva 15) y una frase final memorable (16).
6. **Un momento de atrezo:** se entrega una **etiqueta impresa** a un miembro del jurado para que escanee el QR con su teléfono (sección 9).

---

## 4. Sistema visual (idéntico al de las páginas web)

**Principio:** mismo mundo que la web. Las diapositivas de **contenido** van sobre fondo claro; las de **portada, transición, petición y cierre** van sobre fondo carbón. El oro es el único acento; verde, rojo y ámbar **solo** significan estado.

### Color

| Rol | Nombre | Hex | Uso |
|---|---|---|---|
| Fondo oscuro | carbón 900 | `#0E1612` | portada, transición, petición, cierre |
| Fondo oscuro profundo | carbón 950 | `#080D0B` | degradados de portada |
| Superficie oscura | carbón 800 | `#15201A` | tarjetas sobre fondo oscuro |
| Fondo claro | neutro 50 | `#F4F5F2` | fondo de contenido |
| Tarjeta | blanco | `#FFFFFF` | tarjetas y capturas sobre fondo claro |
| Línea | neutro 200 | `#DFE3DC` | bordes, rejillas |
| Texto | neutro 900 | `#16211B` | cuerpo y títulos |
| Texto secundario | neutro 600 | `#566259` | notas, fuentes |
| **Acento oro** | oro 500 | `#C9A24B` | acento, cifras clave sobre oscuro |
| Oro claro | oro 300 | `#E7CD8B` | texto dorado sobre oscuro |
| **Oro para texto sobre claro** | oro 800 | `#7C5F18` | etiquetas y tracker sobre fondo claro (contraste de 5,5 a 6:1) |
| Oro fondo | oro 100 | `#F6EFD9` | resaltados suaves |
| Estado correcto | verde | `#2E7D5B` (texto `#1B5A40`, fondo `#E4F2EA`) | solo «cumple / verificado» |
| Estado alerta | rojo | `#B3423A` (texto `#8C2F28`, fondo `#FBEDEB`) | solo «retiro / rechazo / riesgo» |
| Estado aviso | ámbar | `#B7791F` (texto `#8A5A0F`, fondo `#FCF1DC`) | solo «límite / advertencia» |

**Prohibido:** usar oro para texto pequeño sobre fondo claro (usa `#7C5F18`), mezclar rojo y verde como decoración, degradados morados/azules, y cualquier color fuera de esta tabla.

### Tipografía (familia única IBM Plex, de Google Fonts)

| Uso | Fuente | Tamaño | Peso |
|---|---|---:|---|
| Titular de acción | IBM Plex Serif | 28 pt | 600 (una palabra clave en *cursiva dorada* cuando aporte) |
| Cifras grandes (KPI) | IBM Plex Serif | 44–60 pt | 600 |
| Subtítulo | IBM Plex Sans | 16 pt | 500 |
| Cuerpo | IBM Plex Sans | 14 pt (mínimo 12) | 400 |
| Etiquetas / tracker | IBM Plex Sans | 11 pt, MAYÚSCULAS, espaciado +1,2 pt | 600 |
| Códigos, hashes, direcciones | IBM Plex Mono | 11–12 pt | 400 |
| Pies y fuentes | IBM Plex Sans | 9 pt | 400 |

Si PowerPoint no tiene IBM Plex, deja los nombres de fuente indicados y avísame para instalarlas; **no sustituyas por Arial/Calibri sin avisar**.

### Maquetación
- Márgenes de 0,6 in; rejilla de 12 columnas; mucho aire. Contenido máximo en 2 zonas por diapositiva (por ejemplo, captura + 3 cifras).
- **Capturas:** borde de 1 px `#DFE3DC`, esquinas redondeadas (8 px) y sombra muy suave. Anótalas con **círculos dorados numerados** (1, 2, 3) y explica cada número en una lista corta al lado. Nunca estires una captura: recórtala.
- **Capturas de celular:** colócalas dentro de un marco de teléfono simple (rectángulo redondeado `#0E1612`, 8 px de grosor).
- **Gráficos:** sin fondo ni rejilla pesada; una sola serie destacada en oro; el tope o límite en línea discontinua ámbar; el problema en rojo.
- **Fondos oscuros:** puedes usar `foto_hato.jpg` o `foto_vaca.jpg` con un velo carbón del 70 al 90 % para legibilidad. Nunca sobre las diapositivas de contenido.
- **Logo:** `00_logo_toro.png` (toro dorado, transparente). En portada grande; en el resto, pequeño arriba a la derecha junto al texto «Camal Metropolitano».

---

## 5. Datos verificados (úsalos tal cual; no inventes otros)

Todos salen del dataset del reto y de las pruebas reales sobre los contratos desplegados en Ethereum Sepolia.

### El caso
| Dato | Valor |
|---|---|
| Lote | **LF-2026-0188** · ingreso 10 ago 2026, faena 11 ago, desposte y empaque 12 ago, despachos 12–13 ago |
| Animales | 60 bovinos, 9 predios, 4 introductores |
| Canales | 57 (54 aprobadas, 1 decomiso parcial, 2 decomiso total) → **55 despostadas**, 825 piezas (15 cortes × 55) |
| Cajas | 370 en el archivo → **364 registradas** + **6 rechazadas** por el contrato |
| Despachos / ventas | **12 despachos** (5 mayoristas y 7 minoristas directos); 150 redistribuciones; **264 ventas** con código de consulta |
| Laboratorio | LAB-2026-0911: **Salmonella spp. POSITIVO** en la canal **CN-0188-012** (muestreo 12 ago, resultado y notificación 14 ago, 14:20) |
| Orden de retiro | **RS-2026-004**, 14 ago 16:00, plazo 24 h. El acta dice: «14 cajas alcanzadas, 11 retiradas, estado EJECUTADO» |

### Lo que demuestra nuestro sistema (calculado desde la cadena)
| Dato | Valor |
|---|---|
| Cajas alcanzadas por la canal CN-0188-012 | **69** = 14 directas + **55 de carne molida** (mezcla de lote) |
| Peso alcanzado | **1.659 kg** (276 kg directas + 1.383 kg de molida) |
| Clientes a notificar | **15** (5 mayoristas + 10 minoristas) |
| Cobertura del acta oficial | 14 de 69 cajas = **20 %**; retiradas 11 = **16 %**. El acta **omitió toda la carne molida** |
| Ventas posteriores a la orden | **41 ventas** (3 de cortes directos: CJ-0188-0251, CJ-0188-0276, CJ-0188-0294; 38 de molida) = **514 porciones** (41 + 473), del 14 al 20 de agosto, en **10 puntos de venta** |
| Caso del consumidor | Caja **CJ-0188-0294** (pecho, 20,83 kg, de las canales 10, 11 y 12), vendida el **15 ago a las 18:00 (26 h después de la orden)**, 12 porciones; código de consulta **QR-0294-1639** |
| Ventas por día tras la orden (ventas / porciones) | 14 ago: 4 / 50 · 15 ago: 7 / 110 · 16 ago: 12 / 117 · 17 ago: 10 / 119 · 18 ago: 5 / 86 · 19 ago: 1 / 14 · 20 ago: 2 / 18 |
| Consulta hacia adelante | una sola llamada al contrato, **0,3 a 0,6 s** con un nodo público (la primera consulta puede tardar ~1 s) |

### Balance de masa (criterio 3)
| Dato | Valor |
|---|---|
| Lomo fino con piezas reales empacado | **187,13 kg** |
| 6 cajas sin piezas (CJ-0188-0365 a 0370) | **90,94 kg** |
| Total si el contrato las aceptara | **278,07 kg** |
| Tope físico del lote | **205,45 kg** (1,6 % del peso frío despostado de 12.588,62 kg, más 2 % de tolerancia) |
| Exceso | **72,62 kg** más de lo que el lote puede dar. Respuesta del contrato: `CAJA SIN PIEZAS` |
| Caja duplicada | CJ-0188-0321 (molida, 25,79 kg) figuraba en DSP-0188-001 y DSP-0188-002; el contrato rechaza el segundo con `CAJA YA DESPACHADA` |

### Cadena de frío (criterio 4)
Despacho **DSP-0188-006** (VH-01 → cliente CL-R01). Salida 16:32, llegada 20:02, límite 4 °C. Lecturas: **16:32 → 2,2 °C · 16:47 → 2,5 · 17:02 → 2,6 · 19:32 → 2,0 · 19:47 → 2,2 · 20:02 → 2,3**. No hay lecturas entre las 17:02 y las 19:32: **135 minutos sin lecturas** (150 min de silencio menos los 15 min esperables). Declaraba `cumple = SÍ`. Es 1 de los 12 despachos; los otros 11 demuestran su frío. Según el manual, un período sin registro **es** una rotura de cadena de frío.

### Privacidad (criterio 5)
Se leyeron las historias de las **364 cajas** (1.335.104 bytes) y se buscaron **101 textos sensibles** (26 del personal, 45 de clientes y direcciones, 27 de predios e introductores, 3 estaciones): **0 encontrados**. Por lo tanto, la cadena guarda solo números, códigos seudónimos (OP-24, CL-R05) y huellas (hash).

### Trazabilidad hacia atrás (criterio 1)
La caja CJ-0188-0294 cumple el **factor de trazabilidad 7/7** (sección 5 del manual MP-RAS-TRZ-001): animal, estado sanitario, canal y sello, historia térmica, corte, unidad de venta y custodia comercial. Se remonta a 3 animales (canales 010, 011, 012).

### Hallazgos en los datos (7 inconsistencias sembradas por el reto)
| # | Inconsistencia | Qué hace el sistema |
|---|---|---|
| 1 | Animal ingresó con vacuna de aftosa vencida | **Registra, no detecta** (requiere Nivel 3) |
| 2 | Un veterinario selló 41 canales en 9 minutos, fuera de su turno | **Registra, no detecta** (Nivel 3) |
| 3 | 6 cajas de lomo fino sin piezas (278 kg vs 205 kg) | **Rechazada por el contrato** |
| 4 | Hueco de frío de 135 min en un despacho que declara cumplir | **Detectada** y marcada en rojo |
| 5 | Fecha de etiqueta adelantada 2 días en 14 cajas | **Registra la fecha real**; no la compara automáticamente |
| 6 | Caja en dos despachos | **Rechazada por el contrato** |
| 7 | Retiro «ejecutado» con ventas posteriores | **Detectada** (41 ventas, 514 porciones) |

Resumen honesto: **4 de 7 detectadas o rechazadas automáticamente**, 3 quedan registradas de forma inmutable. Además, el sistema reveló que **el acta omitió la molida**.

### Tecnología y costos
| Dato | Valor |
|---|---|
| Red | Ethereum **Sepolia** (red de pruebas, chainId 11155111) |
| Contrato 1 · custodia | `CadenaCarnica` · `0xE78e4382984014D8b15B001ff9054aE9790a79ce` |
| Contrato 2 · retiros | `RetirosSanitarios` · `0x4dAFa0621745559a636333898726A85Dee48c7Ec` (solo la autoridad registra retiros) |
| Carga del lote completo | 37 transacciones, **57,98 millones de gas** (≈ **1,05 M de gas por res**) |
| Costo anual, camal de 300 reses/semana | **Escenario A**, todo el detalle en red pública: ≈ **16.400 M de gas/año** = 16,4 ETH (a 1 gwei) o 164 ETH (a 10 gwei). **Escenario B (recomendado)**: red permisionada + anclaje diario de una raíz Merkle en red pública: ≈ **22 M de gas/año** = 0,02 a 0,22 ETH, **más** la operación de 4 nodos (supuesto de orden de miles de USD al año) |
| Estado del escenario B | **Es una recomendación de arquitectura, no está implementado.** Dilo así |
| Repositorio público | https://github.com/gabriel-toaquiza/Proyecto-CadenaCarnicaReto4 |
| Consulta pública | https://lambent-blancmange-7e26ae.netlify.app/?codigo=QR-0294-1639 (sin cuenta ni wallet) |

---

## 6. Guion diapositiva por diapositiva (pitch de 15:00)

> Formato de cada una: **Titular** · tiempo · contenido · exhibit · imagen · nota del orador.
> Tiempo total = 15:00. Las diapositivas de demo (7 a 10) se acompañan de demo en vivo.

**1 · Portada** · 0:15 · *fondo oscuro*
- Título: «De la vaca al plato, *sin perder el hilo*». Subtítulo: «Trazabilidad cárnica que cualquiera puede verificar».
- Logo grande, `foto_hato.jpg` con velo, nombre del equipo `[EQUIPO]`, integrantes `[INTEGRANTES]`, «Reto 04 · Caso San Ramón de Altamira».

**2 · El gancho** · 1:00 · tracker `01 · EL PROBLEMA`
- Titular: «Una caja de la canal contaminada se vendió 26 horas después de ordenarse el retiro».
- Exhibit: **línea de tiempo** horizontal: 12 ago empaque → 14 ago 14:20 el laboratorio reporta Salmonella en CN-0188-012 → 14 ago 16:00 orden RS-2026-004 → 15 ago 18:00 se vende CJ-0188-0294 (12 porciones) → 20 ago última venta. Marca en rojo el tramo «ya estaba prohibido venderla».
- Cifra grande: **514 porciones** vendidas tras la orden.
- Nota: abre con la pregunta «Si usted compró este pecho de res el 15 de agosto, ¿quién le avisó?». Pausa de 2 segundos.

**3 · Resumen ejecutivo** · 0:45 · tracker `02 · RESUMEN`
- Titular: «Convertimos la trazabilidad en una verificación que cualquiera repite sin pedirle permiso al camal».
- Cuatro filas SCQA: **Situación** (los camales registran en sistemas que se pueden editar) · **Complicación** (la cadena se divide y se mezcla; el retiro tarda y se cumple a medias) · **Pregunta** (¿cómo encontrar cada caja en segundos y demostrarlo?) · **Respuesta** (registro inmutable + regla física que impone un contrato + consulta pública para el consumidor).
- Pie con 3 cifras: 69 cajas halladas en < 1 s · 4 de 7 anomalías detectadas · 0 nombres en la cadena.

**4 · El problema en cifras** · 0:45 · tracker `01 · EL PROBLEMA`
- Titular: «El retiro oficial alcanzó solo 14 de las 69 cajas afectadas: toda la carne molida quedó fuera del acta».
- Exhibit A: **barra apilada** de 69 cajas: 14 en el acta (20 %) · 55 omitidas, toda la molida (80 %). Marca las 11 «retiradas».
- Exhibit B: **columnas** de ventas por día tras la orden (4, 7, 12, 10, 5, 1, 2) con sus porciones.
- Fuente: dataset del reto y verificación en cadena.

**5 · Por qué es difícil** · 0:45 · tracker `01 · EL PROBLEMA`
- Titular: «Un animal produce 15 cortes y la carne molida mezcla todo el lote: la custodia no es una línea».
- Exhibit: **diagrama** de flujo con muchas a muchas: 1 canal → 15 cortes → cajas que juntan piezas de varias canales (ejemplo: CJ-0188-0003 reúne 4 canales) → **molida = mezcla de lote** (55 cajas, no se rastrea a un animal).
- Implicación: un modelo animal ↔ producto 1 a 1 no sirve; por eso un retiro debe alcanzar toda la mezcla.

**6 · La solución** · 1:15 · tracker `03 · LA SOLUCIÓN`
- Titular: «Un contrato registra cada traspaso y se niega a registrar carne que no existe».
- Exhibit: **arquitectura en tres bloques** (ver apéndice A1): *Origen del dato* (báscula, veterinario, desposte, empaque, despacho, venta) → *Dentro de la cadena* (custodia, regla física, huellas) / *Fuera* (nombres, lecturas de temperatura, documentos) → *Quién verifica* (inspector, auditor, calidad, consumidor).
- Imagen: `03_hilo_del_lote.png` (el hilo del lote: 7 etapas, todas «completas»).
- Dos contratos: custodia y retiros. Cinco reglas que el contrato impone: `CAJA SIN PIEZAS`, `PIEZA YA EMPACADA`, `PESO EXCEDE PIEZAS`, `EXCEDE RENDIMIENTO DEL LOTE`, `CAJA YA DESPACHADA`.

**7 · Demo 1 · Hacia adelante** · 1:30 · tracker `04 · LA PRUEBA`
- Titular: «En menos de un segundo sabemos qué cajas y qué clientes recibieron la carne de la canal enferma».
- Imagen: `06_hacia_adelante_retiro.png`, con círculos: ① 14 cajas directas + 55 de molida ② 15 clientes a notificar ③ 1.659 kg ④ filas en rojo: vendidas tras la orden.
- Cifras al lado: 0,3–0,6 s · 69 cajas · 41 ventas tardías.
- **Demo en vivo:** buscar `CN-0188-012`.

**8 · Demo 2 · Balance de masa** · 1:15 · tracker `04 · LA PRUEBA`
- Titular: «El contrato rechaza 91 kg de lomo fino que no tienen carne detrás».
- Exhibit: **barra horizontal apilada**: 187,13 kg con piezas reales (oro) + 90,94 kg sin piezas (rojo, rayado) contra una línea vertical discontinua en 205,45 kg (tope físico). Etiqueta «+72,62 kg sobre el tope».
- Imágenes: `07_balance_de_masa.png` y `08_simulador_del_contrato.png` (simulador: «el contrato responde sin escribir nada»).
- **Demo en vivo:** simulador → «Sin piezas» → `CAJA SIN PIEZAS`.

**9 · Demo 3 · Cadena de frío** · 1:00 · tracker `04 · LA PRUEBA`
- Titular: «Un despacho que declaró cumplir pasó 135 minutos sin una sola lectura de temperatura».
- Exhibit: **gráfico de líneas nativo** con la serie de la sección 5 (6 puntos), zona sombreada en rojo entre 17:02 y 19:32 rotulada «135 min sin lecturas» y línea ámbar discontinua en 4 °C. Debajo, tabla pequeña: 12 despachos, 11 con frío demostrado, 1 sin demostrar.
- Imagen: `09_cadena_de_frio.png`.
- Nota: las lecturas no están en la cadena; está su **huella**, y la app recalcula y compara.

**10 · Demo 4 · Origen y privacidad** · 1:00 · tracker `04 · LA PRUEBA`
- Titular: «Cada caja se remonta a su animal y la cadena no guarda un solo nombre».
- Imágenes: `05_hacia_atras_factor.png` (factor 7/7) y `10_privacidad.png` (tabla «lo que ve la cadena / lo que solo sabe el camal»; auditoría: 101 textos buscados, 0 encontrados).
- Cifras: 7/7 · 364 cajas leídas · 0 encontrados.

**11 · El consumidor** · 1:30 · tracker `05 · EL CONSUMIDOR`
- Titular: «Quien compró la carne recibe la alerta aunque el comercio diga que la venta se concretó».
- Imágenes: `14_consulta_movil_con_retiro.png` y `15_consulta_movil_sin_retiro.png` en marcos de teléfono, lado a lado («con retiro» frente a «sin retiro»); `13_consulta_computadora.png` más pequeña; `11_etiqueta_con_qr.png`.
- Mensajes: sin app, sin cuenta, sin wallet · el teléfono **recalcula la huella del frío** y la compara con la anclada · enlaces a Etherscan para repetir la consulta sin pasar por el camal.
- **Momento de atrezo:** ver sección 9.

**12 · Evidencia en datos reales** · 0:45 · tracker `04 · LA PRUEBA`
- Titular: «El sistema detectó o rechazó 4 de las 7 anomalías del lote y reveló que el acta omitió la molida».
- Exhibit: **tabla de 7 filas** de la sección 5, con un semáforo: verde «detecta/rechaza» (3, 4, 6, 7), ámbar «registra, no detecta» (1, 2, 5). Fila final: «Hallazgo extra: el acta omitió la molida».
- Nota: decir los 3 que no detectamos **antes** de que pregunten.

**13 · Viabilidad** · 1:15 · tracker `06 · VIABILIDAD`
- Titular: «Con una red permisionada y un anclaje diario, el anclaje público de un camal de 300 reses por semana cuesta menos de 0,25 ETH al año, más la operación de los nodos».
- Exhibit: **tabla comparativa de dos escenarios** (sección 5) y, al lado, tres puntos de adopción: la etiqueta ya lleva un código impreso (no hay lector especial) · la tercena vende como siempre y el consumidor verifica desde su teléfono · el cargador **ancla lo que el sistema del camal ya registra**, no lo reemplaza.
- Etiqueta visible: «Estimación; el escenario B no está implementado».
- Imagen pequeña: `11_etiqueta_con_qr.png`.

**14 · Honestidad** · 0:45 · tracker `07 · LÍMITES`
- Titular: «La cadena no impide que alguien teclee un dato falso: impide que la historia se cambie después».
- Tres columnas: **Lo que resuelve** (nadie reescribe la historia; la regla física la impone el contrato; el retiro es una consulta pública) · **Lo que no resuelve** (el oráculo: balanza, sello o sensor que mienten; hoy las lecturas las firma el camal, no el sensor; cualquier wallet puede escribir en el contrato de custodia) · **Qué sigue** (sensores que firman, credenciales verificables de vacunación, retiro automático).
- Nota: tono sereno; esta diapositiva **gana puntos** en «pertinencia y oráculo».

**15 · La petición** · 1:00 · tracker `08 · LO QUE PEDIMOS` · *fondo oscuro*
- Titular: «Pedimos un piloto de 90 días en un camal real para llevar el sistema de la prueba a la operación». `[AJUSTAR CON EL EQUIPO]`
- Hoja de ruta de tres fases en una línea (iconografía mínima): **Días 0–30** integrar con el sistema del camal y definir la red permisionada · **Días 31–60** sensores y balanza que firmen sus lecturas · **Días 61–90** retiro automático y credenciales de origen, con ANSA y ARSA.
- Tres cosas que se piden: 1) un camal piloto, 2) el aval de la autoridad sanitaria, 3) acceso a un sensor y una balanza reales. `[AJUSTAR]`

**16 · Cierre** · 0:15 · *fondo oscuro*
- Frase: «*La confianza también se traza.*» y la cifra **514 porciones**.
- QR a la consulta pública, enlace del repositorio, contacto `[CONTACTO]`.

---

## 7. Apéndice (para el turno de preguntas; no se presenta)

- **A1 · Arquitectura técnica:** diagrama completo (origen del dato → dentro/fuera de la cadena → verificadores), con las dos direcciones de contrato y la red.
- **A2 · Las cinco reglas que impone el contrato:** tabla (regla · error que devuelve · ejemplo del lote).
- **A3 · Cobertura del reto:** matriz de los 5 criterios del Nivel 1 y los 2 del Nivel 2 con estado ✅ y la captura que lo prueba; Nivel 3 con estado «hoja de ruta».
- **A4 · Costos y supuestos:** el cálculo de gas (57,98 M de gas ÷ 55 canales = 1,05 M de gas por res; × 300 reses × 52 semanas) y los supuestos de la red permisionada.
- **A5 · Banco de preguntas:** las de la sección 8, en una tabla de dos columnas.
- **A6 · Equipo y reparto de roles** `[COMPLETAR]`.

---

## 8. Banco de preguntas de los «tiburones» (con respuesta lista)

**El tecnólogo**
1. *¿Por qué blockchain y no una base de datos?* — Porque quien registra es quien tendría que responder en un retiro. En una base de datos editable se puede agregar kilos o borrar un hueco de frío después de ver los números; aquí no, y cualquier inspector lo verifica sin pedir permiso.
2. *¿Qué pasa si la balanza o el veterinario mienten?* — La cadena guarda la mentira, pero la hace permanente y atribuible: no podemos impedir el dato falso, sí la manipulación retroactiva. Los sensores que firman son la siguiente fase.
3. *¿Por qué una red de pruebas?* — Es un prototipo. En producción, recomendamos una red permisionada entre camal, mayoristas y autoridad sanitaria, con un anclaje diario en red pública.

**El financiero**
4. *¿Cuánto cuesta?* — El lote completo costó 58 M de gas, 1,05 M por res. A 300 reses por semana, todo en red pública sería inviable; por eso proponemos el escenario B: unas centésimas de ETH al año de anclaje más los nodos.
5. *¿Quién paga y por qué?* — Hipótesis a validar con el piloto: el camal, porque evita retiros tardíos y sanciones, y gana confianza de mayoristas. `[AJUSTAR]`

**El experto sanitario**
6. *¿Y la carne molida?* — Es mezcla autorizada de lote: no se rastrea a un animal. Un retiro de cualquier canal que aportó a la mezcla alcanza toda la molida. Eso es lo que el acta omitió.
7. *¿Por qué no automatizaron el retiro?* — Es una decisión de alcance: hoy el sistema alerta al consumidor y lista cada caja y cliente; bloquear ventas automáticamente es la fase 3 de la hoja de ruta.
8. *¿Los umbrales son reales?* — Son los del manual del ejercicio (7 °C en 24 h, 0–4 °C, ±2 %); son plausibles pero están redondeados y debe revisarlos alguien de la planta.

**El operador**
9. *¿Cómo se integra con el sistema que ya tiene el camal?* — No lo reemplaza: ancla lo que ya registra. El cargador lee su exportación.
10. *¿Qué pasa con la tercena sin conexión?* — La etiqueta lleva el código impreso; la tercena vende como siempre. El consumidor verifica desde su teléfono, y la venta se registra cuando hay conexión.
11. *¿Qué impide que el camal omita registrar una venta?* — Nada: el contrato impide registrar más de lo que entró, no omitir. Por eso la conciliación entre lo despachado y lo registrado es parte del piloto.

**El jurado de seguridad y privacidad**
12. *¿Qué datos personales hay en la cadena?* — Ninguno: solo números, códigos seudónimos y huellas. Los seudónimos se pueden enlazar con la tabla interna del camal, y lo declaramos como límite.
13. *¿Y la seguridad del panel?* — El inicio de sesión es una barrera de la interfaz; lo que protege los datos son los contratos. El contrato de retiros solo acepta la wallet de la autoridad; el de custodia hoy no distingue roles, y agregarlos está en la hoja de ruta.

---

## 9. Guion del pitch en vivo

**Antes de entrar**
- Imprime **2 etiquetas** (`11_etiqueta_con_qr.png`, tamaño de una tarjeta) con el QR de `QR-0294-1639`.
- Abre en pestañas: panel de administración con sesión iniciada, la consulta pública y Etherscan de los dos contratos. **Graba un video de respaldo** de la demo completa (2 min).
- Prueba el celular con datos móviles y wifi; el QR abre la consulta pública.

**Reparto sugerido de voces** `[ADAPTAR]`: *A* abre y cierra (diap. 1–6, 15–16) · *B* hace la demo (7–10) · *C* habla del consumidor y de la viabilidad (11–14).

**Demo (4 a 5 minutos entre las diap. 7 y 10).** Orden: ① `CN-0188-012` hacia adelante, mostrar 69 cajas y las 41 en rojo ② simulador de balance: «Sin piezas» ③ cadena de frío: se abre sola en DSP-0188-006 ④ privacidad: «Auditar todas las cajas».

**Momento de atrezo (diap. 11).** *B* entrega la etiqueta impresa a un miembro del jurado: «Escanee el código con su teléfono». Aparece la **alerta roja de retiro** y, debajo, «Tu compra se registró el 15 ago 2026, después de ordenado el retiro». Frase: «El comercio registró que la venta se concretó; nuestro sistema le dice que no debía venderse».

**Si algo falla:** pasar al video de respaldo sin disculpas, y continuar con las capturas de la diapositiva.

**Cierre:** mirar al jurado, decir la petición (diap. 15), pausa, y la última frase: *«La confianza también se traza.»*

---

## 10. Reglas finales para Claude web

**No inventes.** Usa solo los datos de la sección 5. No agregues cifras de mercado, precios de carne, porcentajes de pérdida, nombres de empresas competidoras ni citas. Si un dato no está aquí, deja el marcador `[COMPLETAR]` y lo listas al final.

**Datos que debo completar yo** (déjalos como marcadores visibles, en oro, y avísame): `[EQUIPO]`, `[INTEGRANTES]`, `[CONTACTO]`, la petición exacta de la diapositiva 15 y el modelo de ingresos de la pregunta 5.

**Cuida estas cuatro cosas:**
1. El escenario B de costos **no está implementado**: rotúlalo como recomendación.
2. El Nivel 3 es hoja de ruta, **no** funcionalidad.
3. No digas que blockchain «resuelve» el oráculo ni que «evita el fraude»: di que **impide la manipulación retroactiva**.
4. Cada captura debe corresponder a lo que afirma el titular.

**Lista de verificación antes de entregar**
- [ ] Los 16 titulares leídos de corrido cuentan la historia completa.
- [ ] Ninguna diapositiva de contenido tiene más de dos zonas ni texto por debajo de 12 pt.
- [ ] Todos los números coinciden con la sección 5.
- [ ] Cada diapositiva de contenido tiene fuente, número y tracker.
- [ ] Los gráficos son nativos y editables; rojo/verde/ámbar solo como estado.
- [ ] Hay notas del orador con tiempos que suman 15:00.
- [ ] Las capturas no están estiradas ni borrosas.
- [ ] El texto de las notas es hablado, en frases cortas, sin lenguaje de informe.

---

## 11. Archivos de imagen que acompañan este brief (carpeta `imagenes/`)

| Archivo | Qué muestra | Úsalo en |
|---|---|---|
| `00_logo_toro.png` | Logo dorado, fondo transparente | portada, cierre, esquina de cada diapositiva |
| `foto_hato.jpg` | Vaca Hereford en el páramo (panorámica) | fondo de portada y cierre (con velo) |
| `foto_vaca.jpg` | Retrato de la vaca | fondo de la petición (con velo) |
| `01_login.png` | Pantalla de ingreso del panel | apéndice A1, diap. 6 (opcional) |
| `02_inicio_portada.png` | Panel de administración: Inicio | diap. 6 (apoyo) |
| `03_hilo_del_lote.png` | «El hilo del lote»: 7 etapas con su estado | **diap. 6** |
| `04_alertas_del_lote.png` | Campana abierta con 4 alertas reales | diap. 12 (apoyo) |
| `05_hacia_atras_factor.png` | Caja CJ-0188-0294: factor 7/7 y 3 canales | **diap. 10** |
| `06_hacia_adelante_retiro.png` | Canal CN-0188-012: 69 cajas, ventas tras la orden | **diap. 7** |
| `07_balance_de_masa.png` | Medidor de lomo fino y 6 cajas rechazadas | **diap. 8** |
| `08_simulador_del_contrato.png` | Simulador: «El contrato la rechaza» | **diap. 8** |
| `09_cadena_de_frio.png` | Trayecto de DSP-0188-006 con el hueco de 135 min | **diap. 9** |
| `10_privacidad.png` | Qué ve la cadena vs. qué sabe el camal; auditoría 0/101 | **diap. 10** |
| `11_etiqueta_con_qr.png` | Etiqueta de trazabilidad con QR | **diap. 11 y 13** |
| `12_catalogo_de_cortes.png` | 15 cortes: rendimiento y tope físico | apéndice A2 |
| `13_consulta_computadora.png` | Consulta pública en computadora, con alerta | diap. 11 |
| `14_consulta_movil_con_retiro.png` | Celular: alerta roja de retiro | **diap. 11** |
| `15_consulta_movil_sin_retiro.png` | Celular: sin retiro, todo verificado | **diap. 11** |

Si el chat no admite 19 archivos a la vez, sube primero este brief y las imágenes `00`, `03`, `05` a `11`, `14` y `15`; el resto se puede enviar en un segundo mensaje.

*Nota de privacidad:* algunas capturas del panel muestran nombres en gris cursiva con la etiqueta «registro interno». Son datos sintéticos del ejercicio; si el jurado lo ve, la explicación es que esos nombres **viven fuera de la cadena** y solo el camal los conoce (es justo lo que muestra la diapositiva 10).
