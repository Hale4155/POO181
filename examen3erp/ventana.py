from tkinter import *
from tkinter import ttk

import tkinter as tk 

ventana = Tk()
ventana.title("CRUD de Mercancías")
ventana.geometry("800x600")

panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')

pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)

varNom = tk.StringVar()
titulo1 = Label(pestana1, text="Nombre de la mercancía:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
mercancia = Entry(pestana1, textvariable=varNom, font=("Helvetica", 18)).pack( padx=20, pady=10)
        
varPais = tk.StringVar()        
titulo2 = Label(pestana1, text="País de origen:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
pais = Entry(pestana1,textvariable=varPais, font=("Helvetica", 18)).pack( padx=20, pady=10, )

botonLog = tk.Button(pestana1, text="Guardar Mercancía", fg="Black", bg="#00ccff", font=("Modern", 15),)
botonLog.pack()

#pestaña2: consultarXpais

titulo2 = Label(pestana2, text="Buscar país", fg="green",font=("Modern", 18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2,text="Nombre del país: ").pack()
txtid = Entry(pestana2,textvariable=varBus).pack()
btnBus = Button(pestana2,text="Buscar").pack()

subBus = Label(pestana2,text="encontrado:",fg="blue",font=("Modern",15)).pack()
textEnc = tk.Text(pestana2,height=5,width=52)
textEnc.pack()

botonConsultarPais = tk.Button(pestana2, text="Consultar Países", fg="Black", bg="#00ccff", font=("Modern", 15))
botonConsultarPais.pack()

#pestaña3: eliminar 
titulo3 = Label(pestana3, text="Eliminar mercancía", fg="green",font=("Modern", 18)).pack()

varIDs = tk. StringVar()
lblid = Label(pestana3,text="ID de la mercancía: ").pack()
txtid = Entry(pestana3,textvariable=varIDs).pack()
btnElim = Button(pestana3,text="Eliminar").pack()

panel.add(pestana1, text="Insertar Mercancía")
panel.add(pestana2, text="consultar pais")
panel.add(pestana3, text="eliminar")

ventana.mainloop()
