import mysql.connector

class Circuitos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into circuitos(denominacion_circuito, cant_asist_anual) values (%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        
    def alta_ciudad(self, datosciudad):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into circuitos_ciudades(fk_id_ciudad) values (%s)"
        cursor.execute(sql, datosciudad)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select denominacion_circuito, cant_asist_anual from circuitos where id_circuito=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_circuito, denominacion_circuito, cant_asist_anual from circuitos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def obtener_ciudades(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_ciudad FROM ciudades")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
