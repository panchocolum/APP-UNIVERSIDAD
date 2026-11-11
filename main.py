import sqlite3

from alumno import Alumno
from curso import Curso
from matricula import Matricula

# --------------------------------
# CONECTAR CON LA BASE DE DATOS
# --------------------------------

conexion = sqlite3.connect("inacap.db")

print("Conexion realizada correctamente")

# --------------------------------------
# CREAR CURSOR
# --------------------------------------

cursor = conexion.cursor()

print("Cursor creado correctamente")


# ========================================
#     CREAR TABLA ALUMNO
# ========================================

cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS alumno (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL, 
        email TEXT NOT NULL,
        edad INTEGER
    )
        
    """
)

print("Tabla: 'alumno' creada correctamente")

#""""""""""""""""""""""""""""""
#         crear tabla alumno
#"""""""""""""""""""""""""""""""""""""

cursor.execute("""
    CREATE TABLE IF NOT EXIST CURSOR()
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    hora INTEGER
    
               """)

print("Tabla: 'curso' creada correctamente")


#=======================================
#        CREAR TABLA MATRICULA
#=======================================

cursor.execute

      CREATE TABLE IF NOT EXISTS matricula(
          id INTEGER PRIMARY KEY AUTOINCREMENT,
          alumno_id INTEGER NOT NULL,
          curso_id INTEGER NOT NULL,
          fecha TEXT NOT NULL,
          
          FOREIGN KEY(alumno_id)
          FOREIGH KEY(alumno(id))
               REFERENCE curso(id)
        )           