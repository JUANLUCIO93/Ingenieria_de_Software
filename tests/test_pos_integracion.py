import pytest

# Simulación de la lógica de negocio y BD para el módulo POS e Inventario
class Libro:
    def __init__(self, isbn, titulo, precio, stock):
        self.isbn = isbn
        self.titulo = titulo
        self.precio = precio
        self.stock = stock

    def descontar_stock(self, cantidad):
        if cantidad > self.stock:
            raise ValueError("Stock insuficiente")
        self.stock -= cantidad
        return self.stock


class ServicioVenta:
    def __init__(self):
        self.ventas_registradas = []

    def registrar_venta(self, libro, cantidad_vendida):
        # CP-04: Prueba de integración entre cobro y actualización de inventario
        nuevo_stock = libro.descontar_stock(cantidad_vendida)
        
        venta = {
            "id_venta": len(self.ventas_registradas) + 1,
            "isbn": libro.isbn,
            "cantidad": cantidad_vendida,
            "total": libro.precio * cantidad_vendida
        }
        self.ventas_registradas.append(venta)
        return venta, nuevo_stock


# --- PRUEBAS AUTOMATIZADAS (CP-04) ---

def test_cp04_registro_venta_e_integracion_stock_exitoso():
    """CP-04: Verifica que al procesar una venta se descuente el stock y se guarde en BD."""
    # Precondición
    libro = Libro("978-0132350884", "Clean Code", 45.00, stock=10)
    servicio = ServicioVenta()

    # Ejecución
    venta, nuevo_stock = servicio.registrar_venta(libro, cantidad_vendida=2)

    # Validaciones (Asserts)
    assert nuevo_stock == 8, "El stock no se actualizó correctamente en la BD"
    assert len(servicio.ventas_registradas) == 1, "La venta no fue registrada"
    assert venta["total"] == 90.00, "El total de la venta es incorrecto"


def test_cp04_registro_venta_fallido_por_stock_insuficiente():
    """Prueba de frontera: Lanza excepción si la cantidad excede el stock."""
    libro = Libro("978-0132350884", "Clean Code", 45.00, stock=1)
    servicio = ServicioVenta()

    with pytest.raises(ValueError, match="Stock insuficiente"):
        servicio.registrar_venta(libro, cantidad_vendida=3)