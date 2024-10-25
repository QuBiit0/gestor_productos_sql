
# Gestión de Productos con MySQL

Este proyecto permite gestionar productos utilizando **programación orientada a objetos** (POO) y una base de datos **MySQL** para la persistencia de los datos. El sistema permite agregar productos de tipo hardware y software, actualizarlos, eliminarlos y listarlos, todo ello a través de una interfaz de línea de comandos.

## Requisitos

- **Python 3.x**
- **MySQL** instalado y en ejecución
- **Librería** `mysql-connector-python` para la conexión con MySQL

## Instalación

1. **Clona este repositorio**:

   ```bash
   git clone https://github.com/QuBiit0/gestor_productos_mysql.git
   ```

2. **Navega al directorio del proyecto**:

   ```bash
   cd gestor_productos_mysql
   ```

3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configura la base de datos MySQL**:
   
   Puedes usar el script `crear_bd.py` proporcionado para crear la base de datos `gestiondeproductos` y un usuario con permisos:
   
   ```bash
   python crear_bd.py
   ```

   Asegúrate de actualizar las credenciales y parámetros de conexión en el archivo `gestionproductossql.py` según tu configuración de MySQL.

5. **Ejecuta el archivo principal**:

   ```bash
   python main.py
   ```

## Funcionalidades

- **Agregar producto**: Permite agregar un nuevo producto de tipo hardware o software con su ID, nombre, precio, cantidad en stock, y características específicas (garantía para hardware o fecha de expiración para software).
- **Listar productos**: Muestra todos los productos almacenados en la base de datos, junto con sus detalles.
- **Actualizar producto**: Actualiza el nombre, precio, cantidad, garantía (hardware) o fecha de expiración (software) de un producto existente.
- **Eliminar producto**: Elimina un producto de la base de datos según su nombre.
- **Salir**: Cierra la conexión a la base de datos y finaliza la aplicación.

## Notas

- Los productos se almacenan en una base de datos **MySQL** bajo la tabla `productos`.
- Se ha implementado manejo de excepciones para evitar errores comunes en las operaciones con la base de datos y garantizar que los productos tengan valores válidos antes de ser almacenados.
- Asegúrate de que MySQL esté en ejecución antes de usar el sistema.

## Ejemplo de Uso

Al ejecutar el archivo `main.py`, se mostrará un menú con las siguientes opciones:

```
********************************
          --- Sistema de Gestión de Productos ---
          1. Agregar producto
          2. Listar productos
          3. Actualizar producto
          4. Eliminar producto
          5. Salir
********************************
Seleccione una opción:
```

Desde este menú, puedes gestionar los productos interactuando con el sistema de manera fácil y eficiente.
