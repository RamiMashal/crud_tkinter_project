import time
import sqlite3
from tkinter import messagebox

def log_app(mensaje):
    mensaje_control = f"{time.strftime('%d/%m/%Y %H:%M:%S')} - {mensaje}\n";
    with open("log_app.txt", "a", encoding="utf-8") as log_app:
        log_app.write(mensaje_control);

# ----------------------------- FUNCIONES EJECUTAR QUERY / CREAR BBDD ----------------------------------

def ejecutar_slq(query, parametros = ()):
    log_app("Ejecutando query");

    with sqlite3.connect("crud_db") as conexion_bbdd:
        cursor = conexion_bbdd.cursor();
        ejecutar = cursor.execute(query, parametros);
        conexion_bbdd.commit();
    return ejecutar;

def crear_bbdd():
    log_app("Creando BBDD");

    query = '''
            CREATE TABLE CRUD (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR (20),
            PASSWORD VARCHAR (20) UNIQUE,
            APELLIDOS VARCHAR (20),
            DIRECCIÓN VARCHAR (50),
            COMENTARIOS VARCHAR (100))
            ''';

    try:
        ejecutar_slq(query);

        log_app("BBDD creada con éxito");
        return(messagebox.showinfo("Creación BBDD", "BBDD creada con éxito"));

    except:
        log_app("Error al crear BBDD, es posible que exista una BBDD con el mismo nombre");
        return (messagebox.showwarning("Creación BBDD", "Error al crear BBDD, es posible que exista una BBDD con el mismo nombre"));