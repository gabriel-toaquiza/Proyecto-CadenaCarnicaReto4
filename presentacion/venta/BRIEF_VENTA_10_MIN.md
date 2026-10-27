# BRIEF PARA CLAUDE WEB — Pitch de VENTA (Shark Tank × McKinsey), 10 minutos

## 0. Qué te pido
Crea una **presentación HTML de una sola página** (diapositivas a pantalla completa, navegables con flechas) para que **4 integrantes** vendan, en **10 minutos**, un **sistema de trazabilidad cárnica** a un panel de inversionistas/jurado. El objetivo no es explicar tecnología ni demostrar un caso: es **convencer de que este producto debe existir, que funciona y que alguien pagará por él**.

- Formato: títulos que son conclusiones (estilo McKinsey: "La trazabilidad que hoy existe no sobrevive a una auditoría"), una idea por diapositiva, poco texto, mucha imagen.
- Tono: Shark Tank. Abrir con un gancho, nombrar el dolor, mostrar el producto, probar que funciona, decir cómo se gana dinero, pedir algo concreto y cerrar con una frase.
- Idioma: español neutro. Cada diapositiva lleva **notas del orador** con el guion hablado (sección 6).
- Entrega: un `.html` (diapositivas + notas visibles con la tecla `N`), con barra de tiempo opcional (tecla `T`) que muestra el minuto objetivo de cada diapositiva.

## 1. El producto en una frase
**Camal Metropolitano · Trazabilidad**: un registro compartido e infalsificable que sigue cada res desde el predio hasta el plato, incluso cuando la carne se corta, se mezcla y se reparte. Si hay un problema, **se encuentra todo lo afectado en menos de un segundo** y **el consumidor lo ve desde su celular, sin instalar nada**.

Nombre de marca: *Camal Metropolitano — Del origen al corte perfecto*. Lema de portada: **"Cada corte cuenta una historia."**

## 2. Reglas de contenido (importante)
**PROHIBIDO:**
- Costos de gas, tokens o ETH de Sepolia, y cualquier cifra de consumo de la red.
- Datos del lote de demostración como "prueba del problema": nada de "41 canales", "6 cajas fantasma", "135 min sin lecturas", "14 de 69 cajas", "26 horas después", nombres de anomalías sembradas ni cuántas se detectaron.
- Nombres de personas, razones sociales o direcciones (el sistema justamente no los publica).
- Inventar mercado, precios, clientes, ingresos, cifras de pérdidas o estadísticas externas. Si hace falta un número que no está en este brief, escribe un **[PLACEHOLDER: …]** visible en la diapositiva y en las notas.

**El problema se cuenta en general**, con situaciones típicas de cualquier camal: una res se convierte en decenas de piezas que se mezclan en cajas; los registros en papel o en hojas de cálculo se pueden editar sin dejar rastro; un hueco en la cadena de frío se puede declarar "cumplido"; cuando hay un retiro sanitario no se sabe con certeza qué se vendió ni a quién; el consumidor no puede verificar nada.

**Datos del producto que SÍ puedes usar (verificados):**
- Cinco capacidades: (1) **hacia atrás**: de una caja al animal, predio, dictámenes, quién la despostó y su frío; (2) **hacia adelante**: de una canal a todas sus cajas y clientes en menos de un segundo (consulta de ~0,3 s con una sola llamada); (3) **balance de masa**: el contrato rechaza cajas cuyo peso no se respalda con piezas reales; (4) **cadena de frío recalculada** desde la telemetría, marcando el hueco aunque el transportista declare cumplir; (5) **privacidad**: en la cadena solo hay códigos seudónimos y huellas, nunca nombres ni direcciones, y el consumidor igual verifica su compra.
- Una res produce 15 cortes; las cajas juntan piezas de varias reses; la carne molida es mezcla de lote. El registro modela esto como un grafo de muchos a muchos (no una línea recta).
- Consumidor: escanea el QR de la etiqueta → ve el recorrido "del predio a tu mesa" → si hay retiro, ve una **alerta roja aunque la venta ya conste como concretada**. Sin app, sin cuenta, sin wallet.
- Arquitectura: contrato de trazabilidad + contrato de retiros sanitarios (solo la autoridad registra retiros), desplegados y funcionando en red de prueba Ethereum Sepolia; panel de administración con login; página pública del consumidor; las lecturas de temperatura se resumen y se anclan (no se suben una por una).
- Honestidad: la cadena **no resuelve el oráculo** (no garantiza que el dato de entrada sea verdadero); lo que elimina es la **manipulación retroactiva**: nadie puede cambiar ni borrar después lo que ya se registró, ni las lecturas que faltan.
- Estado: prototipo funcional en testnet, datos sintéticos, repositorio público. No hay clientes pagando todavía (no lo afirmes).

## 3. Sistema visual (misma estética que la web del producto)
- **Fondo carbón** `#080D0B` / `#0E1612` / `#15201A`; **oro** `#C9A24B` (acento), `#E7CD8B` (brillo), `#B8923D`; texto claro `#F4F5F2`; secundario `#A9B3AC`. Estados: ok `#2E7D5B`, alerta `#B3423A`, aviso `#B7791F`. Sobre fondo claro, texto dorado `#7C5F18`.
- **Tipografía** (Google Fonts): títulos **IBM Plex Serif** (peso 600, cursiva dorada para la palabra clave, como en "Cada corte cuenta una *historia*"), cuerpo **IBM Plex Sans**, datos y etiquetas **IBM Plex Mono** en mayúsculas con espaciado.
- Escala: 12/14/16/20/26/36/60 px. Un solo título por diapositiva (máx. 2 líneas), cifras grandes en serif.
- Elementos: etiqueta superior tipo "pastilla" con borde dorado (kicker), numeración "01/14", línea dorada fina como separador, tarjetas con borde sutil y esquinas de 14–18 px. Fotos con velo oscuro degradado para que el texto sea legible.
- Mínimo: texto ≥ 20 px en pantalla de 1920×1080; contraste AA; nada de clip-art ni emojis.

## 4. Imágenes (carpeta `imagenes/`, súbelas junto con este brief)
| Archivo | Qué es | Dónde usarla |
|---|---|---|
| `00_logo_toro.png` | Logo (toro dorado, fondo transparente) | Portada y cierre |
| `foto_hato.jpg` | Vaca y hato al atardecer, montañas | Portada (fondo) y cierre |
| `foto_retrato_vaca.jpg` | Retrato de vaca | Diapositiva del origen / gancho |
| `foto_corral.jpg` | Portón de corral al amanecer | El problema: el origen |
| `foto_cortes.jpg` | Cortes de carne sobre tabla | El problema: se divide y se mezcla |
| `foto_empaque.jpg` | Pieza empacada con etiqueta en blanco | Producto: etiqueta y QR |
| `foto_camion_frio.jpg` | Camión refrigerado abierto con cajas | Problema/solución: frío y retiro |
| `01_hilo_del_lote.png` | "El hilo": 7 etapas como etiquetas atadas a un cordel | Visión del producto (recortar a la franja de etapas) |
| `02_panel_navegador.png` | Panel de administración dentro de un navegador | Portada del producto |
| `03_hacia_atras.png` | Pantalla "de la caja al animal" | Prueba 1 |
| `04_hacia_adelante.png` | Pantalla "de la canal a los clientes" (tabla recortada) | Prueba 2 |
| `05_regla_fisica.png` | Simulador de la regla de balance de masa | Prueba 3 |
| `06_cadena_de_frio.png` | Gráfico de frío recalculado | Prueba 4 |
| `07_privacidad.png` | Comparativa "lo que NO está en la cadena" | Prueba 5 |
| `08_etiqueta_qr.png` | Etiqueta imprimible con QR | Consumidor |
| `09_celulares_consumidor.png` | Dos celulares: alerta de retiro y "sin retiros" | Consumidor (imagen clave) |

Reglas: usa las capturas **como están** (son del producto real); recórtalas con `object-fit: cover` o enmárcalas, no las redibujes. Algunas capturas contienen códigos de ejemplo del lote de demostración: úsalas como **pantallas del producto**, y **no las leas ni las comentes como "el caso"**. Si falta una imagen, deja un marco con el nombre del archivo, no generes una sustituta.

## 5. Estructura: 14 diapositivas + 3 de apéndice (≈10:00)
Voces: **A**, **B**, **C**, **D** (los 4 integrantes; completar nombres en `[INTEGRANTES]`). Reparto parejo ≈ 2:30 por persona.

| # | Min | Voz | Título (conclusión) | Contenido / imagen |
|---|---|---|---|---|
| 1 | 0:00–0:30 | A | **Cada corte cuenta una historia.** | Portada: `foto_hato` + logo + nombre del equipo `[EQUIPO]`. Una línea: "Trazabilidad cárnica infalsificable, del predio al plato". |
| 2 | 0:30–1:00 | A | Una res llega al plato como 15 cortes… y nadie sabe de cuál vienen | Gancho: `foto_retrato_vaca` → `foto_cortes`; flecha 1 → 15 → cajas → mesas. Pregunta al jurado: "¿Alguien sabe de qué animal es el último bistec que comió?" |
| 3 | 1:00–1:50 | A | El problema: la carne se divide, se mezcla y los registros se pueden editar | 3 tarjetas con foto: *Se divide y se mezcla* (`foto_cortes`), *Se registra donde se puede editar* (`foto_corral`), *El frío se declara, no se prueba* (`foto_camion_frio`). Sin cifras. |
| 4 | 1:50–2:25 | B | Cuando algo falla, retirar es adivinar | Línea de tiempo genérica: "hay un resultado de laboratorio → ¿qué cajas? ¿qué clientes? ¿ya se vendió?". Mensaje: la regla exige retirar en 24 h; sin trazabilidad no se puede cumplir ni demostrar. Y el consumidor es el último en enterarse. |
| 5 | 2:25–3:00 | B | Por qué hoy no se resuelve | Comparativa 3 columnas: *Papel/Excel* (editable), *Base de datos de un solo dueño* (el dueño puede reescribir), *Registro compartido* (nadie reescribe). Las dos primeras fallan ante una auditoría; la tercera no. |
| 6 | 3:00–3:45 | B | La solución: un hilo que no se puede cortar | `01_hilo_del_lote` + `02_panel_navegador`. Siete etapas: origen → inspección → faena y sello → frío → empaque → transporte → venta. Cada traspaso queda firmado con su responsable y su hora. Se modela como grafo, no como línea. |
| 7 | 3:45–4:35 | B/C | Prueba 1 y 2: del plato al animal y del animal al plato, al instante | `03_hacia_atras` y `04_hacia_adelante` lado a lado. "Una caja → su animal, predio, dictámenes, quién la despostó y su frío. Un animal → todas sus cajas y clientes en menos de un segundo." |
| 8 | 4:35–5:15 | C | Prueba 3 y 4: el contrato no deja mentir con kilos ni con frío | `05_regla_fisica` y `06_cadena_de_frio`. "No se puede registrar una caja que pese más de lo que respaldan sus piezas. Y el frío se recalcula desde la telemetría: un hueco es un hueco aunque se declare cumplido." |
| 9 | 5:15–5:50 | C | Prueba 5: trazabilidad pública sin exponer a nadie | `07_privacidad`. Dos columnas: *En la cadena*: códigos seudónimos y huellas. *Fuera de la cadena*: nombres, razones sociales, direcciones. "Verificable por todos, legible solo por quien debe." |
| 10 | 5:50–6:50 | C | El consumidor verifica con su celular, sin instalar nada | `09_celulares_consumidor` (grande) + `08_etiqueta_qr`. Escanea → recorrido "del predio a tu mesa" → si hay retiro, alerta roja aunque la venta ya conste como concretada. "Sin app, sin cuenta, sin wallet." **Momento demo (20 s):** mostrar la web real o el QR impreso. |
| 11 | 6:50–7:35 | D | Cómo se gana dinero | Modelo en 3 patas, **precios en placeholder**: *suscripción por camal* `[PRECIO]`, *tarifa por lote/etiqueta* `[PRECIO]`, *módulo de cumplimiento para autoridad y mayoristas* `[PRECIO]`. Quién paga y por qué: camal (evita multas y pérdida de marca), mayorista/cadena (prueba de origen), autoridad (retiros auditables). |
| 12 | 7:35–8:20 | D | Por qué se adopta: nadie compra un lector nuevo | Adopción: el operario usa el panel que ya conoce; la tercena no instala nada (el QR se lee con cualquier celular); el consumidor tampoco. Plan de entrada: un camal piloto → mayoristas → autoridad. Arquitectura en 1 imagen: red permisionada (camal, mayoristas, autoridad) + anclaje periódico en red pública. Lecturas de frío se resumen y anclan, no se suben una a una. |
| 13 | 8:20–9:00 | D | Lo que hacemos y lo que NO prometemos | Honestidad (credibilidad Shark Tank): *Hecho*: prototipo funcional en testnet con 2 contratos, panel y página pública. *No resuelve*: que el dato de entrada sea verdadero (el oráculo); solo evita que se **reescriba después**. *Falta*: sensores que firmen sus lecturas, habilitación en origen, retiro automático por resultado de laboratorio. *Supuestos y costo anual*: `[PLACEHOLDER: costo anual estimado para cientos de reses por semana, a completar con el equipo]`. |
| 14 | 9:00–10:00 | A→D | La petición y el cierre | Petición concreta `[PETICIÓN: monto / piloto / aval / acceso a un camal]` y `[USO DEL DINERO: 3 rubros]`. Cierre en grande sobre `foto_hato`: **"Cada corte cuenta una historia. Que sea verdadera."** + logo + `[CONTACTO]` + enlace al repositorio público. |

**Apéndice (no se presenta; para preguntas):** A1 arquitectura (qué va dentro y fuera de la cadena, dónde entra el dato); A2 honestidad extendida (supuestos, límites, costo anual, qué no se resuelve); A3 hoja de ruta: Nivel 3 (sensores firmados, credenciales verificables, retiro automático).

## 6. Guion hablado (≈1.300 palabras; ritmo 130 pal/min). Ajusta a las notas del orador de cada diapositiva.

**[A · 1–3, 0:00–1:50]**
"Buenas tardes. Somos `[EQUIPO]` y venimos a venderles algo que hoy no existe en ningún camal: **una carne que puede demostrar de dónde viene.**
Piensen en el último bistec que comieron. Una res se convierte en quince cortes distintos; esos cortes viajan en cajas junto con piezas de otros animales; y la carne molida es, literalmente, una mezcla de todos. Si mañana apareciera un problema sanitario, ¿de qué animal vino su bistec? Hoy, nadie puede responder con certeza.
El problema tiene tres raíces. Uno: la carne se divide y se mezcla, y un registro en línea recta no puede seguirla. Dos: los registros viven en papel, en hojas de cálculo o en bases de datos de un solo dueño, y cualquiera puede editarlos sin dejar rastro. Tres: el frío se declara, no se prueba; un transporte puede decir que cumplió aunque tenga horas sin registro."

**[B · 4–6, 1:50–4:35]**
"¿Qué pasa cuando algo falla? La norma exige retirar el producto en veinticuatro horas. Pero para retirar hay que saber qué cajas, qué clientes y si ya se vendió. Hoy se adivina, y el último en enterarse es el consumidor.
¿Por qué no se ha resuelto? El papel y el Excel se pueden editar. La base de datos tiene dueño, y el dueño puede reescribirla. Lo que necesitamos es un registro **que nadie, ni siquiera nosotros, pueda reescribir después**: un registro compartido.
Eso es lo que construimos. Un hilo de siete etapas, del predio a la mesa. Cada traspaso queda firmado con su responsable y su hora. Y no es una línea: es un grafo, porque un animal se divide en muchas piezas y una caja junta varios animales."

**[B→C · 7–9, 4:35–5:50]**
"Y funciona. Lo probamos con cinco capacidades. De una caja llegamos al animal, al predio, a los dictámenes y al frío. De un animal llegamos a todas sus cajas y clientes en menos de un segundo: eso es un retiro sanitario real. El contrato **rechaza** cajas que pesen más de lo que respaldan sus piezas: no se puede inventar carne. Recalculamos el frío desde la telemetría: un hueco es un hueco, aunque se declare cumplido. Y todo esto sin publicar un solo nombre ni una sola dirección: en la cadena solo hay códigos y huellas."

**[C · 10, 5:50–6:50]**
"Pero el cliente final es el consumidor. Miren: escanea el código de la etiqueta con su celular. Sin app. Sin cuenta. Sin billetera. Ve el recorrido del predio a su mesa. Y si existe un retiro, ve una alerta roja **aunque la venta ya conste como concretada**. *(Demo de 20 s.)* Es la primera vez que el consumidor puede verificar en lugar de creer."

**[D · 11–14, 6:50–10:00]**
"¿Cómo se gana dinero? Tres patas: suscripción por camal, tarifa por lote etiquetado y un módulo de cumplimiento para autoridades y mayoristas. `[PRECIOS]`. Paga el camal porque evita multas y protege su marca; pagan los mayoristas porque exigen prueba de origen; y la autoridad gana retiros auditables.
¿Se adopta? Sí, porque no pedimos lectores especiales: el operario usa un panel, la tercena usa su celular, el consumidor también. Entramos por un camal piloto, luego mayoristas y luego la autoridad.
Y seamos honestos: la cadena **no garantiza que el dato de entrada sea verdadero**; lo que elimina es la manipulación retroactiva. Hoy tenemos un prototipo funcional en red de prueba; faltan sensores que firmen sus lecturas, habilitación en origen y retiro automático. `[Costo anual para cientos de reses por semana]`.
Por eso venimos hoy: `[PETICIÓN]` para `[USO DEL DINERO]`. Porque cada corte cuenta una historia… y queremos que sea verdadera. Gracias."

## 7. Banco de preguntas (diapositivas de apéndice o respuesta oral; sin cifras de gas)
- *¿Quién garantiza que el dato es verdadero?* Nadie lo garantiza en origen: la cadena elimina la manipulación retroactiva. Para reducir el riesgo de entrada: sensores que firman lecturas y credenciales verificables (hoja de ruta).
- *¿Por qué blockchain y no una base de datos?* Porque una base de datos tiene un dueño que puede reescribirla; aquí participan camal, mayoristas y autoridad y ninguno puede alterar el historial.
- *¿Y la privacidad?* Solo seudónimos y huellas en la cadena; nombres y direcciones quedan fuera.
- *¿Cuánto cuesta operarlo?* `[PLACEHOLDER: a completar con el equipo]` — no citar costos de la red de prueba.
- *¿Qué pasa si el internet falla en la tercena?* El consumidor solo necesita su celular; el registro se carga por lotes desde el camal.
- *¿Qué hay de la molida?* Se rastrea hasta el lote (mezcla), nunca hasta un animal: lo decimos así a propósito.
- *¿Quién está pagando hoy?* Nadie todavía: es un prototipo con datos sintéticos; buscamos el piloto.

## 8. Instrucciones de calidad
1. Cada diapositiva debe poder entenderse en 3 segundos: título-conclusión + una imagen + máx. 3 líneas.
2. Respeta el tiempo de la columna "Min"; si no cabe, recorta texto, no reduzcas la letra.
3. No uses más de dos animaciones (entrada suave y el "hilo" que se dibuja en la diapositiva 6).
4. Deja los **[PLACEHOLDER]** y `[INTEGRANTES]`, `[EQUIPO]`, `[CONTACTO]`, `[PETICIÓN]`, `[PRECIO]` visibles y resaltados en oro para que el equipo los complete.
5. Al terminar, lista qué placeholders quedaron pendientes y confirma que no incluiste ninguna cifra prohibida.
