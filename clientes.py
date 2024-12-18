import mysql.connector

class Clientes:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into clientes(nombre_cliente, apellido_cliente, dni_cliente, email, telefono) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre_cliente, apellido_cliente, dni_cliente, email, telefono from clientes where id_cliente=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_cliente, nombre_cliente, apellido_cliente, dni_cliente, email, telefono from clientes"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from clientes where id_cliente=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas

    def modificacion(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="update clientes set nombre_cliente=%s, apellido_cliente=%s, dni_cliente=%s, email=%s, telefono=%s where id_cliente=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas modificadas
    