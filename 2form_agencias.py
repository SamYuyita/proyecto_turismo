import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import agencias

class FormularioAgencias:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Agencias")
        self.ventana1.state('zoomed') # Maximiza la ventana
        self.ventana1.configure(bg='gray')
        
        self.agencia1=agencias.Agencias()
        self.cuaderno1 = ttk.Notebook(self.ventana1)
            
        self.carga_agencias()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        
        self.cuaderno1.grid(column=0, row=0, padx=550, pady=100)
        self.ventana1.mainloop()

    def carga_agencias(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de agencias")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Agencia")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Cantidad de empleados:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.cantempc=tk.StringVar()
        self.entrycantempc=ttk.Entry(self.labelframe1, textvariable=self.cantempc)
        self.entrycantempc.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Direccion:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.direccionc=tk.StringVar()
        self.entrydireccionc=ttk.Entry(self.labelframe1, textvariable=self.direccionc)
        self.entrydireccionc.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="Codigo mayorista:")    
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.comboboxmayorista=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxmayorista.grid(column=1, row=2, padx=4, pady=4)
        self.poblar_mayoristas()  # Poblar las mayoristas en el combobox
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        
    def poblar_mayoristas(self):
        mayoristas = self.agencia1.obtener_mayoristas()  # Obtener lista de mayorista desde agencias
        self.comboboxmayorista['values'] = mayoristas

    def agregar(self):
        datos=(self.cantempc.get(), self.direccionc.get())
        self.agencia1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.cantempc.set("")
        self.direccionc.set("")
        
    def agregar_mayorista(self):
        datosmayo=(self.comboboxmayorista.get())
        mb.showinfo("Información", "Los datos fueron cargados")
        self.agencia1.alta_mayo(datosmayo)
        self.comboboxmayorista.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Agencia")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Cantidad de empleados:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.cantemp=tk.StringVar()
        self.entrycantemp=ttk.Entry(self.labelframe2, textvariable=self.cantemp, state="readonly")
        self.entrycantemp.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Direccion:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.direccion=tk.StringVar()
        self.entrydireccion=ttk.Entry(self.labelframe2, textvariable=self.direccion, state="readonly")
        self.entrydireccion.grid(column=1, row=2, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.agencia1.consulta(datos)
        if len(respuesta)>0:
            self.cantemp.set(respuesta[0][0])
            self.direccion.set(respuesta[0][1])
        else:
            self.cantemp.set('')
            self.direccion.set('')
            mb.showinfo("Información", "No existe una agencia con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Agencia")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.agencia1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])
                                      +"\ncantidad de empleados:"+str(fila[1])
                                      +"\ndireccion:"+str(fila[2])+"\n\n")
            
    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar agencia")
        
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Agencia")        
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
        cantidad=self.agencia1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró la agencia con dicho código")
        else:
            mb.showinfo("Información", "No existe una agencia con dicho código")

aplicacion1=FormularioAgencias()