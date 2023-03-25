from tkinter import messagebox
import sqlite3 
import bcrypt 

class controladorBD:
    
    def __init__(self):
        pass
    #metdo para crear conexiones 
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/alexh/OneDrive/Documentos/GitHub/POO181/tkinterSQLite/TBResgistrados.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:   
            print("no se pudo conectar a la BD")
    
    #metodos para guardar usuarios
    
    def guardarUsuario(self,nom,cor,con):
        
        #1. usamos una conexion 
        
        conx= self.conexionBD()
        
        #2. validar paramestros vacios 
        if(nom ==""or cor=="" or con ==""):
            messagebox.showwarning("cuidado","formulario incompleto")
        else:
            
            #3. preparamos cursor,datos,querysql
            cursor= conx.cursor()
            conH=self.encriptarCon(con)
            datos=(nom,cor,conH)
            qrInsert="insert into TBRegistrados(nombre,correo,contra) values(?,?,?)"
            
            #4. ejecutar insert y cerramos conexion
            cursor.execute(qrInsert,datos) 
            conx.commit()
            conx.close
            messagebox.showinfo("Exito","Usuario Guardado") 
            
    # metodo para encriptar contraseñas        
    def encriptarCon(self,con):
        conplana= con
        
        #preparamos con en bytes y la sal
        conplana= conplana.encode() #convertimos con a bytes        
        sal = bcrypt.gensalt()
        
        #encryptamos la contraseña
        conHa= bcrypt.hashpw(conplana,sal)
        print(conHa)
        
        #enviamos la contraseña encryptada
        return conHa         