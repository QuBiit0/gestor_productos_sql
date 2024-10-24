from gestionproductossql import Inventario, limpiar_pantalla, mostrar_menu, obtener_opcion

def main():
    inventario = Inventario(
        host="localhost",  # Cambiar por la dirección de tu servidor MySQL
        user="root",       # Cambiar por tu usuario MySQL
        password="nosedice",  # Cambiar por tu contraseña MySQL
        database="gestiondeproductos",  # Cambiar por tu base de datos
        port=3306  # Cambia por el puerto de tu base de datos
    )

    while True:
        limpiar_pantalla()
        mostrar_menu()
        opcion = obtener_opcion()

        if opcion == 1:
            inventario.agregar_producto_interactivo()
        elif opcion == 2:
            inventario.listar_productos()
        elif opcion == 3:
            inventario.actualizar_producto_interactivo()
        elif opcion == 4:
            inventario.eliminar_producto_interactivo()
        elif opcion == 5:
            inventario.cerrar_conexion()
            break

        input("\nPresione enter para continuar...")

if __name__ == "__main__":
    main()
