import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import mayoristas

class FormularioMayoristas:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Mayoristas")
        self.ventana1.state('zoomed') # Maximiza la ventana
        
        self.mayorista1=mayoristas.Mayoristas()
        self.cuaderno1 = ttk.Notebook(self.ventana1)
            
        self.carga_mayoristas()
        self.consulta_por_codigo()
        self.listado_completo()
        
        self.cuaderno1.grid(column=0, row=0, padx=550, pady=100)
        self.ventana1.mainloop()

    def carga_mayoristas(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de mayoristas")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Mayorista")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cantempc=tk.StringVar()
        self.entrycantempc=ttk.Entry(self.labelframe1, textvariable=self.cantempc)
        self.entrycantempc.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Facturacion anual:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.direccionc=tk.StringVar()
        self.entrydireccionc=ttk.Entry(self.labelframe1, textvariable=self.direccionc)
        self.entrydireccionc.grid(column=1, row=1, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)

    def agregar(self):
        datos=(self.cantempc.get(), self.direccionc.get())
        self.mayorista1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.cantempc.set("")
        self.direccionc.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Mayoristas")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Nombre:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cantemp=tk.StringVar()
        self.entrycantemp=ttk.Entry(self.labelframe2, textvariable=self.cantemp, state="readonly")
        self.entrycantemp.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Facturacion anual:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.direccion=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe2, textvariable=self.direccion, state="readonly")
        self.entrydireccion.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.mayorista1.consulta(datos)
        if len(respuesta)>0:
            self.cantemp.set(respuesta[0][0])
            self.direccion.set(respuesta[0][1])
        else:
            self.cantemp.set('')
            self.direccion.set('')
            mb.showinfo("Información", "No existe un mayorista con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Mayorista")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.mayorista1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])
                                      +"\nnombre:"+str(fila[1])
                                      +"\nfacturacion anual:"+str(fila[2])+"\n\n")


aplicacion1=FormularioMayoristas()