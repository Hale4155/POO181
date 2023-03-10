import tkinter as tk
import random
import string
from tkinter import messagebox

class PasswordGeneratorGUI:
    
    def __init__(self, master):
        self.master = master
        #Variables para las opciones
        self.password_length = tk.IntVar(value=8)
        self.include_uppercase = tk.BooleanVar(value=False)
        self.include_special_chars = tk.BooleanVar(value=False)
        self.check_strength = tk.BooleanVar(value=False)
        
        #Frame para las opciones
        self.options_frame = tk.LabelFrame(self.master, text="Opciones")
        self.options_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        #Entry para la longitud de la contraseña
        tk.Label(self.options_frame, text="Longitud de la contraseña:").grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Entry(self.options_frame, textvariable=self.password_length).grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
        
        #Checkbuttons para incluir mayúsculas y caracteres especiales
        tk.Checkbutton(self.options_frame, text="Incluir Mayúsculas", variable=self.include_uppercase).grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        tk.Checkbutton(self.options_frame, text="Incluir Caracteres Especiales", variable=self.include_special_chars).grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        
        #Checkbutton para comprobar fortaleza de la contraseña
        tk.Checkbutton(self.options_frame, text="Comprobar Fortaleza de la Contraseña", variable=self.check_strength).grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        
        #Botón para generar contraseña
        tk.Button(self.master, text="Generar Contraseña", command=self.generate_password).pack(pady=10)
        
        #Frame para la contraseña
        self.password_frame = tk.LabelFrame(self.master, text="Contraseña Generada")
        self.password_frame.pack(padx=20, pady=20, fill=tk.BOTH, expand=True)
        
        #Entry para mostrar la contraseña
        self.password_entry = tk.Entry(self.password_frame, width=30, font=('Arial', 16), justify='center')
        self.password_entry.pack(padx=10, pady=10)
        
    def generate_password(self):
        length = self.password_length.get()
        include_uppercase = self.include_uppercase.get()
        include_special_chars = self.include_special_chars.get()
        check_strength = self.check_strength.get()
        
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        numbers = string.digits
        special_chars = string.punctuation
        
        #Crear lista con los caracteres permitidos
        allowed_chars = list(lowercase_letters)
        if include_uppercase:
            allowed_chars.extend(list(uppercase_letters))
        if include_special_chars:
            allowed_chars.extend(list(special_chars))
        if numbers:
            allowed_chars.extend(list(numbers)) 
        
        #Generar la contraseña
        password = ''.join(random.choice(allowed_chars) for i in range(length))
        
        #Comprobar la fortaleza de la contraseña si la opción está seleccionada
        strength = ""
        if check_strength:
            #Comprobar longitud mínima
            if length < 8:
                strength = "La contraseña es muy débil"
            #Comprobar si hay mayúsculas
            elif include_uppercase and not any(char.isupper() for char in password):
                strength = "La contraseña es débil (no incluye mayúsculas)"
            #Comprobar si hay caracteres especiales
            elif include_special_chars and not any(char in special_chars for char in password):
                strength = "La contraseña es débil (no incluye caracteres especiales)"
            #Comprobar si hay números
            elif not any(char.isdigit() for char in password):
                strength = "La contraseña es débil (no incluye números)"
            #Comprobar si hay minúsculas
            elif not any(char.islower() for char in password):
                strength = "La contraseña es débil (no incluye minúsculas)"
            #Si se cumplen todos los requisitos, la contraseña es fuerte
            else:
                strength = "La contraseña es fuerte"
        
        #Mostrar la contraseña en la interfaz de usuario
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        
        #Mostrar la fortaleza de la contraseña en la interfaz de usuario
        if check_strength:
            tk.messagebox.showinfo(title="Fortaleza de la Contraseña", message=strength)
