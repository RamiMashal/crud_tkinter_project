'''
PRIMERO CREARÉ LA INTERFAZ Y CREO QUE DEBERÍA LLEVAR LAS FUNCIONES A OTRO SCRIPT E IMPORTARLO, Y OTRO PARA LA APP?
'''

import tkinter as tk
from tkinter import*
from tkinter import messagebox

raiz = Tk()
raiz.title("CRUD App")
raiz.resizable(1,1) # PERMITIMOS MANIPULAR EL TAMAÑO DE LA VENTANA
raiz.geometry("400x400")

miFrame = Frame(raiz)
miFrame.pack()

# ----------------------------- FUNCIONES PARA VENTANAS EMERGENTES, MENÚ Y BOTONES ----------------------------------

'''
Para la función de "Borrar Campos" voy a guardar la información de los mismos (ID, Nombre...) en variables StringVar que
vincularé a cada uno de los cuadros. De esta forma, puedo manipular la información de los campos usando las variables.

Así mismo, vincularé la función borrarCampos() al menú "Borrar Campos" --> menuBorrar.add_command(label = "Borrar campos", command = borrarCampos)

ATENCIÓN !! AL FINAL NO USÉ LAS VARIABLES STRINGVAR PARA LA FUNCION borrarCampos(), SINO QUE USÉ ESTA FÓRMULA PARA MODIFICAR
DIRECTAMENTE LOS CUADROS DE TEXTO --> cuadroID.delete(0, tk.END) --> PARA USAR ESE tk HE TENIDO QUE IMPORTAR tkinter as tk

DE TODAS FORMAS, MANTENGO CREADAS Y VINCULADAS A LOS CUADROS LAS VARIABLES STRINGVAR POR SI FUERA DE UTILIDAD MÁS ADELANTE
'''

borrarID = StringVar()
borrarNombre = StringVar()
borrarPass = StringVar()
borrarApellido = StringVar()
borrarDireccion = StringVar()
borrarComentarios = StringVar()

def borrarCampos():
    cuadroID.delete(0, tk.END) # LE DIGO QUE BORRE EL CONTENIDO DEL CUADRO ID DESDE EL ÍNDICE 0 HASTA EL FINAL
    cuadroNombre.delete(0, tk.END)
    cuadroPass.delete(0, tk.END)
    cuadroApellido.delete(0, tk.END)
    cuadroDireccion.delete(0, tk.END)
    cuadroComentarios.delete("1.0", tk.END) # PARA CUADROS DE TIPO TEXT USAMOS "1.0" EN LUGAR DE 0 COMO PRIMER ÍNDICE

def menuBBDDSalir():
    valor = messagebox.askquestion("Salir", "¿Desea salir de la aplicación?")
    if valor == "yes":
        raiz.destroy()

def menuAyudaLicencia():
    messagebox.showinfo("Licencia", "Este producto no tiene licencia.")
def menuAyudaAcerca():
    messagebox.showinfo("Acerca de...", "Esta aplicación ha sido desarrollada para aprender a programar en Python.")

# CONTINUAR POR ESTE PASO Y LUEGO TE METES CON LAS FUNCIONES PARA LA BASE DE DATOS


# ----------------------------- BARRA MENÚ Y VENTANAS EMERGENTES -------------------------------------------------

barraMenu = Menu(raiz)
raiz.config(menu = barraMenu)

menuBBDD = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "BBDD", menu = menuBBDD)
menuBBDD.add_command(label = "Conectar")
menuBBDD.add_separator()
menuBBDD.add_command(label = "Salir", command = menuBBDDSalir)

menuBorrar = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Borrar", menu = menuBorrar)
menuBorrar.add_command(label = "Borrar campos", command = borrarCampos)

menuCRUD = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "CRUD", menu = menuCRUD)
menuCRUD.add_command(label = "Crear")
menuCRUD.add_separator()
menuCRUD.add_command(label = "Leer")
menuCRUD.add_separator()
menuCRUD.add_command(label = "Actualizar")
menuCRUD.add_separator()
menuCRUD.add_command(label = "Eliminar")

menuAyuda = Menu(barraMenu, tearoff = 0)
barraMenu.add_cascade(label = "Ayuda", menu = menuAyuda)
menuAyuda.add_command(label = "Licencia", command = menuAyudaLicencia)
menuAyuda.add_separator()
menuAyuda.add_command(label = "Acerca de...", command = menuAyudaAcerca)


# ----------------------------- CUADROS DE TEXTO Y SUS ETIQUETAS ---------------------------


labelID = Label(miFrame, text = "ID:", padx = 10, pady = 10)
labelID.grid(row = 0, column = 0, sticky="e")

cuadroID = Entry(miFrame, textvariable = borrarID)
cuadroID.grid(row= 0, column = 1, padx = 10, pady = 10)

labelNombre = Label(miFrame, text = "Nombre:", padx = 10, pady = 10)
labelNombre.grid(row = 1, column = 0, sticky="e")

cuadroNombre = Entry(miFrame, textvariable = borrarNombre)
cuadroNombre.grid(row = 1, column = 1, padx = 10, pady = 10)

labelPass = Label(miFrame, text = "Password:", padx = 10, pady = 10)
labelPass.grid(row = 2, column = 0, sticky="e")

cuadroPass = Entry(miFrame, textvariable = borrarPass)
cuadroPass.grid(row = 2, column = 1, padx = 10, pady = 10)
cuadroPass.config(show = "*")

labelApellido = Label(miFrame, text = "Apellido:", padx = 10, pady = 10)
labelApellido.grid(row = 3, column = 0, sticky="e")

cuadroApellido = Entry(miFrame, textvariable = borrarApellido)
cuadroApellido.grid(row = 3, column = 1, padx = 10, pady = 10)

labelDireccion = Label(miFrame, text = "Dirección:", padx = 10, pady = 10)
labelDireccion.grid(row = 4, column = 0, sticky="e")

cuadroDireccion = Entry(miFrame, textvariable = borrarDireccion)
cuadroDireccion.grid(row = 4, column = 1, padx = 10, pady = 10)

labelComentarios = Label(miFrame, text = "Comentarios:", padx = 10, pady = 10)
labelComentarios.grid(row = 5, column = 0, sticky="e")

cuadroComentarios = Text(miFrame, width = 15, height = 5) # RECUERDA --> ESTO ES UN TIPO TEXT, NO ENTRY
cuadroComentarios.grid(row = 5, column = 1, padx = 10, pady = 10)

# ----------------------------- BARRA COMENTARIOS -------------------------------------------------------------

barraComentarios = Scrollbar(miFrame, command = cuadroComentarios.yview)
barraComentarios.grid(row = 5, column = 2, sticky = "nsew") # sticky = "nsew" --> PARA ADAPTAR LA BARRA AL LARGO DEL CUADRO COMENTARIOS
cuadroComentarios.config(yscrollcommand = barraComentarios.set)

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

frameBotones = Frame(raiz) # FRAME INDEPENDIENTE PARA CONTENER LOS BOTONES
frameBotones.pack(side = BOTTOM) # LO UBICAMOS EN LA PARTE DE ABAJO

botonCreate = Button(frameBotones, text = "Create")
botonCreate.pack(side = LEFT, padx = 10, pady = 10)

botonRead = Button(frameBotones, text = "Read")
botonRead.pack(side = LEFT, padx = 10, pady = 10)

botonUpdate = Button(frameBotones, text = "Update")
botonUpdate.pack(side = LEFT, padx = 10, pady = 10)

botonDelete = Button(frameBotones, text = "Delete")
botonDelete.pack(side = LEFT, padx = 10, pady = 10)


raiz.mainloop()
