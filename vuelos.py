import mysql.connector

class Vuelos:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into vuelos(descripcion_pasaje, hora_vuelo, num_asiento, fk_id_ap_salida, fk_id_ap_destino) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select descripcion_pasaje, hora_vuelo, num_asiento, fk_id_ap_salida, fk_id_ap_destino from vuelos where id_vuelo=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_vuelo, descripcion_pasaje, hora_vuelo, num_asiento, fk_id_ap_salida, fk_id_ap_destino from vuelos"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def obtener_aeropuertos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_aeropuerto FROM aeropuertos")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]