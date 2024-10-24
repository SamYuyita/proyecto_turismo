import tkinter as tk
import os

def abrir_clientes():
    os.system('python 1form_clientes.py')

def abrir_agencias():
    os.system('python 2form_agencias.py')
    
def abrir_mayoristas():
    os.system('python 3form_mayoristas.py')

def abrir_reservas():
    os.system('python 4form_reservas.py')

def abrir_hoteles():
    os.system('python 5form_hoteles.py')
    
def abrir_circuitos():
    os.system('python 6form_circuitos.py')
    
def abrir_vuelos():
    os.system('python 7form_vuelos.py')
    
def abrir_aeropuertos():
    os.system('python 8form_aeropuertos.py')

ventana = tk.Tk()
ventana.title("Agencia de turismo")
ventana.state('zoomed')

etiqueta=tk.Label(ventana, text="Agencia de turismo", font=("Helvetica", 20, "bold"))
etiqueta.pack(pady=50)

botonclientes = tk.Button(ventana, text="Clientes", padx=20, command=abrir_clientes)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Agencias", padx=20, command=abrir_agencias)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Mayoristas", padx=20, command=abrir_mayoristas)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Reservas", padx=20, command=abrir_reservas)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Hoteles", padx=20, command=abrir_hoteles)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Circuitos", padx=20, command=abrir_circuitos)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Vuelos", padx=20, command=abrir_vuelos)
botonclientes.pack(pady=20)

botonclientes = tk.Button(ventana, text="Aeropuertos", padx=20, command=abrir_aeropuertos)
botonclientes.pack(pady=20)

ventana.mainloop()




