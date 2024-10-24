
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
        sql="insert into reservas(asiento_vuelo_cliente, fecha_reserva) values (%s,%s)"
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
    
    # Función para buscar cliente por DNI
    def buscar_cliente_por_dni(self, dni_cliente):
        cone=self.abrir()
        cursor=cone.cursor()
        sql="SELECT id_cliente FROM clientes WHERE dni_cliente = %s"
        cursor.execute(sql, (dni_cliente))
        result = cursor.fetchone()  # Obtiene una fila, si existe
        cursor.close()
    
        if result:
            return result[0]  # Devuelve el id_cliente
        else:
            return None  # El cliente no existe
    # lastrowid' que almacena el código de artículo que se acaba de generar
    # cursor.lastrowid