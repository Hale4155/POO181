import tkinter as tk
from tkinter import *

class Cuenta:
    def __init__(self, numero_cuenta, titular, edad, saldo):
        self.__numero_cuenta = numero_cuenta
        self.__titular = titular
        self.__edad = edad
        self.__saldo = saldo
    
    def consultar_saldo(self):
        return self.__saldo
    
    def ingresar_efectivo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a ingresar debe ser mayor a cero.")
        self.__saldo += cantidad
    
    def retirar_efectivo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a retirar debe ser mayor a cero.")
        if cantidad > self.__saldo:
            raise ValueError("No se puede retirar más de lo que hay en la cuenta.")
        self.__saldo -= cantidad
    
    def depositar_otra_cuenta(self, cantidad, cuenta_destino):
        if cantidad <= 0:
            raise ValueError("La cantidad a depositar debe ser mayor a cero.")
        cuenta_destino.ingresar_efectivo(cantidad)
        self.__saldo -= cantidad
    
    def __str__(self):
        return f"No. Cuenta: {self.__numero_cuenta}\nTitular: {self.__titular}\nEdad: {self.__edad}\nSaldo: {self.__saldo}"

class InterfazCajaPopular:
    def __init__(self, master):
        self.master = master
        self.master.title("Caja Popular")
        
        self.cuenta = Cuenta(12345, "Juan Pérez", 30, 5000)
        
        # Etiqueta para mostrar el saldo actual
        self.saldo_label = tk.Label(self.master, text=f"Saldo actual: {self.cuenta.consultar_saldo()}")
        self.saldo_label.pack(pady=10)
        
        # Sección para ingresar efectivo
        self.ingresar_label = tk.Label(self.master, text="Ingresar efectivo:")
        self.ingresar_label.pack()
        
        self.cantidad_entry_ingresar = tk.Entry(self.master)
        self.cantidad_entry_ingresar.pack()
        
        self.ingresar_button = tk.Button(self.master, text="Ingresar", command=self.ingresar_efectivo)
        self.ingresar_button.pack()
        
        # Sección para retirar efectivo
        self.retirar_label = tk.Label(self.master, text="Retirar efectivo:")
        self.retirar_label.pack()
        
        self.cantidad_entry_retirar = tk.Entry(self.master)
        self.cantidad_entry_retirar.pack()
        
        self.retirar_button = tk.Button(self.master, text="Retirar", command=self.retirar_efectivo)
        self.retirar_button.pack()
        
        # Sección para depositar a otra cuenta
        self.depositar_label = tk.Label(self.master, text="Depositar a otra cuenta:")
        self.depositar_label.pack()
        
        self.depositar_cantidad_label = tk.Label(self.master, text="Cantidad:")
        self.depositar_cantidad_label.pack()
        
        self.depositar_cantidad_entry = tk.Entry(self.master)
        self.depositar_cantidad_entry.pack()
        
        self.depositar_cuenta_destino_label = tk.Label(self.master, text="No. cuenta destino:")
        self.depositar_cuenta_destino_label.pack()
        
        self.depositar_cuenta_destino_entry = tk.Entry(self.master)
        self.depositar_cuenta_destino_entry.pack()
        
        self.depositar_button = tk.Button(self.master, text="Depositar", command=self.depositar_otra_cuenta)
        self.depositar_button.pack()

    def actualizar_saldo_label(self):
            self.saldo_label.config(text=f"Saldo actual: {self.cuenta.consultar_saldo()}")

    def ingresar_efectivo(self):
        try:
            cantidad = int(self.cantidad_entry_ingresar.get())
            self.cuenta.ingresar_efectivo(cantidad)
            self.actualizar_saldo_label()
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))

    def retirar_efectivo(self):
        try:
            cantidad = int(self.cantidad_entry_retirar.get())
            self.cuenta.retirar_efectivo(cantidad)
            self.actualizar_saldo_label()
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))

    def depositar_otra_cuenta(self):
        try:
            cantidad = int(self.depositar_cantidad_entry.get())
            cuenta_destino = Cuenta(int(self.depositar_cuenta_destino_entry.get()), "Desconocido", 0, 0)
            self.cuenta.depositar_otra_cuenta(cantidad, cuenta_destino)
            self.actualizar_saldo_label()
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))
            
root = tk. Tk()
app = InterfazCajaPopular(root)
root.mainloop()