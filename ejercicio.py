import sys


class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = margen_de_venta
        self.precio_de_venta = None

    def registrar(self):
        if not isinstance(self.margen_de_venta, float):
         raise ValueError("El margen de venta debe ser un número decimal")

        if self.margen_de_venta > 1:
            raise ValueError("El margen de venta no puede ser superior al 100%")

        self.precio_de_venta = self.costo / (1 - self.margen_de_venta)
        productos[self.id] = self

    def listar(self):
        for id, producto in productos.items():
            print(f"ID: {id} - Nombre: {producto.nombre} - Precio de venta: {producto.precio_de_venta}")


productos = {}


def main():
    id = int(input("Ingrese el ID del producto: "))
    nombre = input("Ingrese el nombre del producto: ")
    descripcion = input("Ingrese la descripción del producto: ")
    costo = float(input("Ingrese el costo del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))
    margen_de_venta = float(input("Ingrese el margen de venta: "))

    try:
        producto = Producto(id, nombre, descripcion, costo, cantidad, margen_de_venta)
        producto.registrar()

        print("Producto registrado")

        producto.listar()
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()