// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

// =====================================================
// RETIROS SANITARIOS · RETO 04 · NIVEL 2
// Registro público de órdenes de retiro sobre el lote ya
// anclado en CadenaCarnica. No modifica ese contrato: lo lee.
//
// Responde a la consulta del consumidor: ¿esta caja está
// alcanzada por un retiro sanitario? Una caja está alcanzada
// si contiene una pieza de una canal retirada o si es carne
// molida (mezcla de lote) y la mezcla incluye esa canal.
//
// No bloquea ventas: solo registra y responde.
// =====================================================

interface ICadenaCarnica {

    struct Caja {
        uint16 numero;
        uint8 corte;
        bool mezclaDeLote;
        uint64 canales;
        uint32 pesoG;
        uint32 fechaEmpaqueReal;
        uint16 operario;
        uint16 despacho;
        uint16 minorista;
        uint32 fechaRedistribucion;
    }

    function obtenerCaja(uint16 numero) external view returns (Caja memory);

    function piezasEmpacadas(uint8 corte) external view returns (uint64);

    function canalesRegistradas() external view returns (uint64);
}

contract RetirosSanitarios {

    // =====================================================
    // ESTRUCTURA DEL RETIRO
    // =====================================================

    struct Retiro {
        string codigo;            // RS-2026-004
        uint8 canal;              // canal con resultado desfavorable
        uint32 fechaNotificacion; // notificación del laboratorio
        uint32 fechaOrden;        // orden de retiro
        bytes32 hashResultado;    // huella del resultado de laboratorio
    }

    // =====================================================
    // ALMACENAMIENTO
    // =====================================================

    uint8 public constant CORTE_MOLIDA = 15;

    ICadenaCarnica public immutable cadena;

    // Única wallet que puede registrar retiros: la que despliega
    address public immutable autoridad;

    Retiro[] private retiros;

    // bit n encendido = la canal n está bajo retiro
    uint64 public canalesRetiradas;

    // índice del retiro de cada canal, más uno (0 = sin retiro)
    mapping(uint8 => uint256) private retiroDeCanal;

    // =====================================================
    // EVENTOS BLOCKCHAIN
    // =====================================================

    event RetiroRegistrado(string codigo, uint8 canal, uint32 fechaOrden);

    constructor(address direccionCadena) {
        require(direccionCadena != address(0), "DIRECCION DE CADENA VACIA");

        cadena = ICadenaCarnica(direccionCadena);
        autoridad = msg.sender;
    }

    // =====================================================
    // REGISTRAR UNA ORDEN DE RETIRO
    // =====================================================

    function registrarRetiro(
        string calldata codigo,
        uint8 canal,
        uint32 fechaNotificacion,
        uint32 fechaOrden,
        bytes32 hashResultado
    ) public {
        require(msg.sender == autoridad, "SOLO LA AUTORIDAD SANITARIA");
        require(bytes(codigo).length > 0, "CODIGO VACIO");
        require(canal > 0 && canal < 64, "NUMERO DE CANAL INVALIDO");
        require(
            cadena.canalesRegistradas() & (uint64(1) << canal) != 0,
            "CANAL NO REGISTRADA"
        );
        require(retiroDeCanal[canal] == 0, "CANAL YA RETIRADA");

        retiros.push(Retiro({
            codigo: codigo,
            canal: canal,
            fechaNotificacion: fechaNotificacion,
            fechaOrden: fechaOrden,
            hashResultado: hashResultado
        }));

        retiroDeCanal[canal] = retiros.length;
        canalesRetiradas |= uint64(1) << canal;

        emit RetiroRegistrado(codigo, canal, fechaOrden);
    }

    // =====================================================
    // ¿ESTA CAJA ESTÁ BAJO RETIRO?
    // =====================================================

    function cajaBajoRetiro(uint16 numeroCaja)
        public
        view
        returns (bool alcanzada, bool porMezcla, Retiro memory retiro)
    {
        ICadenaCarnica.Caja memory caja = cadena.obtenerCaja(numeroCaja);

        require(caja.numero != 0, "CAJA NO REGISTRADA");

        uint64 afectadas;

        if (caja.mezclaDeLote) {
            // La molida mezcla las canales del lote: basta con que una
            // canal retirada haya aportado a la mezcla
            afectadas = cadena.piezasEmpacadas(CORTE_MOLIDA) & canalesRetiradas;
            porMezcla = afectadas != 0;
        } else {
            afectadas = caja.canales & canalesRetiradas;
        }

        if (afectadas == 0) {
            return (false, false, retiro);
        }

        for (uint8 n = 1; n < 64; n++) {
            if (afectadas & (uint64(1) << n) != 0) {
                return (true, porMezcla, retiros[retiroDeCanal[n] - 1]);
            }
        }
    }

    // =====================================================
    // CONSULTAS DE APOYO
    // =====================================================

    function listarRetiros() public view returns (Retiro[] memory) {
        return retiros;
    }

    function totalRetiros() public view returns (uint256) {
        return retiros.length;
    }
}
