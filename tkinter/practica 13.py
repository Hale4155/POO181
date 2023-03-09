import tkinter as tk
from logica13 import*
from tkinter import *

class PasswordGenerator:
    def __init__(self, master):
        self.master = master
        self.master.title("Generador de contraseñas")
        
        self.length_label = tk.Label(self.master, text="Longitud de la contraseña:")
        self.length_label.pack()
        
        self.length_entry = tk.Entry(self.master)
        self.length_entry.pack()
        
        self.generate_button = tk.Button(self.master, text="Generar contraseña")
        self.generate_button.pack()
        
        self.password_label = tk.Label(self.master, text="")
        self.password_label.pack()
        
        
if __name__ == '__main__':
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
