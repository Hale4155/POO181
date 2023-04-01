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
    if usuarios:
        for usuario in usuarios:
            cadena = str(usuario[0]) + " " + usuario[1] + " " + usuario[2] + " " + str(usuario[3])
            textEnc.insert(END, cadena + "\n")
    else:
        messagebox.showinfo("No hay usuarios", "No hay usuarios en la BD")

ventana = Tk()
ventana.title("CRUD de Usuarios")
ventana.geometry("800x600")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4 = ttk.Frame(panel)

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

titulo3 = Label(pestana3, text="Consultar Usuarios", fg="green",font=("Modern", 18)).pack()

varCons = tk.StringVar()
botonCons = Button(pestana3,text="Buscar",command=ejecutarConsultarU).pack()

subCons = Label(pestana3,text="usuarios encontrados:",fg="blue",font=("Modern",15)).pack()
textEnc = tk.Text(pestana3,height=5,width=52)
textEnc.pack()

panel.add(pestana1, text='Formulario usuarios')
panel.add(pestana2, text='Buscar usuarios')
panel.add(pestana3, text='Consultar usuarios')
panel.add(pestana4, text='Actualizar usuarios')

ventana.mainloop()
