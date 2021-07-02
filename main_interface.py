import tkinter as tk
import funciones_crud as fcrud
from tkinter import *
from tkinter import messagebox

raiz = Tk();
raiz.title("CRUD APP");
# PERMITIMOS MANIPULAR EL TAMAÑO DE LA VENTANA
raiz.resizable(1,1);
raiz.geometry("400x400");

miFrame = Frame(raiz);
miFrame.pack();

nombre = StringVar();
passw = StringVar();
apellidos = StringVar();
direccion = StringVar();
comentarios = StringVar();

'''
CREO Y VINCULO LAS VARIABLES STRINGVAR A LOS CUADROS DE TEXTO.
De esta forma, puedo manipular la información de los campos usando las variables.
'''
# ----------------------------- FUNCIONES PARA VENTANAS EMERGENTES, MENÚ Y BOTONES ----------------------------------

def validacion_campos_vacios():
    if len(cuadroNombre.get()) == 0 or len(cuadroPass.get()) == 0 or len(cuadroApellido.get()) == 0 or len(cuadroDireccion.get()) == 0:
        return False;
    return True;

def validacion_id_vacio():
    if len(cuadroID.get()) == 0:
        return False;
    return True;

def borrarCampos():
    cuadroID.delete(0, tk.END);
    # LE DIGO QUE BORRE EL CONTENIDO DEL CUADRO ID DESDE EL ÍNDICE 0 HASTA EL FINAL
    cuadroNombre.delete(0, tk.END);
    cuadroPass.delete(0, tk.END);
    cuadroApellido.delete(0, tk.END);
    cuadroDireccion.delete(0, tk.END);
    cuadroComentarios.delete("1.0", tk.END);
    # PARA CUADROS DE TIPO TEXT USAMOS "1.0" EN LUGAR DE 0 COMO PRIMER ÍNDICE

def menuBBDDSalir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?");
    if valor == "yes":
        raiz.destroy();

def menuAyudaLicencia():
    messagebox.showinfo("Licencia", "Este producto no tiene licencia.");
def menuAyudaAcerca():
    messagebox.showinfo("Acerca de...", "Esta aplicación ha sido desarrollada para aprender a programar en Python.");

def crear_registro():

    if validacion_campos_vacios() == True:

        fcrud.log_app("Creando registro");
        
        campos = (cuadroNombre.get(), cuadroPass.get(), cuadroApellido.get(), cuadroDireccion.get(), cuadroComentarios.get('1.0', tk.END));
        query = "INSERT INTO CRUD VALUES(NULL,?,?,?,?,?)";

        try:
            fcrud.ejecutar_slq(query, campos);

            fcrud.log_app("Registro creado con éxito");
            return (messagebox.showinfo("Creación registro", "Registro creado con éxito"));
        
        except:
            fcrud.log_app("Error al crear registro. Es posible que ya exista un registro con la misma contraseña");
            return (messagebox.showwarning("Creación registro", "Error al crear registro. Es posible que ya exista un registro con la misma contraseña"));
    else:
        fcrud.log_app("Los campos Nombre, Password, Apellidos y Dirección son obligatorios");
        return (messagebox.showwarning("Campos vacíos", "Error al crear registro. Es posible que haya campos obligatorios vacíos"));

def leer_registro():
    if validacion_id_vacio() == True:
        fcrud.log_app("Mostrando registro");
        
        campos = (cuadroID.get());
        query = "SELECT * FROM CRUD WHERE ID = (?)";

        try:
            id_buscar = fcrud.ejecutar_slq(query, campos).fetchone();
            nombre.set(id_buscar[1]);
            passw.set(id_buscar[2]);
            apellidos.set(id_buscar[3]);
            direccion.set(id_buscar[4]);
            cuadroComentarios.insert("1.0", id_buscar[5]);
 
            fcrud.log_app("Registro mostrado con éxito");
        
        except:
            fcrud.log_app("Error al mostrar registro.");
            return (messagebox.showwarning("Mostrar registro", "Error al mostrar registro."));
    else:
        fcrud.log_app("Sin el campo ID no puedo buscar");
        return (messagebox.showwarning("Campos vacíos", "Error al leer registro. Es posible que el campo ID esté vacío"));

def actualizar_registro():
    if validacion_id_vacio() == True:
        fcrud.log_app("Actualizando registro");
        
        campos = (cuadroNombre.get(), cuadroPass.get(), cuadroApellido.get(), cuadroDireccion.get(), cuadroComentarios.get('1.0', tk.END), cuadroID.get());
        query = "UPDATE CRUD SET NOMBRE = (?), PASSWORD = (?), APELLIDOS = (?), DIRECCIÓN = (?), COMENTARIOS = (?) WHERE ID = (?)";

        try:
            fcrud.ejecutar_slq(query, campos);

            fcrud.log_app("Registro actualizado con éxito");
            return (messagebox.showinfo("Actualizar registro", "Registro actualizado con éxito"));
        
        except:
            fcrud.log_app("Error al actualizar registro.");
            return (messagebox.showwarning("Actualizar registro", "Error al actualizar registro."));

    else:
        fcrud.log_app("Sin el campo ID no puedo buscar");
        return (messagebox.showwarning("Campos vacíos", "Error al actualizar registro. Es posible que el campo ID esté vacío"));

def borrar_registro():
    if validacion_id_vacio() == True:
        fcrud.log_app("Eliminando registro");
        
        campos = (cuadroID.get());
        query = "DELETE FROM CRUD WHERE ID = (?)";

        try:
            fcrud.ejecutar_slq(query, campos);

            fcrud.log_app("Registro eliminado con éxito");
            return (messagebox.showinfo("Eliminar registro", "Registro eliminado con éxito"));
        
        except:
            fcrud.log_app("Error al eliminar registro.");
            return (messagebox.showwarning("Eliminar registro", "Error al eliminar registro."));

    else:
        fcrud.log_app("Sin el campo ID no puedo buscar");
        return (messagebox.showwarning("Campos vacíos", "Error al eliminar registro. Es posible que el campo ID esté vacío"));

# ----------------------------- BARRA MENÚ Y VENTANAS EMERGENTES -------------------------------------------------

barraMenu = Menu(raiz);
raiz.config(menu = barraMenu);

menuBBDD = Menu(barraMenu, tearoff = 0);
barraMenu.add_cascade(label = "BBDD", menu = menuBBDD);
menuBBDD.add_command(label = "Conectar", command = fcrud.crear_bbdd);
menuBBDD.add_separator();
menuBBDD.add_command(label = "Salir", command = menuBBDDSalir);

menuBorrar = Menu(barraMenu, tearoff = 0);
barraMenu.add_cascade(label = "Borrar", menu = menuBorrar);
menuBorrar.add_command(label = "Borrar campos", command = borrarCampos);

menuCRUD = Menu(barraMenu, tearoff = 0);
barraMenu.add_cascade(label = "CRUD", menu = menuCRUD);
menuCRUD.add_command(label = "Crear", command = crear_registro);
menuCRUD.add_separator();
menuCRUD.add_command(label = "Leer", command=leer_registro);
menuCRUD.add_separator();
menuCRUD.add_command(label = "Actualizar", command=actualizar_registro);
menuCRUD.add_separator();
menuCRUD.add_command(label = "Eliminar", command=borrar_registro);

menuAyuda = Menu(barraMenu, tearoff = 0);
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda);
menuAyuda.add_command(label = "Licencia", command = menuAyudaLicencia);
menuAyuda.add_separator();
menuAyuda.add_command(label = "Acerca de...", command = menuAyudaAcerca);


# ----------------------------- CUADROS DE TEXTO Y SUS ETIQUETAS ---------------------------


labelID = Label(miFrame, text = "ID:", padx = 10, pady = 10);
labelID.grid(row = 0, column = 0, sticky="e");

cuadroID = Entry(miFrame);
cuadroID.grid(row= 0, column = 1, padx = 10, pady = 10);

labelNombre = Label(miFrame, text = "Nombre:", padx = 10, pady = 10);
labelNombre.grid(row = 1, column = 0, sticky="e");

cuadroNombre = Entry(miFrame, textvariable = nombre);
cuadroNombre.focus();
# Con focus el cursor de escritura se coloca automáticamente en el campo nombre
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10);

labelPass = Label(miFrame, text = "Password:", padx = 10, pady = 10);
labelPass.grid(row = 2, column = 0, sticky="e");

cuadroPass = Entry(miFrame, textvariable = passw);
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10);
cuadroPass.config(show = "*");

labelApellido = Label(miFrame, text = "Apellidos:", padx = 10, pady = 10);
labelApellido.grid(row = 3, column = 0, sticky="e");

cuadroApellido = Entry(miFrame, textvariable = apellidos);
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10);

labelDireccion = Label(miFrame, text = "Dirección:", padx = 10, pady = 10);
labelDireccion.grid(row = 4, column = 0, sticky="e");

cuadroDireccion = Entry(miFrame, textvariable = direccion);
cuadroDireccion.grid(row = 4, column = 1, padx = 10, pady = 10);

labelComentarios = Label(miFrame, text = "Comentarios:", padx = 10, pady = 10);
labelComentarios.grid(row = 5, column = 0, sticky="e");

cuadroComentarios = Text(miFrame, width = 15, height = 5);
# RECUERDA --> ESTO ES UN TIPO TEXT, NO ENTRY
cuadroComentarios.grid(row = 5, column = 1, padx = 10, pady = 10);

# ----------------------------- BARRA COMENTARIOS -------------------------------------------------------------

barraComentarios = Scrollbar(miFrame, command = cuadroComentarios.yview);
barraComentarios.grid(row = 5, column = 2, sticky = "nsew");
# sticky = "nsew" --> PARA ADAPTAR LA BARRA AL LARGO DEL CUADRO COMENTARIOS
cuadroComentarios.config(yscrollcommand = barraComentarios.set);

# ----------------------------- BOTONES -------------------------------------------------------------

'''
ESTE CÓDIGO LO HE SACADO DE AQUÍ https://www.tutorialspoint.com/python/tk_pack.htm, YA QUE MI IDEA ORIGINAL, ASIGNANDO
LA POSICIÓN DE LOS BOTONES PARA QUE COINCIDA CON LAS ROWS Y COLUMNS DE LOS CUADROS DE TEXTO Y LABEL, NO ERA MUY BONITO 

botonCreate = Button(miFrame, text = "Create")
botonCreate.grid(row = 6, column = 0)

botonRead = Button(miFrame, text = "Read")
botonRead.grid(row = 6, column = 1)

botonUpdate = Button(miFrame, text = "Update")
botonUpdate.grid(row = 6, column = 2)

botonDelete = Button(miFrame, text = "Delete")
botonDelete.grid(row = 6, column = 3)

DE ESTA FORMA ESTABLEZCO UN FRAME INDEPENDIENTE PARA LOS BOTONES Y LO COLOCO DEBAJO DEL FRAME QUE CONTIENE LOS LABEL Y CUADROS (miFrame)
'''

frameBotones = Frame(raiz);
# FRAME INDEPENDIENTE PARA CONTENER LOS BOTONES
frameBotones.pack(side = BOTTOM);
# LO UBICAMOS EN LA PARTE DE ABAJO

botonCreate = Button(frameBotones, text = "Create", command = crear_registro);
botonCreate.pack(side = LEFT, padx = 10, pady = 10);

botonRead = Button(frameBotones, text = "Read", command=leer_registro);
botonRead.pack(side = LEFT, padx = 10, pady = 10);

botonUpdate = Button(frameBotones, text = "Update", command=actualizar_registro);
botonUpdate.pack(side = LEFT, padx = 10, pady = 10);

botonDelete = Button(frameBotones, text = "Delete", command=borrar_registro);
botonDelete.pack(side = LEFT, padx = 10, pady = 10);

raiz.mainloop();