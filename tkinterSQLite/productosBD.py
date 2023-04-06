from tkinter import messagebox
import sqlite3

class productosBD:

    def __init__(self):
        pass

    # método para crear conexiones
    def conexionBD(self):
        try:
            conexion = sqlite3.connect("C:/Users/alexh/OneDrive/Documentos/GitHub/POO181/tkinterSQLite/TBProductos.db")
            print("conectado a la BD")
            return conexion
        except sqlite3.OperationalError:
            print("no se pudo conectar a la BD")

    # métodos para guardar productos
    def guardarProducto(self, nombre, desc, precio):
        # 1. usamos una conexión
        conx = self.conexionBD()

        # 2. validar parámetros vacíos
        if nombre == "" or desc == "" or precio == "":
            messagebox.showwarning("cuidado", "formulario incompleto")
        else:
            try:
                # 3. preparamos cursor, datos, query sql
                cursor = conx.cursor()
                datos = (nombre, desc, precio)
                qrInsert = "insert into TBProductos(nombre, descripcion, precio) values(?,?,?)"

                # 4. ejecutar insert y cerramos conexion
                cursor.execute(qrInsert, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Guardado")

            except sqlite3.OperationalError:
                print("error al guardar producto")


    # método para buscar 1 producto
    def consultarProducto(self, id):
        # 1. preparar una conexion
        conx = self.conexionBD()

        # 2.verificar si id contiene algo
        if id == "":
            messagebox.showwarning("cuidado", "id vacio escribe algo valido")
            conx.close()
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()
                selectQry = "select * from TBProductos where id=" + id

                # 4. ejecutar y guardar la consulta
                cursor.execute(selectQry)
                rsProducto = cursor.fetchall()
                conx.close()
                return rsProducto

            except sqlite3.OperationalError:
                print("error consulta")

    # método para consultar a todos los productos de la base de datos
    def importarProductos(self):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        try:
            # 2. Preparar el cursor y la consulta
            cursor = conx.cursor()
            selectQry = "select * from TBProductos"

            # 3. Ejecutar y guardar la consulta
            cursor.execute(selectQry)
            rsProductos = cursor.fetchall()
            conx.close()

            return rsProductos

        except sqlite3.OperationalError:
            print("error consulta")

    # método para actualizar un producto
    def actualizarProducto(self, id, nom, desc, precio):
        # 1. Preparar una conexión
        conx = self.conexionBD()

        # 2. Validar parámetros vacíos
        if desc == "" or precio == "":
            messagebox.showwarning("cuidado", "formulario incompleto")
        else:
            try:
                # 3. Preparar el cursor, datos y query SQL
                cursor = conx.cursor()
                datos = (nom, desc, precio, id)
                qrUpdate = "update TBProductos set nombre=?, descripcion=?, precio=? where id=?"

                # 4. Ejecutar update y cerrar conexión
                cursor.execute(qrUpdate, datos)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Actualizado")

            except sqlite3.OperationalError:
                print("error al actualizar producto")

    # método para eliminar un producto
    def eliminarProducto(self, id):
        # 1. preparar una conexión
        conx = self.conexionBD()

        # 2. verificar si id contiene algo
        if id == "":
            messagebox.showwarning("cuidado", "id vacio escribe algo valido")
            conx.close()
        else:
            try:
                # 3. preparar el cursor y el query
                cursor = conx.cursor()
                deleteQry = "delete from TBProductos where id=" + id

                # 4. ejecutar y confirmar la eliminación
                cursor.execute(deleteQry)
                conx.commit()
                conx.close()
                messagebox.showinfo("Exito", "Producto Eliminado")

            except sqlite3.OperationalError:
                print("error al eliminar producto")
