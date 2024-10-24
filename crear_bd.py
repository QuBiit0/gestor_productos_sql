import mysql.connector
from mysql.connector import errorcode

def crear_base_de_datos_y_usuario():
    try:
        # Conectar a MySQL con un usuario administrador, por ejemplo 'root'
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",  # Cambia esto por tu usuario administrador
            password="nosedice"  # Cambia esto por la contraseña de root
        )
        cursor = conexion.cursor()

        # Crear la base de datos si no existe
        cursor.execute("CREATE DATABASE IF NOT EXISTS gestiondeproductos")
        print("Base de datos 'gestiondeproductos' creada o ya existe.")

        # Crear un nuevo usuario con permisos
        cursor.execute("""
        CREATE USER IF NOT EXISTS 'nombre_usuario'@'localhost' IDENTIFIED BY 'contraseña_usuario';
        GRANT ALL PRIVILEGES ON gestiondeproductos.* TO 'nombre_usuario'@'localhost';
        FLUSH PRIVILEGES;
        """)
        print("Usuario 'nombre_usuario' creado o ya existe, y permisos asignados.")

        # Cerrar la conexión
        cursor.close()
        conexion.close()
        print("Conexión a MySQL cerrada.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Error: Nombre de usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Error: La base de datos no existe.")
        else:
            print(err)
    except Exception as e:
        print(f"Se ha producido un error: {e}")

if __name__ == "__main__":
    crear_base_de_datos_y_usuario()
