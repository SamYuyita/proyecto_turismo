import mysql.connector

class Agencias:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into agencias(cant_empleados, direccion) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def alta_mayo(self, datosmayo):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into agencias_mayoristas(fk_id_mayorista) values (%s)"
        cursor.execute(sql, datosmayo)
        cone.commit()
        cone.close()


    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select cant_empleados, direccion from agencias where id_agencia=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_agencia, cant_empleados, direccion from agencias"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def obtener_mayoristas(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_mayorista FROM mayoristas")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    