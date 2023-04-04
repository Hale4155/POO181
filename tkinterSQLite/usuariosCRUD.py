from tkinter import *
from tkinter import ttk

import tkinter as tk
from controladorBD import * #1. mandamos a llamar los metodos dentro de la clase controladorBD

#2.creamos 1 objeto de la clase controladorBD
#ademas nos ayudara a iniciar los metodos de la clase 

controlador = controladorBD()

#3.funcion para disparar el boton de ingresar un usuario

def ejecutaInsert():
    controlador.guardarUsuario(varNom.get(), varCor.get(), varCon.get())

#4.funcion para disparar el boton de busqueda 

def ejecutaSelectU():
    usuario = controlador.consultarUsuario(varBus.get())
    if usuario:
        cadena = str(usuario[0][0]) + " " + usuario[0][1] + " " + usuario[0][2] + " " + str(usuario[0][3])
        textEnc.delete(1.0, END) #limpiamos el contenido anterior del widget
        textEnc.insert(END, cadena)
    else:
        messagebox.showinfo("Usuario no encontrado", "El usuario no existe en la BD") 
        
        
        
def ejecutarConsultarU():
    usuarios = controlador.importarUsuarios()
    # limpiamos el contenido anterior del widget treeview
    treeview.delete(*treeview.get_children())
    if usuarios:
        for usuario in usuarios:
            treeview.insert("", "end", values=(usuario[0], usuario[1], usuario[2], usuario[3]))
    else:
        messagebox.showinfo("No hay usuarios", "No hay usuarios en la BD")
    
    treeview.pack()
    
def ejecutarActualizarU():
    controlador.actualizarUsuario(varID.get(), varNomAct.get(), varCorAct.get(), varConAct.get())
    # mostramos un mensaje en pantalla
    messagebox.showinfo("Actualización exitosa", "El usuario ha sido actualizado correctamente")

    
def ejecutarEliminarU():
    controlador.eliminarUsuario(varIDs.get())
    

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("800x600")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)
pestaña5= ttk.Frame(panel)

varNom = tk.StringVar()
titulo1 = Label(pestana1, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
usuario = Entry(pestana1, textvariable=varNom, font=("Helvetica", 18)).pack( padx=20, pady=10)
        
varCor = tk.StringVar()        
titulo2 = Label(pestana1, text="Correo:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
correo = Entry(pestana1,textvariable=varCor, font=("Helvetica", 18)).pack( padx=20, pady=10, )

varCon = tk.StringVar()
titulo3 = Label(pestana1, text="Contraseña:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
contraseña = Entry(pestana1, textvariable=varCon, show="*", font=("Helvetica", 18)).pack(padx=20, pady=10,)

botonLog = tk.Button(pestana1, text="Guardar Usuario", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutaInsert)
botonLog.pack()

#pestaña2: buscar usuario

titulo2 = Label(pestana2, text="Buscar usuario", fg="green",font=("Modern", 18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2,text="identificador usuario: ").pack()
txtid = Entry(pestana2,textvariable=varBus).pack()
btnBus = Button(pestana2,text="Buscar",command=ejecutaSelectU).pack()

subBus = Label(pestana2,text="encontrado:",fg="blue",font=("Modern",15)).pack()
textEnc = tk.Text(pestana2,height=5,width=52)
textEnc.pack()

#pestaña3: consultar usuarios 
#pestaña3: consultar usuarios 

titulo3 = Label(pestana3, text="Consultar Usuarios", fg="green",font=("Modern", 18)).pack()

varCons = tk.StringVar()
botonCons = Button(pestana3,text="Buscar",command=ejecutarConsultarU).pack()

treeview = ttk.Treeview(pestana3, columns=(1,2,3,4), show="headings", height="5")
treeview.heading(1, text="ID")
treeview.column(1, width=50)
treeview.heading(2, text="Nombre")
treeview.column(2, width=150)
treeview.heading(3, text="Correo")
treeview.column(3, width=200)
treeview.heading(4, text="Contraseña")
treeview.column(4, width=100)

subCons = Label(pestana3,text="usuarios encontrados:",fg="blue",font=("Modern",15)).pack()
treeview.pack()

#pestaña4: actualizar usuarios
titulo4 = Label(pestana4, text="Actualizar usuario", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=10)

#Campo para ingresar el ID del usuario a actualizar
varID = tk.StringVar()
lblID = Label(pestana4, text="ID del usuario:", font=("Modern", 15)).pack(padx=20, pady=5)
txtID = Entry(pestana4, textvariable=varID, font=("Helvetica", 15))
txtID.pack(padx=20, pady=5)

#Campos para ingresar los nuevos datos del usuario
varNomAct = tk.StringVar()
lblNomAct = Label(pestana4, text="Nuevo nombre:", font=("Modern", 15)).pack(padx=20, pady=5)
txtNomAct = Entry(pestana4, textvariable=varNomAct, font=("Helvetica", 15))
txtNomAct.pack(padx=20, pady=5)

varCorAct = tk.StringVar()        
lblCorAct = Label(pestana4, text="Nuevo correo:", font=("Modern", 15)).pack(padx=20, pady=5)
txtCorAct = Entry(pestana4, textvariable=varCorAct, font=("Helvetica", 15))
txtCorAct.pack(padx=20, pady=5)

varConAct = tk.StringVar()
lblConAct = Label(pestana4, text="Nueva contraseña:", font=("Modern", 15)).pack(padx=20, pady=5)
txtConAct = Entry(pestana4, textvariable=varConAct, show="*", font=("Helvetica", 15))
txtConAct.pack(padx=20, pady=5)

#Botón para actualizar el usuario
botonAct = tk. Button(pestana4, text="Actualizar usuario", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutarActualizarU)
botonAct.pack()

#pestaña5: eliminar usuario 
titulo5 = Label(pestaña5, text="Eliminar usuario", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=10)


#Campo para ingresar el ID del usuario a eliminar
varIDs = tk.StringVar()
lblIDs = Label(pestaña5, text="ID del usuario:", font=("Modern", 15)).pack(padx=20, pady=5)
txtIDs = Entry(pestaña5, textvariable=varIDs, font=("Helvetica", 15))
txtIDs.pack(padx=20, pady=5)

#Botón para actualizar el usuario
botonElm = tk. Button(pestaña5, text="Eliminar usuario", fg="Black", bg="#00ccff", font=("Modern", 15),command=ejecutarEliminarU)
botonElm.pack()


panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')
panel.add(pestaña5, text="eliminar usuarios")

ventana.mainloop()
