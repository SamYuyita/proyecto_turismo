
import mysql.connector

class Reservas:

    def abrir(self):
        conexion=mysql.connector.connect(host="localhost", 
                                              user="root", 
                                              passwd="", 
                                              database="turismo_5")
        return conexion


    def alta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="insert into reservas(fk_id_hotel, fk_id_vuelo, asiento_vuelo_cliente, fecha_reserva, fk_id_cliente, fk_id_agencia) values (%s,%s,%s,%s,%s,%s)"
        cursor.execute(sql, datos)
        cone.commit()
        cone.close()

    def consulta(self, datos):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select fk_id_circuito, fk_id_hotel, fk_id_vuelo, asiento_vuelo_cliente, fecha_reserva, fk_id_cliente, fk_id_agencia from reservas where id_reserva=%s"
        cursor.execute(sql, datos)
        cone.close()
        return cursor.fetchall()

    def recuperar_todos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="select id_reserva, asiento_vuelo_cliente, fecha_reserva from reservas"
        cursor.execute(sql)
        cone.close()
        return cursor.fetchall()
    
    def obtener_circuitos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_circuito FROM circuitos")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    
    def obtener_hoteles(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_hotel FROM hoteles")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    
    def obtener_vuelos(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_vuelo FROM vuelos")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    
    def obtener_clientes(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_cliente FROM clientes")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    
    def obtener_agencias(self):
        cone=self.abrir()
        cursor=cone.cursor()
        cursor.execute("SELECT id_agencia FROM agencias")
        resultados = cursor.fetchall()
        cone.close()
        return [fila[0] for fila in resultados]
    
    

    
    