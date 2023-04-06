from tkinter import *
from tkinter import ttk
from productosBD import *

import tkinter as tk

# Creamos un objeto de la clase controladorBD
controlador = productosBD()

# Función para dar de alta un nuevo producto
def ejecutaInsert():
    controlador.guardarProducto(varNom.get(), varDes.get(), varPrecio.get())

# Función para buscar un producto por su ID
def ejecutaSelectP():
    producto = controlador.consultarProducto(varBus.get())
    if producto:
        cadena = str(producto[0][0]) + " " + producto[0][1] + " " + str(producto[0][2])
        textEnc.delete(1.0, END)
        textEnc.insert(END, cadena)
    else:
        messagebox.showinfo("Producto no encontrado", "El producto no existe en la BD")

def ejecutarActualizarP():
    controlador.actualizarProducto(varID.get(),varNomAct.get(), varDesAct.get(), varPreAct.get())
    # mostramos un mensaje en pantalla
    messagebox.showinfo("Actualización exitosa", "El Producto ha sido actualizado correctamente")


# Función para dar de baja un producto por su ID
def ejecutarEliminarP():
    controlador.eliminarProducto(varIDs.get())

# Función para consultar todos los productos de la base de datos
def ejecutarConsultarP():
    productos = controlador.importarProductos()
    treeview.delete(*treeview.get_children())
    if productos:
        for producto in productos:
            treeview.insert("", "end", values=(producto[0], producto[1], producto[2], producto[3]))
    else:
        messagebox.showinfo("No hay productos", "No hay productos en la BD")

# Creamos la ventana principal
ventana = Tk()
ventana.title("ABM de productos")
ventana.geometry("800x600")

# Creamos las pestañas del panel
panel = ttk.Notebook(ventana)
panel.pack(fill='both', expand='yes')
pestana1 = ttk.Frame(panel)
pestana2 = ttk.Frame(panel)
pestana3 = ttk.Frame(panel)
pestana4= ttk.Frame(panel)
pestaña5= ttk.Frame(panel)

# Pestaña 1: alta de productos
varNom = tk.StringVar()
titulo1 = Label(pestana1, text="Nombre:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
nombre = Entry(pestana1, textvariable=varNom, font=("Helvetica", 18)).pack( padx=20, pady=10)

varDes= tk.StringVar()
titulo2 = Label(pestana1, text="descripcion:", font=("Modern",18)).pack(fill=tk.X, padx=20, pady=5)
descripcion = Entry(pestana1, textvariable=varDes, font=("Helvetica", 18)).pack( padx=20, pady=10)

varPrecio = tk.StringVar()
titulo3 = Label(pestana1, text="Precio:", font=("Modern", 18)).pack(fill=tk.X, padx=20, pady=5)
precio = Entry(pestana1,textvariable=varPrecio, font=("Helvetica", 18)).pack( padx=20, pady=10, )


botonGuardar = tk.Button(pestana1, text="Guardar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutaInsert)
botonGuardar.pack()

# Pestaña 2: búsqueda de productos
titulo2 = Label(pestana2, text="Buscar producto", fg="green",font=("Modern", 18)).pack()

varBus = tk.StringVar()
lblid = Label(pestana2,text="identificador producto: ").pack()
txtid = Entry(pestana2,textvariable=varBus).pack()
btnBus = Button(pestana2,text="Buscar",command=ejecutaSelectP).pack()

subBus = Label(pestana2,text="encontrado:",fg="blue",font=("Modern",15)).pack()
textEnc = tk.Text(pestana2,height=5,width=52)
textEnc.pack()

titulo3 = Label(pestana3, text="Consultar productos", fg="green",font=("Modern", 18)).pack()

varCons = tk.StringVar()
botonCons = Button(pestana3,text="Buscar",command=ejecutarConsultarP).pack()

treeview = ttk.Treeview(pestana3, columns=(1, 2, 3, 4), show="headings", height="5")
treeview.heading(1, text="ID")
treeview.column(1, width=50)
treeview.heading(2, text="Nombre")
treeview.column(2, width=150)
treeview.heading(3, text="Descripcion")
treeview.column(3, width=200)
treeview.heading(4, text="Precio")
treeview.column(4, width=100)

subCons = Label(pestana3,text="productos encontrados:",fg="blue",font=("Modern",15)).pack()
treeview.pack()

#pestaña4: actualizar productos
titulo4 = Label(pestana4, text="Actualizar Producto", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

#Campo para ingresar el ID del producto a actualizar
varID = tk. StringVar()
lblID = Label(pestana4, text="ID del producto:", font=("Modern", 15)).pack(padx=20, pady=5)
txtID = Entry(pestana4, textvariable=varID, font=("Helvetica", 15))
txtID.pack(padx=20, pady=5)

#Campos para ingresar los nuevos datos del producto
varNomAct = tk.StringVar()
lblNomAct = Label(pestana4, text="Nuevo Nombre", font=("Modern", 15)).pack(padx=20, pady=5)
txtNomAct = Entry(pestana4, textvariable=varNomAct, font=("Helvetica", 15))
txtNomAct.pack(padx=20, pady=5)


varDesAct = tk. StringVar()
lblDesAct = Label(pestana4, text="Nueva Descripcion", font=("Modern", 15)).pack(padx=20, pady=5)
txtDesAct = Entry(pestana4, textvariable=varDesAct, font=("Helvetica", 15))
txtDesAct.pack(padx=20, pady=5)

varPreAct = tk. StringVar()
lblPreAct = Label(pestana4, text="Nuevo precio:", font=("Modern", 15)).pack(padx=20, pady=5)
txtPreAct = Entry(pestana4, textvariable=varPreAct, font=("Helvetica", 15))
txtPreAct.pack(padx=20, pady=5)

#Botón para actualizar el producto
botonAct = tk. Button(pestana4, text="Actualizar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutarActualizarP )
botonAct.pack()

#pestaña5: eliminar producto
titulo5 = Label(pestaña5, text="Eliminar Producto", font=("Modern",18)).pack(fill=tk. X, padx=20, pady=10)

#Campo para ingresar el ID del producto a eliminar
varIDs = tk. StringVar()
lblIDs = Label(pestaña5, text="ID del producto:", font=("Modern", 15)).pack(padx=20, pady=5)
txtIDs = Entry(pestaña5, textvariable=varIDs, font=("Helvetica", 15))
txtIDs.pack(padx=20, pady=5)

#Botón para eliminar el producto
botonElm = tk. Button(pestaña5, text="Eliminar producto", fg="Black", bg="#00ccff", font=("Modern", 15), command=ejecutarEliminarP)
botonElm.pack()

panel.add(pestana1, text='Formulario productos')
panel.add(pestana2, text='Buscar productos')
panel.add(pestana3, text='Consultar productos')
panel.add(pestana4, text='Actualizar productos')
panel.add(pestaña5, text='Eliminar productos')

ventana.mainloop()
