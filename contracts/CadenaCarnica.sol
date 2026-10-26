// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// =====================================================
// CADENA CÁRNICA · RETO 04 · NIVEL 1
// Registro de custodia del lote LF-2026-0188:
// arete → canal → piezas → caja → despacho → cliente
//
// Privacidad: el contrato no guarda nombres, razones sociales
// ni direcciones. Solo números, códigos seudónimos y hashes.
//
// Actor de cada traspaso: el código del campo "actor" (u operario,
// veterinario, despachador) más la wallet que firma la transacción,
// que junto con la hora del bloque queda en la propia transacción.
//
// Códigos de actor (se traducen en la app):
//   MV-xx → 100+xx · OP-xx → 200+xx · DS-xx → 300+xx
//   401 báscula de ingreso · 402 línea de faenamiento · 403 sala de desposte
//   CL-Mxx → 1000+xx · CL-Rxx → 2000+xx
// =====================================================

contract CadenaCarnica {

    // =====================================================
    // CONSTANTES DEL LOTE
    // =====================================================

    string public constant LOTE = "LF-2026-0188";

    uint8 public constant CORTE_MOLIDA = 15;

    // Tolerancia del balance de masa: 2 % = 200 puntos básicos
    uint256 public constant TOLERANCIA_PB = 200;

    // Rendimiento de referencia por corte, en centésimas de %
    // (1,6 % = 160). Índice 1 = CT-01 ... 15 = CT-15
    uint16[16] public rendimiento = [
        uint16(0), 160, 240, 320, 500, 460, 300, 340,
        100, 420, 680, 360, 540, 280, 300, 1100
    ];

    // =====================================================
    // ESTRUCTURAS
    // =====================================================

    struct Animal {
        uint64 arete;
        uint16 predio;
        uint32 fechaIngreso;
        uint32 pesoVivoG;
        uint8 dictamenAM;        // 1 APTO · 2 RETENIDO · 3 DECOMISO
        uint16 mviAM;
        uint16 actor;
        bytes32 hashDocumentos;  // guía, certificado sanitario y vacunación
    }

    struct Canal {
        uint8 numero;
        uint64 arete;
        uint32 fechaSacrificio;
        uint32 pesoCalienteG;
        uint8 dictamenPM;        // 1 APROBADA · 2 DECOMISO PARCIAL · 3 DECOMISO TOTAL
        uint16 mviPM;
        uint32 codigoSello;      // SL-03-004 → 3004
        uint32 fechaSello;
        uint16 actor;
        int16[5] curvaDecimas;   // temperatura interna a 0, 6, 12, 18 y 24 h (°C × 10)
    }

    struct Desposte {
        uint32[15] pesosG;       // pieza de cada corte; índice 0 = CT-01
        uint16[15] operarios;
        uint32 pesoFrioG;
        uint32 huesoG;
        uint32 grasaG;
        uint32 mermasG;
        uint32 fechaDesposte;
        uint16 actor;
    }

    struct Caja {
        uint16 numero;
        uint8 corte;
        bool mezclaDeLote;       // carne molida: solo se remonta al lote
        uint64 canales;          // bit n encendido = pieza de la canal n
        uint32 pesoG;
        uint32 fechaEmpaqueReal;
        uint16 operario;
        uint16 despacho;
        uint16 minorista;
        uint32 fechaRedistribucion;
    }

    struct Despacho {
        uint16 numero;
        uint16 cliente;
        uint32 salida;
        uint32 llegada;
        int16 tempMaxDecimas;
        uint16 minutosFuera;
        uint16 minutosSinLectura;
        uint16 lecturas;
        bool cumpleDeclarado;
        uint16 despachador;
        bytes32 hashLecturas;    // hash de las lecturas de telemetría del trayecto
        uint16[] cajas;
    }

    struct Venta {
        bytes32 codigoHash;      // keccak256 del código de consulta impreso
        uint16 caja;
        uint16 minorista;
        uint32 fecha;
        uint8 unidades;
    }

    // =====================================================
    // ALMACENAMIENTO
    // =====================================================

    mapping(uint64 => Animal) private animales;
    mapping(uint8 => Canal) private canales;
    mapping(uint8 => Desposte) private despostes;
    mapping(uint16 => Caja) private cajas;
    mapping(uint16 => Despacho) private despachos;
    mapping(bytes32 => Venta) private ventas;

    mapping(uint64 => uint8) public canalDeArete;

    uint64[] private aretes;
    uint16[] private numerosCajas;
    uint16[] private numerosDespachos;

    uint64 public canalesRegistradas;   // bit n = canal n registrada
    uint64 public canalesDespostadas;   // bit n = canal n despostada

    // Piezas ya empacadas por corte (bit n = pieza de la canal n)
    mapping(uint8 => uint64) public piezasEmpacadas;

    // Gramos empacados por corte y peso frío total despostado
    mapping(uint8 => uint256) public empacadoG;
    uint256 public pesoFrioDespostadoG;

    uint256 public totalVentas;

    // =====================================================
    // EVENTOS BLOCKCHAIN
    // =====================================================

    event AnimalRegistrado(uint64 arete, uint16 actor);
    event CanalRegistrada(uint8 canal, uint64 arete, uint16 mvi);
    event DesposteRegistrado(uint8 canal, uint16 actor);
    event CajaRegistrada(uint16 caja, uint8 corte, uint64 canales, uint16 operario);
    event DespachoRegistrado(uint16 despacho, uint16 cliente, uint16 despachador);
    event CajaRedistribuida(uint16 caja, uint16 minorista);
    event VentaRegistrada(bytes32 codigoHash, uint16 caja, uint16 minorista);

    // =====================================================
    // 1. INGRESO DEL ANIMAL
    // =====================================================

    function registrarAnimales(Animal[] calldata lista) public {
        for (uint256 i = 0; i < lista.length; i++) {
            Animal calldata a = lista[i];

            require(a.arete != 0, "ARETE VACIO");
            require(animales[a.arete].arete == 0, "ANIMAL YA REGISTRADO");

            animales[a.arete] = a;

            aretes.push(a.arete);

            emit AnimalRegistrado(a.arete, a.actor);
        }
    }

    // =====================================================
    // 2. FAENAMIENTO Y POST-MORTEM (vínculo arete → canal)
    // =====================================================

    function registrarCanales(Canal[] calldata lista) public {
        for (uint256 i = 0; i < lista.length; i++) {
            Canal calldata c = lista[i];

            require(c.numero > 0 && c.numero < 64, "NUMERO DE CANAL INVALIDO");
            require(canales[c.numero].numero == 0, "CANAL YA REGISTRADA");
            require(animales[c.arete].arete != 0, "ANIMAL NO REGISTRADO");
            require(canalDeArete[c.arete] == 0, "ARETE YA VINCULADO A OTRA CANAL");

            canales[c.numero] = c;

            canalDeArete[c.arete] = c.numero;
            canalesRegistradas |= uint64(1) << c.numero;

            emit CanalRegistrada(c.numero, c.arete, c.mviPM);
        }
    }

    // =====================================================
    // 3. DESPOSTE (canal → 15 piezas) CON BALANCE DE MASA
    // =====================================================

    function registrarDespostes(
        uint8[] calldata numerosCanal,
        Desposte[] calldata lista
    ) public {
        require(numerosCanal.length == lista.length, "LISTAS DE DISTINTO TAMANO");

        for (uint256 i = 0; i < lista.length; i++) {
            uint8 n = numerosCanal[i];
            Desposte calldata d = lista[i];

            require(canales[n].numero != 0, "CANAL NO REGISTRADA");
            require(despostes[n].pesoFrioG == 0, "CANAL YA DESPOSTADA");
            require(d.pesoFrioG > 0, "PESO FRIO VACIO");

            uint256 total = d.huesoG + d.grasaG + d.mermasG;
            for (uint256 k = 0; k < 15; k++) {
                total += d.pesosG[k];
            }

            // La suma de cortes, hueso, grasa y mermas debe cuadrar con
            // el peso de la canal dentro de ±2 %
            require(
                total * 10000 <= uint256(d.pesoFrioG) * (10000 + TOLERANCIA_PB) &&
                total * 10000 >= uint256(d.pesoFrioG) * (10000 - TOLERANCIA_PB),
                "BALANCE DE MASA FUERA DE TOLERANCIA"
            );

            despostes[n] = d;

            canalesDespostadas |= uint64(1) << n;
            pesoFrioDespostadoG += d.pesoFrioG;

            emit DesposteRegistrado(n, d.actor);
        }
    }

    // =====================================================
    // 4. EMPAQUE (piezas → caja) · REGLA FÍSICA
    // No puede salir más producto del que entró.
    // =====================================================

    function registrarCajas(Caja[] calldata lista) public {
        for (uint256 i = 0; i < lista.length; i++) {
            _registrarCaja(lista[i]);
        }
    }

    function _registrarCaja(Caja calldata c) private {
        require(c.numero != 0, "NUMERO DE CAJA INVALIDO");
        require(cajas[c.numero].numero == 0, "CAJA YA REGISTRADA");
        require(c.corte >= 1 && c.corte <= 15, "CORTE INVALIDO");
        require(c.pesoG > 0, "PESO VACIO");

        // Toda caja debe estar respaldada por piezas reales, sin reutilizar
        require(c.canales != 0, "CAJA SIN PIEZAS");
        require(c.canales & ~canalesDespostadas == 0, "PIEZA NO EXISTE");
        require(piezasEmpacadas[c.corte] & c.canales == 0, "PIEZA YA EMPACADA");

        uint256 pesoPiezas = 0;
        for (uint8 n = 1; n < 64; n++) {
            if (c.canales & (uint64(1) << n) != 0) {
                pesoPiezas += despostes[n].pesosG[c.corte - 1];
            }
        }

        require(c.pesoG <= pesoPiezas, "PESO EXCEDE PIEZAS");

        // Tope físico del lote: rendimiento de referencia del corte
        // aplicado al peso frío despostado, con la tolerancia de ±2 %
        (uint256 empacado, uint256 tope) = topeCorte(c.corte);

        require(empacado + c.pesoG <= tope, "EXCEDE RENDIMIENTO DEL LOTE");

        piezasEmpacadas[c.corte] |= c.canales;
        empacadoG[c.corte] += c.pesoG;

        Caja storage nueva = cajas[c.numero];
        nueva.numero = c.numero;
        nueva.corte = c.corte;
        nueva.mezclaDeLote = c.corte == CORTE_MOLIDA;
        nueva.canales = c.canales;
        nueva.pesoG = c.pesoG;
        nueva.fechaEmpaqueReal = c.fechaEmpaqueReal;
        nueva.operario = c.operario;

        numerosCajas.push(c.numero);

        emit CajaRegistrada(c.numero, c.corte, c.canales, c.operario);
    }

    // =====================================================
    // 5. DESPACHO (caja → cliente) CON RESUMEN DE FRÍO
    // Una caja solo puede constar en un despacho.
    // =====================================================

    function registrarDespacho(Despacho calldata d) public {
        require(d.numero != 0, "NUMERO DE DESPACHO INVALIDO");
        require(despachos[d.numero].numero == 0, "DESPACHO YA REGISTRADO");
        require(d.cajas.length > 0, "DESPACHO SIN CAJAS");

        Despacho storage nuevo = despachos[d.numero];
        nuevo.numero = d.numero;
        nuevo.cliente = d.cliente;
        nuevo.salida = d.salida;
        nuevo.llegada = d.llegada;
        nuevo.tempMaxDecimas = d.tempMaxDecimas;
        nuevo.minutosFuera = d.minutosFuera;
        nuevo.minutosSinLectura = d.minutosSinLectura;
        nuevo.lecturas = d.lecturas;
        nuevo.cumpleDeclarado = d.cumpleDeclarado;
        nuevo.hashLecturas = d.hashLecturas;
        nuevo.despachador = d.despachador;

        for (uint256 i = 0; i < d.cajas.length; i++) {
            uint16 numeroCaja = d.cajas[i];

            require(cajas[numeroCaja].numero != 0, "CAJA NO REGISTRADA");
            require(cajas[numeroCaja].despacho == 0, "CAJA YA DESPACHADA");

            cajas[numeroCaja].despacho = d.numero;
            nuevo.cajas.push(numeroCaja);
        }

        numerosDespachos.push(d.numero);

        emit DespachoRegistrado(d.numero, d.cliente, d.despachador);
    }

    // =====================================================
    // 6. REDISTRIBUCIÓN (mayorista → minorista)
    // =====================================================

    function registrarRedistribuciones(
        uint16[] calldata numerosCaja,
        uint16[] calldata minoristas,
        uint32[] calldata fechas
    ) public {
        require(
            numerosCaja.length == minoristas.length &&
            numerosCaja.length == fechas.length,
            "LISTAS DE DISTINTO TAMANO"
        );

        for (uint256 i = 0; i < numerosCaja.length; i++) {
            Caja storage c = cajas[numerosCaja[i]];

            require(c.despacho != 0, "CAJA NO DESPACHADA");
            require(c.minorista == 0, "CAJA YA REDISTRIBUIDA");

            c.minorista = minoristas[i];
            c.fechaRedistribucion = fechas[i];

            emit CajaRedistribuida(numerosCaja[i], minoristas[i]);
        }
    }

    // =====================================================
    // 7. VENTA AL CONSUMIDOR (código de consulta → caja)
    // =====================================================

    function registrarVentas(Venta[] calldata lista) public {
        for (uint256 i = 0; i < lista.length; i++) {
            Venta calldata v = lista[i];

            require(v.codigoHash != bytes32(0), "CODIGO VACIO");
            require(ventas[v.codigoHash].caja == 0, "VENTA YA REGISTRADA");
            require(cajas[v.caja].despacho != 0, "CAJA NO DESPACHADA");

            ventas[v.codigoHash] = v;

            totalVentas++;

            emit VentaRegistrada(v.codigoHash, v.caja, v.minorista);
        }
    }

    // =====================================================
    // CONSULTA HACIA ATRÁS: caja → canales → animales
    // =====================================================

    function trazarCaja(uint16 numeroCaja)
        public
        view
        returns (
            Caja memory caja,
            Despacho memory despacho,
            Canal[] memory canalesOrigen,
            Animal[] memory animalesOrigen,
            uint32[] memory pesosPieza,
            uint16[] memory operariosPieza
        )
    {
        caja = cajas[numeroCaja];
        require(caja.numero != 0, "CAJA NO REGISTRADA");

        despacho = despachos[caja.despacho];

        uint256 cantidad = _contarBits(caja.canales);

        canalesOrigen = new Canal[](cantidad);
        animalesOrigen = new Animal[](cantidad);
        pesosPieza = new uint32[](cantidad);
        operariosPieza = new uint16[](cantidad);

        uint256 j = 0;
        for (uint8 n = 1; n < 64; n++) {
            if (caja.canales & (uint64(1) << n) != 0) {
                canalesOrigen[j] = canales[n];
                animalesOrigen[j] = animales[canales[n].arete];
                pesosPieza[j] = despostes[n].pesosG[caja.corte - 1];
                operariosPieza[j] = despostes[n].operarios[caja.corte - 1];
                j++;
            }
        }
    }

    // =====================================================
    // CONSULTA HACIA ADELANTE: canal → cajas → clientes
    // Devuelve las cajas con pieza de la canal y, aparte,
    // todas las cajas de mezcla de lote (carne molida).
    // =====================================================

    function trazarCanal(uint8 numeroCanal)
        public
        view
        returns (
            Caja[] memory directas,
            uint16[] memory clientesDirectas,
            Caja[] memory mezcla,
            uint16[] memory clientesMezcla
        )
    {
        require(canales[numeroCanal].numero != 0, "CANAL NO REGISTRADA");

        uint64 bit = uint64(1) << numeroCanal;
        bool aportaMezcla = piezasEmpacadas[CORTE_MOLIDA] & bit != 0;

        uint256 nDirectas = 0;
        uint256 nMezcla = 0;

        for (uint256 i = 0; i < numerosCajas.length; i++) {
            Caja storage c = cajas[numerosCajas[i]];
            if (c.mezclaDeLote) {
                if (aportaMezcla) nMezcla++;
            } else if (c.canales & bit != 0) {
                nDirectas++;
            }
        }

        directas = new Caja[](nDirectas);
        clientesDirectas = new uint16[](nDirectas);
        mezcla = new Caja[](nMezcla);
        clientesMezcla = new uint16[](nMezcla);

        uint256 a = 0;
        uint256 b = 0;

        for (uint256 i = 0; i < numerosCajas.length; i++) {
            Caja storage c = cajas[numerosCajas[i]];
            if (c.mezclaDeLote) {
                if (aportaMezcla) {
                    mezcla[b] = c;
                    clientesMezcla[b] = despachos[c.despacho].cliente;
                    b++;
                }
            } else if (c.canales & bit != 0) {
                directas[a] = c;
                clientesDirectas[a] = despachos[c.despacho].cliente;
                a++;
            }
        }
    }

    // =====================================================
    // VERIFICACIÓN DE COMPRA POR EL CONSUMIDOR
    // =====================================================

    function verificarCompra(bytes32 codigoHash)
        public
        view
        returns (Venta memory)
    {
        require(ventas[codigoHash].caja != 0, "CODIGO NO ENCONTRADO");

        return ventas[codigoHash];
    }

    // =====================================================
    // CONSULTAS DE APOYO
    // =====================================================

    // Gramos ya empacados de un corte y el máximo físico que el lote puede rendir
    function topeCorte(uint8 corte)
        public
        view
        returns (uint256 empacado, uint256 tope)
    {
        require(corte >= 1 && corte <= 15, "CORTE INVALIDO");

        empacado = empacadoG[corte];
        tope = pesoFrioDespostadoG * rendimiento[corte]
            * (10000 + TOLERANCIA_PB) / 100000000;
    }

    function obtenerCaja(uint16 numero)
        public
        view
        returns (Caja memory)
    {
        return cajas[numero];
    }

    function obtenerDespacho(uint16 numero)
        public
        view
        returns (Despacho memory)
    {
        require(despachos[numero].numero != 0, "DESPACHO NO REGISTRADO");

        return despachos[numero];
    }

    function obtenerDesposte(uint8 numeroCanal)
        public
        view
        returns (Desposte memory)
    {
        return despostes[numeroCanal];
    }

    function listarAretes() public view returns (uint64[] memory) {
        return aretes;
    }

    function listarCajas() public view returns (uint16[] memory) {
        return numerosCajas;
    }

    function listarDespachos() public view returns (uint16[] memory) {
        return numerosDespachos;
    }

    function totales()
        public
        view
        returns (
            uint256 nAnimales,
            uint256 nCanales,
            uint256 nDespostadas,
            uint256 nCajas,
            uint256 nDespachos,
            uint256 nVentas
        )
    {
        return (
            aretes.length,
            _contarBits(canalesRegistradas),
            _contarBits(canalesDespostadas),
            numerosCajas.length,
            numerosDespachos.length,
            totalVentas
        );
    }

    function _contarBits(uint64 x) private pure returns (uint256 n) {
        while (x != 0) {
            x &= x - 1;
            n++;
        }
    }
}
