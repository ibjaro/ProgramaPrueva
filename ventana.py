# creacion de una ventana para los datos, con tkinter

# impotamos tkinter para crear la ventana
import tkinter

# tambien podemos crear una variable para cada dato, y luego llamarla en la funcion agregar_datos
# nombre = tkinter.StringVar()
# nombre.get()
# en el entry se debe agregar la variable creada, y en la funcion agregar_datos se debe llamar la variable creada
# textvariable=nombre, esto se le agrega como otro parametro al entry
# si queremos imprimir en el label, se debe agregar la variable creada
# label_nombre.config(text="Se imprime "+nombre.get()+" en el label")

# importamos la clase Agenda  
from agenda import Agenda
# creamos un objeto de la clase Agenda
agenda = Agenda()

#funcion para agregar datos
def agregar_datos():
    nombre = entry_nombre.get()
    apellido = entry_apellido.get()
    telefono = entry_telefono.get()
    correo = entry_correo.get()
    direccion = entry_direccion.get()
    agenda.principal(1, nombre, apellido, telefono, correo, direccion)
    entry_nombre.delete(0, tkinter.END)
    entry_apellido.delete(0, tkinter.END)
    entry_telefono.delete(0, tkinter.END)
    entry_correo.delete(0, tkinter.END)
    entry_direccion.delete(0, tkinter.END)
    #print(nombre, apellido, telefono, correo, direccion)

#funcion para eliminar datos
def eliminar_datos():
    nombre = entry_nombre.get()
    agenda.principal(2, nombre)
    entry_nombre.delete(0, tkinter.END)

#funcion para mostrar datos
def mostrar_datos():
    agenda.principal(3)

#funcion para salir
def salir():
    agenda.principal(4)

# creacion de la ventana
ventana = tkinter.Tk()
# titulo de la ventana
ventana.title("Agenda")
# label y entry para cada dato
label_nombre = tkinter.Label(ventana, text="Ingrese su Nombre: ", font=("Arial", 15),padx=10, pady=10).pack()
entry_nombre = tkinter.Entry(ventana, font=("Arial", 15), width=15)
entry_nombre.pack()

label_apellido = tkinter.Label(ventana, text="Ingrese su Apellido: ", font=("Arial", 15),padx=10, pady=10).pack()
entry_apellido = tkinter.Entry(ventana, font=("Arial", 15), width=15)
entry_apellido.pack()

label_telefono = tkinter.Label(ventana, text="Ingrese su Telefono: ", font=("Arial", 15),padx=10, pady=10).pack()
entry_telefono = tkinter.Entry(ventana, font=("Arial", 15), width=15)
entry_telefono.pack()

label_correo = tkinter.Label(ventana, text="Ingrese su Correo: ", font=("Arial", 15),padx=10, pady=10).pack()
entry_correo = tkinter.Entry(ventana, font=("Arial", 15), width=15)
entry_correo.pack()

label_direccion = tkinter.Label(ventana, text="Ingrese su Direccion: ", font=("Arial", 15),padx=10, pady=10).pack()
entry_direccion = tkinter.Entry(ventana, font=("Arial", 15), width=15)
entry_direccion.pack()

# botones para agregar, eliminar, mostrar y salir
boton_agregar = tkinter.Button(ventana, text="Agregar", font=("Arial", 14), command=agregar_datos).pack(padx=5, pady=2)

boton_eliminar = tkinter.Button(ventana, text="Eliminar", font=("Arial", 14), command=eliminar_datos).pack(padx=5, pady=2)

boton_mostrar = tkinter.Button(ventana, text="Mostrar", font=("Arial", 14), command=mostrar_datos).pack(padx=5, pady=2)

boton_salir = tkinter.Button(ventana, text="Salir", font=("Arial", 14), command=salir).pack(padx=5, pady=2)

# bucle para que la ventana se mantenga abierta
ventana.mainloop()