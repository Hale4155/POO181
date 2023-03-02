
from tkinter import Tk,Frame,Button,messagebox

#4. funcion de mensajes para el boton 
def mostrarMensaje():
    messagebox.showinfo("Aviso","este mensaje es para informar algo")
    messagebox.showerror("error","todo fallo con exito")
    print(messagebox.askyesnocancel("pregunta: ","el o ella jugo con tu corazon"))

#5.funcion para agregar botones 

def agregarboton():
    botonverde.config(text="+",bg="green",fg="white")
    botonNuevo=Button(seleccion3, text="boton Nuevo")
    botonNuevo.pack()
    
#1. instanciamos un objeto ventana  
ventana = Tk()
ventana.title(" practica 11: frames")
ventana.geometry("600x400")

#2. definimos secciones de la ventana
seccion1=Frame(ventana,bg="#99ffff")
seccion1.pack(expand=True, fill="both")
seleccion2=Frame(ventana,bg="#00cccc")
seleccion2.pack(expand=True, fill="both")
seleccion3=Frame(ventana,bg="#ffb380")
seleccion3.pack(expand=True, fill="both")

#3.botones

botonAzul= Button(seccion1, text="boton azul",fg="blue",command=mostrarMensaje )
botonAzul.place(x=60, y=60)

botonamarillo= Button(seleccion2, text="boton amarillo",bg="yellow", fg="black")
botonamarillo.grid(row= 0, column=0)

botonnegro= Button(seleccion2, text="boton negro", bg="black", fg="white")
botonnegro.grid(row=1, column=1)

botonverde =Button(seleccion3,text="boton verde",bg="#66ff99",command= agregarboton)
botonverde.pack()
ventana.mainloop()

