import sqlite3 
from tkinter import messagebox

class importacionBD:
    
    def __init__(self):
        pass
    
    #metodo para crear conexiones 
    def conexionBD(self):
        
        try:
            conexion = sqlite3.connect("C:/Users/alexh/OneDrive/Documentos/GitHub/POO181/examen3erp/BDImportaciones.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:   
            print("no se pudo conectar a la BD")
            
    def guardarMercancia(self, mercancia, pais):
            
        #1. usamos una conexion 
        conx= self.conexionBD()
            
        #2. validar parametros vacios 
        if(mercancia == "" or pais == ""):
            messagebox.showwarning("cuidado", "formulario incompleto - asegúrate de proporcionar el nombre de la mercancía y el país de procedencia")
        else:
                
            #3. preparamos cursor, datos, querysql
            cursor = conx.cursor()
            datos = (mercancia, pais)
            qrInsert = "insert into TB_Europa(Mercancia, pais) values(?, ?)"
                
            #4. ejecutar insert y cerramos conexion
            cursor.execute(qrInsert, datos) 
            conx.commit()
            conx.close()
            messagebox.showinfo("Exito", "Información sobre la mercancía guardada satisfactoriamente")

    def eliminarMercancia(self, id):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Verificar si el ID contiene algo
        if id == "":
            messagebox.showwarning("Cuidado", "ID vacío, escribe algo válido")
            conx.close()
        else:
            try:
                # 3. Preparar el cursor y la consulta
                cursor = conx.cursor()
                selectQry = "SELECT * FROM TB_Europa WHERE IDImpo = " + id

                # 4. Ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsMercancia = cursor.fetchall()

                # 5. Mostrar ventana de confirmación
                if rsMercancia:
                    confirmacion = messagebox.askyesno("Confirmar eliminación", f"¿Está seguro que desea eliminar la mercancía {rsMercancia[0][1]} y su país de procedencia {rsMercancia[0][2]}?")
                    if confirmacion:
                        # 6. Preparar el query y ejecutar eliminación
                        deleteQry = "DELETE FROM TB_Europa WHERE IDImpo = " + id
                        cursor.execute(deleteQry)
                        conx.commit()
                        conx.close()
                        messagebox.showinfo("Éxito", "Mercancía eliminada")
                    else:
                        conx.close()
                else:
                    messagebox.showwarning("Mercancía no encontrada", f"La mercancía con ID {id} no existe en la base de datos.")
                    conx.close()

            except sqlite3.OperationalError:
                print("Error en la eliminación")
    
    def consultarPais(self, pais):
    # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Verificar si el país contiene algo
        if pais == "":
            messagebox.showwarning("Cuidado", "Nombre de país vacío, escribe algo válido")
            conx.close()
        else:
            try:
                # 3. Preparar el cursor y la consulta
                cursor = conx.cursor()
                selectQry = f"SELECT * FROM TB_Europa WHERE pais = '{pais}'"

                # 4. Ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsPais = cursor.fetchall()

                # 5. Mostrar los resultados
                if rsPais:
                    messagebox.showinfo("País encontrado", f"País: {rsPais[0][2]}, Mercancía: {rsPais[0][1]}, ID: {rsPais[0][0]}")
                    conx.close()
                else:
                    messagebox.showwarning("País no encontrado", f"No se encontró ningún país con el nombre {pais}")
                    conx.close()

            except sqlite3.OperationalError:
                print("Error en la consulta de país")
                
