import tkinter as tk
from PasswordGeneratorGUI import PasswordGeneratorGUI

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Generador de Contraseñas")
        self.root.geometry("400x400")
        self.password_generator_gui = PasswordGeneratorGUI(self.root)
        self.root.mainloop()

if __name__ == '__main__':
    MainWindow()

