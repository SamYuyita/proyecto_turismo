import mysql.connector

class Aeropuertos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into aeropuertos(nombre_ap, cant_vuelos_prom, fk_id_pais) values (%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select nombre_ap, cant_vuelos_prom, fk_id_pais from aeropuertos where id_aeropuerto=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_aeropuerto, nombre_ap, cant_vuelos_prom, fk_id_pais from aeropuertos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def baja(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="delete from aeropuertos where id_aeropuerto=%s"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()
        return cursor.rowcount # retornamos la cantidad de filas borradas
    
    def obtener_paises(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_pais FROM paises")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]