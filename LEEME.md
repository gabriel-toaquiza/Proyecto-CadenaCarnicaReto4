# Hackathon Blockchain — Caso “San Ramón de Altamira”

Cuatro retos independientes, construidos sobre procedimientos administrativos municipales reales,
reescritos por completo como material ficticio (el cuarto se redactó desde cero; ver más abajo). Los tres comparten un mismo universo: el
**Gobierno Autónomo Descentralizado del Distrito Metropolitano de San Ramón de Altamira**, en la
**República de Andania**. La entidad, el territorio, la normativa, las plataformas tecnológicas y
todas las personas mencionadas no existen.

Cada reto se puede correr solo. Si corren varios a la vez, los equipos comparten universo,
vocabulario y tipo de material, lo que facilita mucho la labor del jurado.

## Los cuatro retos

### Reto 01 — Trazabilidad verificable de concursos públicos
Un concurso de méritos y oposición para llenar una vacante en el servicio público: 30 actividades,
7 fases, dos tribunales y una plataforma central del ministerio. Cuando un postulante pierde y
sospecha que hubo arreglo, nadie puede probar lo contrario.

**Caso de trabajo:** concurso `MO-2026-0147`, 48 postulantes, 6 inconsistencias sembradas.
**Núcleo a construir:** un sellador de puntajes y un verificador que detecte alteraciones.
**Dificultad:** media. Buen reto de entrada.

### Reto 02 — Un remate público que nadie pueda torcer
Un remate coactivo: el municipio embarga un inmueble a quien le debe impuestos y lo subasta en una
ventana de 24 horas, en una plataforma que administra él mismo, siendo a la vez el acreedor.

**Caso de trabajo:** remate `RM-2026-0312`, 14 postores, 7 inconsistencias sembradas, varias de
ellas decisivas: cambian quién se lleva la casa y por cuánto.
**Núcleo a construir:** la ventana de posturas en un contrato, con reglas que se hagan cumplir solas.
**Dificultad:** media-alta. **Es el reto más fuerte de los tres** y el que da mejores demos.

### Reto 03 — El indicador que nadie puede recalcular
Una mesa de ayuda con tres niveles de soporte, un proveedor externo con penalidades contractuales,
y un indicador mensual que publica la misma unidad que se mide con él.

**Caso de trabajo:** julio de 2026, 187 tickets, 6 inconsistencias sembradas.
**Núcleo a construir:** un indicador que cualquiera pueda recalcular desde lo sellado.
**Dificultad:** alta, pero no por lo técnico. Es el reto donde menos obvio resulta que haga falta
blockchain, y donde se premia delimitar bien. **Asígnenlo a los equipos con más experiencia.**

### Reto 04 — De la vaca al plato, sin perder el hilo
La cadena cárnica del camal metropolitano: del ingreso del ganado en pie al consumidor final,
pasando por inspección sanitaria, faenamiento, oreo, desposte, empaque, despacho a mayoristas y
minoristas. Cuatro días después del faenamiento, un laboratorio reporta Salmonella y hay que
encontrar cada caja antes de que alguien la cocine.

**Caso de trabajo:** lote `LF-2026-0188`, 60 animales, 370 cajas, 7 inconsistencias sembradas.
**Núcleo a construir:** trazabilidad en los dos sentidos, con balance de masa y cadena de frío
verificables.
**Dificultad:** alta, por una razón propia: la cadena se divide y se mezcla. Un animal produce
quince cortes y la carne molida es mezcla de lote. Quien lo modele como custodia lineal se estrella.
**Es el reto con mejor demo del paquete** y el único donde el perjudicado es el ciudadano que come.

**Atención:** a diferencia de los otros tres, este manual no parte de un documento institucional —
se redactó desde cero reproduciendo la secuencia técnica común de los camales. Los límites (7 °C en
24 h, rendimientos de corte, tolerancias) son plausibles pero están redondeados. Si se presenta
ante una empresa pública de rastro, conviene que alguien de la planta lo revise antes.

## Qué contiene cada carpeta

```
Reto NN - Nombre/
  MP-…pdf                    El manual del procedimiento, ficticio y completo
  Reto NN - … (brief).pdf    El documento para participantes
  datos/                     CSV y JSON del caso, con su README
  mentores/                  NO ENTREGAR: clave de respuestas y notas de jurado
```

El **zip para participantes** de cada reto se arma copiando la carpeta **sin** `mentores/`.

## Formato previsto

Los briefs están escritos para **36 horas de construcción** y equipos que ya trabajan con
blockchain. Cada uno define un núcleo obligatorio con cinco criterios de aceptación que el equipo
puede comprobar por su cuenta, más dos niveles de extensión opcionales. Si su formato es distinto,
lo que hay que ajustar es la sección "Qué tienen que construir" y la agenda; el resto sirve igual.

## Lo que comparten los tres

Los cuatro datasets tienen la misma estructura de fondo y las mismas trampas de diseño:

- Una **bitácora de eventos** cuyo `hash_evento` se calcula sobre cada evento por separado y **no
  encadena con el anterior**, de modo que se puede borrar un evento intermedio sin que nada se
  rompa. Es la puerta natural hacia una propuesta de log encadenado o árbol de Merkle.
- **Campos calculados que mienten**: horas, porcentajes y banderas de cumplimiento que no coinciden
  con lo que resulta de recalcularlos desde los datos crudos. Los equipos que confían en el campo
  en vez de recalcular no encuentran nada.
- **Documentos sustituidos** bajo el mismo código, con hashes distintos y sin versionar.
- **Datos personales sensibles** que no pueden ir a una cadena pública bajo ningún concepto:
  acciones afirmativas en el 01, identificación de postores en el 02, contenido de tickets de
  seguridad en el 03, nombres de operarios y de clientes en el 04.

## Una advertencia que conviene dar en la apertura

Ninguna de estas soluciones impide que alguien introduzca un dato falso desde el teclado. El
problema del oráculo sigue vivo en los cuatro retos, y en el del camal está en su forma más cruda:
un sensor, una balanza y un sello de veterinario. Lo que sí se puede eliminar es la **manipulación
retroactiva**, y no es un premio de consolación: de las veintiséis inconsistencias sembradas en los
cuatro datasets, la gran mayoría son retroactivas, porque así ocurre en la realidad. Quien manipula
rara vez sabe de antemano a quién necesita favorecer; se entera cuando ya vio los números.

Decirlo en voz alta al abrir el hackathon ahorra que la mitad de los equipos prometa de más en la
presentación final.

## Variantes

Los cuatro datasets son deterministas, con semillas `20260147`, `20260312`, `20260701` y `20260811`. Cambiando la
semilla salen otros nombres, montos y ganadores, conservando la estructura y las anomalías. Sirve
si corren el hackathon en varias sedes o quieren una segunda edición sin que circulen las
respuestas.

## Sugerencia de asignación

Si van a correr los cuatro, el orden por dificultad creciente es **01 → 02 → 04 → 03**. El 02 da las
mejores historias de fraude, el 04 las mejores demostraciones y el 03 exige el criterio más maduro
para decidir dónde blockchain no corresponde. Si solo pueden correr dos, el 02 y el 04.
