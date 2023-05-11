#Juan de Jesus Tovar Reyes 09/03/2023
from tkinter import *
from tkinter import ttk
from tkinter import Tk
import tkinter as tk
import csv

class Muestra_Widgets:
    def __init__(self):

    
        self.raiz = Tk()

        self.raiz.title("Muestra de Widgets")

        self.Nombre = StringVar()
        self.A_Paterno = StringVar()
        self.A_Materno = StringVar()
        self.Correo = StringVar()
        self.Movil = StringVar()

        #Frames
        frame = ttk.Frame(self.raiz, padding="40 40 40 40", relief="raised")
        frame.grid(column=0, row=0)
        frame2 = ttk.Frame(frame, padding="15 15", relief="raised")
        frame2.grid(column=0, row=0)
        frame3 = ttk.Frame(frame, padding="15 15", relief="raised")
        frame3.grid(column=0, row= 2, pady=30)
        frame4 = ttk.Frame(frame, padding="15 15")
        frame4.grid(column=1, row= 0)
        frame5 = ttk.Frame(frame, padding="15 15")
        frame5.grid(column=0,row=3)



        #Etiquetas
        ttk.Label(frame2, text="Nombre: ").grid(column=0, row=1, sticky=W)
        ttk.Label(frame2, text="").grid(column= 0, row= 2, columnspan=2)
        ttk.Label(frame2, text="").grid(column= 1, row= 2, columnspan=2)
        ttk.Label(frame2, text="A. Paterno: ").grid(column=0, row=3, sticky=W)
        ttk.Label(frame2, text="").grid(column= 0, row= 4, columnspan=2)
        ttk.Label(frame2, text="").grid(column= 1, row= 4, columnspan=2)
        ttk.Label(frame2, text="A. Materno: ").grid(column=0, row=5, sticky=W)
        ttk.Label(frame2, text="").grid(column= 0, row= 6, columnspan=2)
        ttk.Label(frame2, text="").grid(column= 1, row= 6, columnspan=2)
        ttk.Label(frame2, text="Correo: ").grid(column=0, row=7, sticky=W)
        ttk.Label(frame2, text="").grid(column= 0, row= 8, columnspan=2)
        ttk.Label(frame2, text="").grid(column= 1, row= 8, columnspan=2)
        ttk.Label(frame2, text="Movil: ").grid(column=0, row=9, sticky=W)

        
        #Entrys
        self.NombreEntry = ttk.Entry(frame2, width=30,textvariable=self.Nombre)
        self.NombreEntry.grid( column= 1 , row= 1, columnspan=2)
        self.A_PaternoEntry= ttk.Entry(frame2, width=30,textvariable=self.A_Paterno)
        self.A_PaternoEntry.grid( column= 1 , row= 3, columnspan=2)
        self.A_MaternoEntry= ttk.Entry(frame2, width=30,textvariable=self.A_Materno)
        self.A_MaternoEntry.grid( column= 1 , row= 5, columnspan=2)
        self.CorreoEntry= ttk.Entry(frame2, width=30,textvariable=self.Correo)
        self.CorreoEntry.grid( column= 1 , row= 7, columnspan=2)
        self.MovilEntry= ttk.Entry(frame2, width=30,textvariable=self.Movil)
        self.MovilEntry.grid( column= 1 , row= 9, columnspan=2)

        #CheckButton
        self.Afi = StringVar()
        self.Afi2 = StringVar()
        self.Afi3= StringVar()
        ttk.Label(frame3, text="Aficiones:").grid(column=1, row=0,sticky=W)
        chkBoton = ttk.Checkbutton(frame3, text="Leer",variable=self.Afi)
        chkBoton.grid(column=1,row=1)
        ttk.Label(frame3, text="    ").grid(column= 2, row= 1)
        chkBoton = ttk.Checkbutton(frame3, text="Musica",variable=self.Afi2)
        chkBoton.grid(column=3,row=1)
        ttk.Label(frame3, text="    ").grid(column= 4, row= 1)
        chkBoton = ttk.Checkbutton(frame3, text="Videojuegos",variable=self.Afi3)
        chkBoton.grid(column=5,row=1)

        #RadioButton
        self.Ocupacion = StringVar()
        Estudiante = ttk.Radiobutton(frame4,text='Estudiante',variable=self.Ocupacion,value="Estudiante", compound="center").grid(column=0, row=1, sticky=W)
        Empleado = ttk.Radiobutton(frame4,text='Empleado',variable=self.Ocupacion,value="Empleado",compound="center").grid(column=0, row=2, sticky=W)
        Desempleado = ttk.Radiobutton(frame4,text='Desempleado',variable=self.Ocupacion,value="Desempleado",compound="center").grid(column=0, row=3, sticky=W)

        #Combobox
        self.Estado = StringVar()

        tituloestados = Label(frame, text="Estado").grid(column= 1, row= 1,sticky=S,pady=0)
        comboEstados = ttk.Combobox(frame, textvariable=self.Estado)
        comboEstados.grid(column= 1, row=2, sticky=N)
        comboEstados['values']=("Jalisco","Zacatecas","Colima","Tlaxcala")

        #Botones Finales
        button = ttk.Button(frame5, text="Guardar", command=self.guardar_datos)
        button.grid(column=0,row=0)
        ttk.Label(frame5, text="                    ").grid(column= 1, row= 0)
        button2 = ttk.Button(frame5, text="Cerrar",command=self.cerrar_ventana)
        button2.grid(column=2,row=0)
        cancelar=ttk.Button(frame5,text="Ver datos",command=self.ver_datos)
        cancelar.grid(column=2, row=5, sticky=(W))

        self.raiz.mainloop()
    def guardar_datos(self):
    
            nombre1 = self.Nombre.get()
            A_Paterno1 = self.A_Paterno.get()
            A_Materno1 = self.A_Materno.get()
            Correo1 = self.Correo.get() 
            Movil1 = self.Movil.get()

            Aficiones = self.Afi.get()
            Aficiones2 = self.Afi2.get()
            Aficiones3 = self.Afi3.get()

            Estado1 = self.Estado.get()

            Ocupacion = self.Ocupacion.get()

            with open("datos.csv", mode="a", newline="") as archivo:

            # Abrimos el archivo en modo escritura
                escritor = csv.writer(archivo)
            # Si el archivo está vacío escribimos la primera línea con los encabezados
                if archivo.tell() == 0:
                    escritor.writerow(['Nombre','A_paterno','A_materno','Correo','Movil','Leer','Musica','Videojuegos','Estado','Ocupacion'])
            # Escribimos los datos del formulario en una nueva línea
                escritor.writerow([nombre1, A_Paterno1, A_Materno1, Correo1, Movil1, Aficiones, Aficiones2, Aficiones3, Estado1, Ocupacion])
        
        #Borrar espacios
            self.NombreEntry.delete(0,"end")
            self.A_PaternoEntry.delete(0,"end")
            self.A_MaternoEntry.delete(0,"end")
            self.CorreoEntry.delete(0,"end")
            self.MovilEntry.delete(0,"end")

            self.Afi.set(False)
            self.Afi2.set(False)
            self.Afi3.set(False)

            self.Estado.set("Estados")
            
            self.Ocupacion.set("")

    def cerrar_ventana(self):
        self.raiz.destroy()


    def ver_datos(self):
        ventana = Toplevel(self.raiz)
        ventana.title("Datos almacenados")
        
        with open("datos.csv", mode="r") as archivo:
            lector = csv.reader(archivo)

            # Creamos la tabla utilizando un LabelFrame y Labels
            table_frame = ttk.LabelFrame(ventana, text='Datos')
            table_frame.pack(fill=BOTH, expand=1, padx=5, pady=5)

            row_num = 0
            for row in lector:
                label_1 = ttk.Label(table_frame, text=row[0], width=20, borderwidth=1, relief='solid')
                label_1.grid(row=row_num, column=0)
                
                label_2 = ttk.Label(table_frame, text=row[1], width=20, borderwidth=1, relief='solid')
                label_2.grid(row=row_num, column=1)
                
                label_3 = ttk.Label(table_frame, text=row[2], width=20, borderwidth=1, relief='solid')
                label_3.grid(row=row_num, column=2)

                label_4 = ttk.Label(table_frame, text=row[3], width=20, borderwidth=1, relief='solid')
                label_4.grid(row=row_num, column=3)
                
                label_5 = ttk.Label(table_frame, text=row[4], width=20, borderwidth=1, relief='solid')
                label_5.grid(row=row_num, column=4)
                
                label_6 = ttk.Label(table_frame, text=row[5], width=20, borderwidth=1, relief='solid')
                label_6.grid(row=row_num, column=5)

                label_7 = ttk.Label(table_frame, text=row[6], width=20, borderwidth=1, relief='solid')
                label_7.grid(row=row_num, column=6)
                
                label_8 = ttk.Label(table_frame, text=row[7], width=20, borderwidth=1, relief='solid')
                label_8.grid(row=row_num, column=7)
                
                label_9 = ttk.Label(table_frame, text=row[8], width=20, borderwidth=1, relief='solid')
                label_9.grid(row=row_num, column=8)

                label_10 = ttk.Label(table_frame, text=row[9], width=20, borderwidth=1, relief='solid')
                label_10.grid(row=row_num, column=9)

                row_num += 1


Muestra_Widgets()