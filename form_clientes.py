import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import clientes

class FormularioClientes:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Clientes")
        self.ventana1.state('zoomed') # Maximiza la ventana
        
        self.cliente1=clientes.Clientes()
        self.cuaderno1 = ttk.Notebook(self.ventana1)
           
        self.carga_clientes()
        self.consulta_por_codigo()
        self.listado_completo()
        
        self.cuaderno1.grid(column=0, row=0, padx=100, pady=100)
        self.ventana1.mainloop()

    def carga_clientes(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de clientes")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Cliente")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Nombre:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe1, textvariable=self.nombre)
        self.entrynombre.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Apellido:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.apellido=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe1, textvariable=self.apellido)
        self.entryapellido.grid(column=1, row=1, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="DNI:")        
        self.label2.grid(column=0, row=2, padx=4, pady=4)
        self.dni=tk.StringVar()
        self.entrydni=ttk.Entry(self.labelframe1, textvariable=self.dni)
        self.entrydni.grid(column=1, row=2, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Email:")                
        self.label2.grid(column=0, row=3, padx=4, pady=4)
        self.email=tk.StringVar()
        self.entryemail=ttk.Entry(self.labelframe1, textvariable=self.email)
        self.entryemail.grid(column=1, row=3, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Telefono:")
        self.label2.grid(column=0, row=4, padx=4, pady=4)
        self.telefono=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe1, textvariable=self.telefono)
        self.entrytelefono.grid(column=1, row=4, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)

    def agregar(self):
        datos=(self.nombre.get(), self.apellido.get(), self.dni.get(), self.email.get(), self.telefono.get())
        self.cliente1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.nombre.set("")
        self.apellido.set("")
        self.dni.set("")
        self.email.set("")
        self.telefono.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Cliente")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Nombre:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.nombre=tk.StringVar()
        self.entrynombre=ttk.Entry(self.labelframe2, textvariable=self.nombre, state="readonly")
        self.entrynombre.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Apellido:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.apellido=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe2, textvariable=self.apellido, state="readonly")
        self.entryapellido.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="DNI:")        
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.apellido=tk.StringVar()
        self.entryapellido=ttk.Entry(self.labelframe2, textvariable=self.apellido, state="readonly")
        self.entryapellido.grid(column=1, row=3, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Email:")        
        self.label3.grid(column=0, row=4, padx=4, pady=4)
        self.email=tk.StringVar()
        self.entryemail=ttk.Entry(self.labelframe2, textvariable=self.email, state="readonly")
        self.entryemail.grid(column=1, row=4, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Telefono:")        
        self.label3.grid(column=0, row=5, padx=4, pady=4)
        self.telefono=tk.StringVar()
        self.entrytelefono=ttk.Entry(self.labelframe2, textvariable=self.telefono, state="readonly")
        self.entrytelefono.grid(column=1, row=5, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=6, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.cliente1.consulta(datos)
        if len(respuesta)>0:
            self.nombre.set(respuesta[0][0])
            self.apellido.set(respuesta[0][1])
            self.dni.set(respuesta[0][2])
            self.email.set(respuesta[0][3])
            self.telefono.set(respuesta[0][4])
        else:
            self.nombre.set('')
            self.apellido.set('')
            self.dni.set('')
            self.email.set('')
            self.telefono.set('')
            mb.showinfo("Información", "No existe un cliente con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Cliente")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.cliente1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                      "\nnombre:"+str(fila[1])+
                                      "\napellido:"+str(fila[2])+
                                      "\ndni:"+str(fila[3])+
                                      "\nemail:"+str(fila[4])+
                                      "\ntelefonoo:"+str(fila[5])+
                                      "\n\n")


aplicacion1=FormularioClientes()