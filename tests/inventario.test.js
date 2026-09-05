const { validarVentaLibro } = require('../src/inventario');

describe('Pruebas del Módulo de Gestión de Inventario', () => {
  
  // CP-01: Caso crítico - Rechazar venta si no hay stock suficiente
  test('Debe rechazar la venta si la cantidad solicitada supera el stock disponible', () => {
    const resultado = validarVentaLibro('Cien Años de Soledad', 5, 10);
    
    expect(resultado.exito).toBe(false);
    expect(resultado.mensaje).toBe('Stock insuficiente');
  });

  // CP-02: Permitir venta cuando hay stock suficiente
  test('Debe procesar la venta y actualizar el stock si hay suficiente disponibilidad', () => {
    const resultado = validarVentaLibro('Cien Años de Soledad', 10, 3);
    
    expect(resultado.exito).toBe(true);
    expect(resultado.nuevoStock).toBe(7);
  });
});