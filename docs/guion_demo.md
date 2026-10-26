# Guion de la demo · 5 minutos + 3 de preguntas

**Hilo conductor:** el retiro sanitario por Salmonella en la canal `CN-0188-012`.
**Antes de empezar:**
- App abierta con Live Server en la sección *Inicio*, con los totales a la vista (60 · 57/55 · 364 · 12 · 264).
- MetaMask conectado en Sepolia.
- Una pestaña con el contrato en Etherscan.
- El celular a mano y el QR `docs/qr_QR-0294-1639.png` impreso o en pantalla (lleva a la consulta pública en Netlify).
- Pulsar una vez cada botón para precalentar el RPC.

| Tiempo | Pantalla | Qué hacer | Qué decir |
|---|---|---|---|
| 0:00–0:25 | Inicio | Mostrar los totales | "Un camal faenó 60 reses y salieron 370 cajas. Cuatro días después, Salmonella en la canal 12. Hay que encontrar cada caja antes de que alguien la cocine. Todo este lote está registrado en Sepolia." |
| 0:25–1:15 | **2 · Hacia adelante** | `CN-0188-012` → *Buscar cajas y clientes* | "Una sola consulta al contrato: 14 cajas directas, y aparte 55 de carne molida, porque la molida es mezcla de lote y no se puede separar por animal. Estos son los clientes a notificar, en menos de un segundo. Cualquier inspector puede hacerla, sin pedir permiso al camal." |
| 1:15–1:55 | **1 · Hacia atrás** | `CJ-0188-0294` → *Reconstruir historia* | "Tomemos una de esas cajas, el pecho que terminó en una carnicería. Viene de 3 canales: aretes, predios, dictámenes, quién selló cada canal, quién la despostó y su curva de frío. El vínculo arete–canal no se puede perder ni cambiar." |
| 1:55–2:35 | **3 · Balance de masa** | *Intentar registrar las 6 cajas de lomo fino* | "En el lote aparecieron 6 cajas de lomo fino sin piezas detrás. El contrato las rechaza: no tienen piezas de respaldo, y juntas serían 278 kg contra un máximo físico de 205. No lo decide quien registra; lo impone el contrato." (Opcional: mostrar en Etherscan la transacción revertida.) |
| 2:35–3:10 | **4 · Cadena de frío** | *Recalcular cadena de frío* | "Cada despacho declara si cumplió con el frío. En la cadena guardamos la huella de las lecturas del sensor. Recalculamos: el despacho 6 dice que cumplió, pero tiene 135 minutos sin lecturas. Un hueco sin datos es una rotura de cadena de frío." |
| 3:10–3:45 | **5 · Privacidad** | *Ver datos crudos* → *Auditar todas las cajas* → *Verificar compra* con `QR-0294-1639` | "Esto es todo lo que la cadena sabe: números, códigos y huellas. Buscamos 98 nombres y direcciones en la historia de las 364 cajas: cero. Y aun así, el consumidor que compró con este código verifica que su compra existe y de qué caja salió." |
| 3:45–4:40 | **Nivel 2 · Consumidor** (celular) | Escanear el QR de `QR-0294-1639` con el celular | "Ahora soy la familia que compró este pecho. Escaneo la etiqueta: sin app, sin cuenta, sin wallet. La página lee directo de la blockchain y lo primero que dice es: retiro sanitario, no lo consumas. El registro comercial dice que la venta se concretó el 15 de agosto, un día después de la orden. Y no tengo que creerle a nadie: la huella del frío se recalcula en mi teléfono y el enlace a Etherscan me deja repetir la consulta." |
| 4:40–5:00 | Cierre | Volver a *Inicio* | "Lo que no resolvemos: si alguien teclea un peso falso, la cadena lo guarda. Lo que sí eliminamos es reescribir la historia: kilos que aparecen después, cajas despachadas dos veces y lecturas borradas." |

## Preguntas probables (3 min)

- **"¿Qué pasa si el veterinario sella sin mirar?"** La cadena lo guarda tal cual, pero con su código, su
  hora y su sello: queda atribuible para siempre. En el lote, el veterinario MV-03 selló 41 canales en
  9 minutos sin estar de turno; con este registro eso ya no se puede borrar ni maquillar después.
- **"¿Por qué blockchain y no una base de datos?"** Porque quien registra (el camal) es quien tendría
  que responder en un retiro. Una base de datos editable permite borrar el hueco de frío o agregar kilos
  después. Aquí no.
- **"¿Cuánto cuesta?"** El lote completo costó unos 58 M de gas, alrededor de 1 M por res. En
  producción: detalle en una red permisionada y un anclaje diario en red pública, con un costo de gas
  mínimo (ver lámina de honestidad).
- **"¿Y la carne molida?"** Es mezcla autorizada de lote. El modelo la vincula al lote: un retiro de
  cualquier canal que aportó a la mezcla alcanza toda la molida. Es lo conservador y lo correcto.
- **"¿Una tercena necesita algo especial?"** No. El código va impreso; el consumidor lo verifica desde
  su teléfono.

## Plan B
- Grabar la demo completa en video antes de presentar.
- Si el RPC público falla, conectar MetaMask: la app lee a través de su conexión.
- Tener abiertas capturas de las 5 pantallas con resultado.
