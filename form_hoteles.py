import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import hoteles

class FormularioHoteles:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Hoteles")
        self.ventana1.state('zoomed') # Maximiza la ventana
        
        self.hotel1=hoteles.Hoteles()
        self.cuaderno1 = ttk.Notebook(self.ventana1)      
          
        self.carga_hoteles()
        self.consulta_por_codigo()
        self.listado_completo()
        
        self.cuaderno1.grid(column=0, row=0, padx=10, pady=10)
        self.ventana1.mainloop()

    def carga_hoteles(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de hoteles")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Hoteles")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Descripción:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcionc=tk.StringVar()
        self.entrydescripcionc=ttk.Entry(self.labelframe1, textvariable=self.descripcionc)
        self.entrydescripcionc.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Cantidad de habitaciones:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.canthabc=tk.StringVar()
        self.entrycanthabc=ttk.Entry(self.labelframe1, textvariable=self.canthabc)
        self.entrycanthabc.grid(column=1, row=1, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.descripcionc.get(), self.canthabc.get())
        self.hotel1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcionc.set("")
        self.canthabc.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Hotel")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcion=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2, textvariable=self.descripcion, state="readonly")
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Cantidad de habitaciones:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.canthab=tk.StringVar()
        self.entrycanthab=ttk.Entry(self.labelframe2, textvariable=self.canthab, state="readonly")
        self.entrycanthab.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.hotel1.consulta(datos)
        if len(respuesta)>0:
            self.descripcion.set(respuesta[0][0])
            self.canthab.set(respuesta[0][1])
        else:
            self.descripcion.set('')
            self.canthab.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Hotel")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.hotel1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])
                                      +"\ndescripción:"+str(fila[1])
                                      +"\ncantidadhabitaciones:"+str(fila[2])+"\n\n")


aplicacion1=FormularioHoteles()