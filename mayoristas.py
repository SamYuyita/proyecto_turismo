import mysql.connector

class Mayoristas:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into mayoristas(nombre_mayorista, facturacion_anual) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def alta_agencia(self, datosagencia):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into agencias_mayoristas(fk_id_agencia) values (%s)"
        cursor.execute(sql, datosagencia)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre_mayorista, facturacion_anual from mayoristas where id_mayorista=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_mayorista, nombre_mayorista, facturacion_anual from mayoristas"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def obtener_agencias(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_agencia FROM agencias")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    