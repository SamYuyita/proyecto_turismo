import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import reservas

class FormularioReservas:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Reservas")
        self.ventana1.state('zoomed') # Maximiza la ventana
        self.ventana1.configure(bg='gray')
        
        self.reserva1=reservas.Reservas()
        self.cuaderno1 = ttk.Notebook(self.ventana1)
            
        self.carga_reservas()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        
        self.cuaderno1.grid(column=0, row=0, padx=550, pady=100)
        self.ventana1.mainloop()

    def carga_reservas(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de reservas")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Reservas")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Codigo circuito:")    
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.comboboxcircuito=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxcircuito.grid(column=1, row=0, padx=4, pady=4)
        self.poblar_circuitos()  # Poblar los circuitos en el combobox
        
        self.label2=ttk.Label(self.labelframe1, text="Codigo hotel:")    
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.comboboxhotel=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxhotel.grid(column=1, row=1, padx=4, pady=4)
        self.poblar_hoteles()  # Poblar los hoteles en el combobox
        
        self.label3=ttk.Label(self.labelframe1, text="Codigo vuelo:")    
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.comboboxvuelo=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxvuelo.grid(column=1, row=2, padx=4, pady=4)
        self.poblar_vuelos()  # Poblar los vuelos en el combobox
        
        self.label4=ttk.Label(self.labelframe1, text="Asiento del vuelo:")
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.asientoc=tk.StringVar()
        self.entryasientoc=ttk.Entry(self.labelframe1, textvariable=self.asientoc)
        self.entryasientoc.grid(column=1, row=3, padx=4, pady=4)
        
        self.label5=ttk.Label(self.labelframe1, text="Fecha:")    
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.fechac=tk.StringVar()
        self.entryfechac=ttk.Entry(self.labelframe1, textvariable=self.fechac)
        self.entryfechac.grid(column=1, row=4, padx=4, pady=4)
        
        self.label6=ttk.Label(self.labelframe1, text="Codigo cliente:")    
        self.label6.grid(column=0, row=5, padx=4, pady=4)
        self.comboboxdni=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxdni.grid(column=1, row=5, padx=4, pady=4)
        self.poblar_clientes()  # Poblar los DNIs en el combobox
        
        self.label7=ttk.Label(self.labelframe1, text="Codigo agencia:")    
        self.label7.grid(column=0, row=6, padx=4, pady=4)
        self.comboboxagencia=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxagencia.grid(column=1, row=6, padx=4, pady=4)
        self.poblar_agencias()  # Poblar las agencias en el combobox
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=7, padx=4, pady=4)
    
    def poblar_circuitos(self):
        circuitos = self.reserva1.obtener_circuitos()  # Obtener lista de circuitos desde reservas
        self.comboboxcircuito['values'] = circuitos
        
    def poblar_hoteles(self):
        hoteles = self.reserva1.obtener_hoteles()  # Obtener lista de hoteles desde reservas
        self.comboboxhotel['values'] = hoteles
    
    def poblar_vuelos(self):
        vuelos = self.reserva1.obtener_vuelos()  # Obtener lista de vuelos desde reservas
        self.comboboxvuelo['values'] = vuelos
        
    def poblar_clientes(self):
        clientes = self.reserva1.obtener_clientes()  # Obtener lista de clientes desde reservas
        self.comboboxdni['values'] = clientes
        
    def poblar_agencias(self):
        agencias = self.reserva1.obtener_agencias()  # Obtener lista de agencias desde reservas
        self.comboboxagencia['values'] = agencias

    def agregar(self):
        datos=(self.comboboxcircuito.get(), self.comboboxhotel.get(), self.comboboxvuelo.get(), self.asientoc.get(), self.fechac.get(), self.comboboxdni.get(), self.comboboxagencia.get())
        self.reserva1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.comboboxcircuito.set("")
        self.comboboxhotel.set("")
        self.comboboxvuelo.set("")
        self.asientoc.set("")
        self.fechac.set("")
        self.comboboxdni.set("")
        self.comboboxagencia.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Reservas")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Asiento del vuelo:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cantemp=tk.StringVar()
        self.entrycantemp=ttk.Entry(self.labelframe2, textvariable=self.cantemp, state="readonly")
        self.entrycantemp.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Fecha:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.direccion=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe2, textvariable=self.direccion, state="readonly")
        self.entrydireccion.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.reserva1.consulta(datos)
        if len(respuesta)>0:
            self.cantemp.set(respuesta[0][0])
            self.direccion.set(respuesta[0][1])
        else:
            self.cantemp.set('')
            self.direccion.set('')
            mb.showinfo("Información", "No existe una reserva con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Reservas")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.reserva1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])
                                      +"\nasiento del vuelo:"+str(fila[1])
                                      +"\nfecha:"+str(fila[2])+"\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar reserva")
        
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Reserva")        
        self.labelframe4.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe4, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe4, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe4, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.reserva1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró la reserva con dicho código")
        else:
            mb.showinfo("Información", "No existe una reserva con dicho código")

aplicacion1=FormularioReservas()