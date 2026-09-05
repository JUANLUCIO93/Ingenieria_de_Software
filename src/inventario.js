function validarVentaLibro(titulo, cantidadDisponible, cantidadSolicitada) {
  if (cantidadSolicitada <= 0) {
    return { exito: false, mensaje: "La cantidad solicitada debe ser mayor a cero" };
  }
  
  if (cantidadSolicitada > cantidadDisponible) {
    return { exito: false, mensaje: "Stock insuficiente" };
  }

  return { 
    exito: true, 
    nuevoStock: cantidadDisponible - cantidadSolicitada,
    mensaje: "Venta realizada con éxito" 
  };
}

module.exports = { validarVentaLibro };