
class Producto:
    
    def __init__(self,Nombre:str,Precio:float,Cantidad:int):
        self.Nombre = Nombre
        self.Precio = Precio
        self.Cantidad = Cantidad

class Inventario:
    def __init__(self):
        self.items = [] # Lista interna

    def agregar_productos(self):
        Nombre = input("Nombre del producto: ")
        Precio = float(input("Precio del producto: "))
        Cantidad = int(input("Cantidad en stock del producto: "))
        print("\nProducto agregado:",Nombre,"\n")
        producto = Producto(Nombre,Precio,Cantidad) # aquí creamos el producto(objeto) con sus características(atributos)
        self.items.append(producto) # aquí estamos creando una lista de objetos de los productos


    def mostrar_productos(self):
        if not self.items:
            print("No hay productos registrados.\n")
        else:
            print("Listado: \n")
            for producto in self.items:
                print(f"Producto: {producto.Nombre} - ${producto.Precio} - {producto.Cantidad} pieza(s)")
            print("\n")

    def buscar_productos(self):
        producto_buscar = str(input("¿Qué producto te gustaría buscar? ")) #Aquí ponemos el nombre del producto que queremos
        for producto in self.items: #aquí iteramos por la cantidad de productos que hay en nuestra lista
            if hasattr(producto, "Nombre"): #con esta sentencia nos aseguramos que el atributo o característica que buscamos exista
                if getattr(producto, "Nombre") == producto_buscar: # aquí obtenemos el atributo deseado comparandolo con el producto que buscamos
                    print(f"Producto encontrado con Nombre = {producto_buscar}, precio {producto.Precio} y cantidad {producto.Cantidad} pieza(s)\n")
                    # Aquí puedes realizar la acción deseada con el objeto encontrado
                    break  # Salir del bucle si solo necesitas el primer objeto
            
            
    def valor_total_inventario(self):
        contador = 0
        for producto in self.items:
            precio_total = producto.Precio*producto.Cantidad
            contador += precio_total
        print(f"Valor total del inventario: ${round(contador,2)}\n")

    def salir(self):
        exit()


def main():
    MiInventario = Inventario()

    while True:
        print("=== Menú ===")
        print("1. Agregar productos")
        print("2. Mostrar productos")
        print("3. Buscar producto")
        print("4. Valor total del inventario")
        print("5. Salir\n")

        opcion = input("Selecciona una opción: ")
        print("\n")

        match opcion:
            
            case "1":    
                MiInventario.agregar_productos()
            case "2":
                MiInventario.mostrar_productos()
            case "3":
                MiInventario.buscar_productos()
            case "4":
                MiInventario.valor_total_inventario()
            case "5":
                MiInventario.salir()
            case _:
                print("Opción no válida.\n")


if __name__ == "__main__":
    main()