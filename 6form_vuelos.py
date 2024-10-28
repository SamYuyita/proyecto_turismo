import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import vuelos

class FormularioVuelos:
    
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("Vuelos")
        self.ventana1.state('zoomed') # Maximiza la ventana
        self.ventana1.configure(bg='gray')
        
        self.vuelo1=vuelos.Vuelos()
        self.cuaderno1 = ttk.Notebook(self.ventana1)
           
        self.carga_vuelos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        
        self.cuaderno1.grid(column=0, row=0, padx=550, pady=100)
        self.ventana1.mainloop()

    def carga_vuelos(self):
        self.pagina1 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1, text="Carga de vuelos")
        
        self.labelframe1=ttk.LabelFrame(self.pagina1, text="Vuelos")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe1, text="Descripcion:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.descripcionc=tk.StringVar()
        self.entrydescripcionc=ttk.Entry(self.labelframe1, textvariable=self.descripcionc)
        self.entrydescripcionc.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe1, text="Hora:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.horac=tk.StringVar()
        self.entryhorac=ttk.Entry(self.labelframe1, textvariable=self.horac)
        self.entryhorac.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe1, text="N de asiento:")
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.asientoc=tk.StringVar()
        self.entryasientoc=ttk.Entry(self.labelframe1, textvariable=self.asientoc)
        self.entryasientoc.grid(column=1, row=2, padx=4, pady=4)
        
        self.label4=ttk.Label(self.labelframe1, text="Codigo ap salida:")    
        self.label4.grid(column=0, row=3, padx=4, pady=4)
        self.comboboxaps=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxaps.grid(column=1, row=3, padx=4, pady=4)
        self.poblar_aeropuertos_salida()  # Poblar los aeropuertos en el combobox
        
        self.label5=ttk.Label(self.labelframe1, text="Codigo ap destino:")    
        self.label5.grid(column=0, row=4, padx=4, pady=4)
        self.comboboxapd=ttk.Combobox(self.labelframe1, state="readonly")
        self.comboboxapd.grid(column=1, row=4, padx=4, pady=4)
        self.poblar_aeropuertos_destino()
        
        self.boton1=ttk.Button(self.labelframe1, text="Confirmar", command=self.agregar)
        self.boton1.grid(column=1, row=5, padx=4, pady=4)
        
    def poblar_aeropuertos_salida(self):
        aeropuertos = self.vuelo1.obtener_aeropuertos()  # Obtener lista de aeropuertos desde reservas
        self.comboboxaps['values'] = aeropuertos
        
    def poblar_aeropuertos_destino(self):
        aeropuertos = self.vuelo1.obtener_aeropuertos()  # Obtener lista de aeropuertos desde reservas
        self.comboboxapd['values'] = aeropuertos

    def agregar(self):
        datos=(self.descripcionc.get(), self.horac.get(), self.asientoc.get())
        self.vuelo1.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcionc.set("")
        self.horac.set("")
        self.asientoc.set("")

    def consulta_por_codigo(self):
        self.pagina2 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2, text="Consulta por código")
        
        self.labelframe2=ttk.LabelFrame(self.pagina2, text="Vuelos")
        self.labelframe2.grid(column=0, row=0, padx=5, pady=10)
        
        self.label1=ttk.Label(self.labelframe2, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigo=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2, textvariable=self.codigo)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        
        self.label2=ttk.Label(self.labelframe2, text="Descripcion:")
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcioncons=tk.StringVar()
        self.entrydescripcioncons=ttk.Entry(self.labelframe2, textvariable=self.descripcioncons, state="readonly")
        self.entrydescripcioncons.grid(column=1, row=1, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="Hora:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.horacons=tk.StringVar()
        self.entryhoracons=ttk.Entry(self.labelframe2, textvariable=self.horacons, state="readonly")
        self.entryhoracons.grid(column=1, row=2, padx=4, pady=4)
        
        self.label3=ttk.Label(self.labelframe2, text="N de asiento:")        
        self.label3.grid(column=0, row=3, padx=4, pady=4)
        self.asientocons=tk.StringVar()
        self.entryasientocons=ttk.Entry(self.labelframe2, textvariable=self.asientocons, state="readonly")
        self.entryasientocons.grid(column=1, row=3, padx=4, pady=4)
        
        self.boton1=ttk.Button(self.labelframe2, text="Consultar", command=self.consultar)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def consultar(self):
        datos=(self.codigo.get(), )
        respuesta=self.vuelo1.consulta(datos)
        if len(respuesta)>0:
            self.descripcioncons.set(respuesta[0][0])
            self.horacons.set(respuesta[0][1])
            self.asientocons.set(respuesta[0][2])
        else:
            self.descripcioncons.set('')
            self.horacons.set('')
            self.asientocons.set('')
            mb.showinfo("Información", "No existe un vuelo con dicho código")

    def listado_completo(self):
        self.pagina3 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3, text="Listado completo")
        
        self.labelframe3=ttk.LabelFrame(self.pagina3, text="Vuelos")
        self.labelframe3.grid(column=0, row=0, padx=5, pady=10)
        
        self.boton1=ttk.Button(self.labelframe3, text="Listado completo", command=self.listar)
        self.boton1.grid(column=0, row=0, padx=4, pady=4)
        self.scrolledtext1=st.ScrolledText(self.labelframe3, width=30, height=10)
        self.scrolledtext1.grid(column=0,row=1, padx=10, pady=10)

    def listar(self):
        respuesta=self.vuelo1.recuperar_todos()
        self.scrolledtext1.delete("1.0", tk.END)        
        for fila in respuesta:
            self.scrolledtext1.insert(tk.END, "código:"+str(fila[0])+
                                      "\ndescripcion:"+str(fila[1])+
                                      "\nhora:"+str(fila[2])+
                                      "\nN de asiento:"+str(fila[3])+
                                      "\n\n")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de vuelos")
        
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Vuelo")        
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
        cantidad=self.vuelo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el vuelo con dicho código")
        else:
            mb.showinfo("Información", "No existe un vuelo con dicho código")

    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrar vuelo")
        
        self.labelframe4=ttk.LabelFrame(self.pagina4, text="Vuelo")        
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
        cantidad=self.vuelo1.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el vuelo con dicho código")
        else:
            mb.showinfo("Información", "No existe un vuelo con dicho código")

aplicacion1=FormularioVuelos()