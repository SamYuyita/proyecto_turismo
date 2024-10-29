import tkinter as tk
import os

def abrir_clientes():
    os.system('python 1form_clientes.py')

def abrir_agencias():
    os.system('python 2form_agencias.py')
    
def abrir_mayoristas():
    os.system('python 3form_mayoristas.py')

def abrir_hoteles():
    os.system('python 4form_hoteles.py')
    
def abrir_circuitos():
    os.system('python 5form_circuitos.py')
    
def abrir_vuelos():
    os.system('python 6form_vuelos.py')
    
def abrir_aeropuertos():
    os.system('python 7form_aeropuertos.py')

def abrir_reservas():
    os.system('python 8form_reservas.py')
    
ventana = tk.Tk()
ventana.title("Agencia de turismo")
ventana.state('zoomed')
ventana.configure(bg='gray')

etiqueta=tk.Label(ventana, text="Agencia de turismo", font=("Helvetica", 21, "bold"))
etiqueta.pack(pady=40)

botonclientes = tk.Button(ventana, text="Clientes", padx=20, command=abrir_clientes)
botonclientes.pack(pady=20)

botonagencias = tk.Button(ventana, text="Agencias", padx=20, command=abrir_agencias)
botonagencias.pack(pady=20)

botonmayorstas = tk.Button(ventana, text="Mayoristas", padx=20, command=abrir_mayoristas)
botonmayorstas.pack(pady=20)

botonhoteles = tk.Button(ventana, text="Hoteles", padx=20, command=abrir_hoteles)
botonhoteles.pack(pady=20)

botoncircuitos = tk.Button(ventana, text="Circuitos", padx=20, command=abrir_circuitos)
botoncircuitos.pack(pady=20)

botonvuelos = tk.Button(ventana, text="Vuelos", padx=20, command=abrir_vuelos)
botonvuelos.pack(pady=20)

botonaeropuertos = tk.Button(ventana, text="Aeropuertos", padx=20, command=abrir_aeropuertos)
botonaeropuertos.pack(pady=20)

botonreservas = tk.Button(ventana, text="Reservas", padx=20, command=abrir_reservas)
botonreservas.pack(pady=20)

botonsalir = tk.Button(ventana, text="Salir", padx=20, command=ventana.destroy)
botonsalir.pack(pady=20)

ventana.mainloop()




