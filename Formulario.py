from tkinter import *
from tkinter import ttk

class Widgets:        
    def __init__(self, raiz):
        
        raiz.title("Formulario") 
        self.nombre=StringVar()
        self.APaterno= StringVar()
        self.AMaterno= StringVar()
        self.Correo= StringVar()
        self.Movil= StringVar()
        self.Estudiante= StringVar()
        self.Empleado= StringVar()
        self.Desempleado= StringVar()
        self.Leer= StringVar()
        self.Musica= StringVar()
        self.Videojuegos= StringVar()
        self.Guardar= StringVar()
        self.Cancelar= StringVar()
        Estados= StringVar()

        mainFrame = ttk.Frame(raiz, padding="16")
        mainFrame.grid(column=0, row=0, columnspan=4, rowspan=4,sticky=(N, W, E, S))

        nombre_entry=ttk.Entry(mainFrame, width=50, textvariable=self.nombre)
        nombre_entry.grid(column=1,row=0,pady=10, sticky=(N,W,E,S))
        ttk.Label(mainFrame, text="Nombre: " ).grid(column=0, row=0)

        APaterno_entry=ttk.Entry(mainFrame, width=20, textvariable=self.APaterno)
        APaterno_entry.grid(column=1,row=1, pady=10,sticky=(N,W,E,S))
        ttk.Label(mainFrame, text="A. Paterno: " ).grid(column=0, row=1)

        AMaterno_entry=ttk.Entry(mainFrame, width=20, textvariable=self.AMaterno)
        AMaterno_entry.grid(column=1,row=2,pady=10, sticky=(N,W,E,S))
        ttk.Label(mainFrame, text="A. Materno: " ).grid(column=0, row=2)

        Correo_entry=ttk.Entry(mainFrame, width=20, textvariable=self.Correo)
        Correo_entry.grid(column=1,row=3,pady=10, sticky=(N,W,E,S))
        ttk.Label(mainFrame, text="Correo: " ).grid(column=0, row=3)

        Movil_entry=ttk.Entry(mainFrame, width=20, textvariable=self.Movil)
        Movil_entry.grid(column=1,row=4,pady=10, sticky=(N,W,E,S))
        ttk.Label(mainFrame, text="Movil: " ).grid(column=0, row=4)
        
        mainFrame = ttk.Frame(raiz, padding="16")
        mainFrame.grid(column=4, row=4,padx=4 ,sticky=(N, W, E, S))

        Estudiante = ttk.Radiobutton(raiz, text="Estudiante",value=1).grid(column=5, row=1)
        Empleado = ttk.Radiobutton(raiz, text="Empleado",value=2).grid(column=5, row=2)
        Desempleado = ttk.Radiobutton(raiz, text="Desempleado",value=3).grid(column=5, row=3)

        mainFrame = ttk.Frame(raiz, padding="16")
        mainFrame.grid(column=0, row=5,pady=4 ,sticky=(N, W, E, S))
        ttk.Label(mainFrame, text="Aficiones: " ).grid(column=0, row=5)
        Leer = ttk.Checkbutton(raiz, text="Leer")
        Leer.grid(column=0,row=6)
        Musica = ttk.Checkbutton(raiz, text="Musica")
        Musica.grid(column=1,row=6)
        Videojuegos = ttk.Checkbutton(raiz, text="Videojuegos")
        Videojuegos.grid(column=2,row=6)

        mainFrame = ttk.Frame(raiz, padding="30")
        mainFrame.grid(column=0, row=7,sticky=(N, W, E, S))
        Guardar=ttk.Button(mainFrame, text="Guardar").grid(column=0,row=0)
        Cancelar=ttk.Button(mainFrame, text="Cancelar").grid(column=1,row=0)

        mainFrame = ttk.Frame(raiz, padding="20")
        mainFrame.grid(column=5, row=6,sticky=(N, W, E, S))
        Estados=ttk.Combobox(raiz, textvariable=Estados)
        Estados.grid(column=6,row=6)
        Estados['values']=("Jalisco","Nayarit","Colima","Michoacan")
      



raiz=Tk()
Widgets(raiz)
raiz.mainloop()

