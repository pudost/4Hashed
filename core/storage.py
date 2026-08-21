#para cosas como:¿Existe database/database.db? 
# ¿Dónde está la carpeta database? 
# Crear la carpeta projects/Construir una ruta hacia un archivo


from pathlib import Path
import os
import sqlite3

class Storage:



    def ensure_database_exists(self):
    current_dir = Path(__file__).parent
    
    database_dir = current_dir / "database"
    if not database_dir.exists():
        database_dir.mkdir()
        print ("Carpeta 'database' creada exitosamente.")


    def ensure_users_table_exists(self):
        conexion = sqlite3.connect("database/data_base.db")
        try:
        cursor = conexion.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
        fila = cursor.fetchone()
        if fila is None:
            conexion.execute('''CREATE TABLE users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL
                            );''')
            print("Tabla 'users' creada exitosamente.")
        else:
            print("La tabla 'users' ya existe.")
        except sqlite3.Error as e:
        print(f"Error al verificar o crear la tabla 'users': {e}")
        finally:
        conexion.close()

def initialize_database(self):
    self.ensure_database_exists()
    self.ensure_users_table_exists()


conexion = sqlite3.connect("database/data_base.db")
try:
    cursor = conexion.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='users';")
    fila = cursor.fetchone()
    if fila is None:
        conexion.execute('''CREATE TABLE users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT NOT NULL UNIQUE,
                            password TEXT NOT NULL
                        );''')
        print("Tabla 'users' creada exitosamente.")
    else:
        print("La tabla 'users' ya existe.")
except sqlite3.Error as e:
    print(f"Error al verificar o crear la tabla 'users': {e}")
finally:
    conexion.close()
    
