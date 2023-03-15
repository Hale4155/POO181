import tkinter as tk
from datetime import datetime

class Transaccion:
    def __init__(self, tipo, cantidad, cuenta_origen=None, cuenta_destino=None):
        self.fecha = datetime.now()
        self.tipo = tipo
        self.cantidad = cantidad
        self.cuenta_origen = cuenta_origen
        self.cuenta_destino = cuenta_destino

class CuentaBancaria:
    def __init__(self, numero_cuenta, titular, edad, saldo):
        self.numero_cuenta = numero_cuenta
        self.titular = titular
        self.edad = edad
        self.saldo = saldo
        self.transacciones = []
    
        self.cuenta =CuentaBancaria(12345, "Juan Pérez", 30, 5000)
    
    def consultar_saldo(self):
        return self.saldo
    
    def ingresar_efectivo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self.saldo += cantidad
        transaccion = Transaccion("Ingreso", cantidad)
        self.transacciones.append(transaccion)
        
    def retirar_efectivo(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta.")
        self.saldo -= cantidad
        transaccion = Transaccion("Retiro", cantidad)
        self.transacciones.append(transaccion)
        
    def depositar_otra_cuenta(self, cantidad, cuenta_destino):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if cantidad > self.saldo:
            raise ValueError("No hay suficiente saldo en la cuenta.")
        cuenta_destino.ingresar_efectivo(cantidad)
        self.saldo -= cantidad
        transaccion = Transaccion("Depósito", cantidad, self, cuenta_destino)
        self.transacciones.append(transaccion)
        
class CuentaGUI:
    def __init__(self, master, cuenta):
        self.master = master
        self.cuenta = cuenta
        
        # Etiqueta para mostrar el saldo actual
        self.saldo_label = tk.Label(master, text=f"Saldo actual: {self.cuenta.consultar_saldo()}")
        self.saldo_label.pack()
        
        # Entrada de texto para la cantidad a ingresar o retirar
        self.cantidad_entry = tk.Entry(master)
        self.cantidad_entry.pack()
        
        # Botón para realizar un ingreso
        self.ingresar_button = tk.Button(master, text="Ingresar", command=self.ingresar)
        self.ingresar_button.pack()
        
        # Botón para realizar un retiro
        self.retirar_button = tk.Button(master, text="Retirar", command=self.retirar)
        self.retirar_button.pack()
        
        # Entrada de texto para la cantidad a depositar en otra cuenta
        self.depositar_cantidad_entry = tk.Entry(master)
        self.depositar_cantidad_entry.pack()
        
        # Entrada de texto para el número de cuenta a depositar
        self.depositar_cuenta_entry = tk.Entry(master)
        self.depositar_cuenta_entry.pack()
        
        # Botón para realizar un depósito en otra cuenta
        self.depositar_button = tk.Button(master, text="Depositar en otra cuenta", command=self.depositar)
        self.depositar_button.pack()
        
    def ingresar(self):
        cantidad = float(self.cantidad_entry.get())
        try:
            self.cuenta.ingresar_efectivo(cantidad)
            self.saldo_label.configure(text=f"Saldo actual: {self.cuenta.consultar_saldo()}")
            self.cantidad_entry.delete(0, tk.END)
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))

    def retirar(self):
        cantidad = float(self.cantidad_entry.get())
        try:
            self.cuenta.retirar_efectivo(cantidad)
            self.saldo_label.configure(text=f"Saldo actual: {self.cuenta.consultar_saldo()}")
            self.cantidad_entry.delete(0, tk.END)
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))

    def depositar_otra_cuenta(self):
        try:
            cantidad = int(self.depositar_cantidad_entry.get())
            cuenta_destino = CuentaBancaria(int(self.depositar_cuenta_destino_entry.get()), "Desconocido", 0, 0)
            self.cuenta.depositar_otra_cuenta(cantidad, cuenta_destino)
            self.actualizar_saldo_label()
        except ValueError as error:
            tk.messagebox.showerror("Error", str(error))
            
root = tk. Tk()
app = CuentaGUI(root)
root.mainloop()

