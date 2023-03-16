import tkinter as tk
from tkinter import messagebox

class GeneradorMatriculas: 
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de Matrículas")
    
        #almacenar datos de entrada 
        self.nombre_var = tk.StringVar()
        self.apellidopaterno_var = tk.StringVar()
        self.apellidomaterno_var = tk.StringVar()
        self.fecha_nacimiento_var = tk.StringVar()
        self.carrera_var = tk.StringVar()
        
        tk.Label(self.master, text="Nombre:").grid(row=0, column=0)
        tk.Entry(self.master, textvariable=self.nombre_var).grid(row=0, column=1)
        
        tk.Label(self.master, text="Apellido paterno:").grid(row=1, column=0)
        tk.Entry(self.master, textvariable=self.apellidopaterno_var).grid(row=1, column=1)
        
        tk.Label(self.master, text="apellido materno:").grid(row=2, column=0)
        tk.Entry(self.master, textvariable=self.apellidomaterno_var).grid(row=2, column=1)
        
        tk.Label(self.master, text="fecha de nacimiento:").grid(row=3, column=0)
        tk.Entry(self.master, textvariable=self.fecha_nacimiento_var).grid(row=3, column=1)
        
        tk.Label(self.master, text="Carrera:").grid(row=4, column=0)
        tk.Entry(self.master, textvariable=self.carrera_var).grid(row=4, column=1)
        
        # Botón para generar la matrícula
        tk.Button(self.master, text="Generar Matrícula", command=self.generar_matricula).grid(row=4, column=0, columnspan=2, pady=10)
        
        self.matricula_var = tk.StringVar()
        self.matricula_var.set("")
        
    def generar_matricula(self):
        nombre = self.nombre_var.get()
        apellidopaterno = self.apellidopaterno_var.get()
        apellidomaterno = self.apellidomaterno_var.get()
        fecha_nacimiento = self.fecha_nacimiento_var.get()
        carrera = self.carrera_var.get()
        
        # Extraer la letra del nombre, apellido y carrera
        letra_nombre = nombre[0]
        letra_apellido = apellidopaterno[0]
        letra_apellido= apellidomaterno[0]
        letra_carrera = carrera[0]
        
        # Extraer los dos dígitos de la fecha de nacimiento
        dia, mes, año = fecha_nacimiento.split("/")
        digitos_fecha = año[-2:]
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        