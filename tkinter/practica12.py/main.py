from ventana import ventana
from tkinter import *

root = Tk()

ventana= Tk()
ventana.title(" practica 12: login con tkinter y P.O.O")
ventana.geometry("600x400")

label=Label(ventana, text="correo:")
label.pack()
texto = Entry(ventana)
texto.pack()

label=Label(ventana, text="contraseña:")
label.pack()
texto2= Entry(ventana, show="*")
texto2.pack()

botonlogin =Button(ventana,text="boton verde",bg="#66ff99",command=login)
botonlogin.pack()

ventana.mainloop()

