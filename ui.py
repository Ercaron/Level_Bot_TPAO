from tkinter import *
from tkinter.messagebox import showinfo
from functools import partial
import threading

window = Tk()
txtTeclaMeditar = StringVar(window)

def mostrarTexto(texto):
    if(len(texto) != 1):
        showinfo("Error", "La tecla debe ser un caracter")
    else :
        print(texto)

class UiBot(threading.Thread):
    PORCENTAJEANCHO = 30
    PORCENTAJEALTO = 25

    def __init__(self):
        super(UiBot, self).__init__()
        self.window = window
        self.txtTeclaMeditar = txtTeclaMeditar

    window.title("Herramienta de Lanzamiento Automático de Hechizos para TPAO")
    window.geometry("1024x720")

    anchoPantalla = window.winfo_screenwidth()
    altoPantalla = window.winfo_screenheight()

    anchoWidget = (PORCENTAJEANCHO * anchoPantalla) / 100
    altoWidghet = (PORCENTAJEALTO * altoPantalla) / 100

    resolucionWidget = str(int(anchoWidget)) + "x" + str(int(altoWidghet))
    window.geometry(resolucionWidget)

    # Primera fila: Titulo de la aplicación
    labelTitulo = Label(window, text="Bienvenido, Sr trolo", anchor='center', font=("Arial Bold", 25))
    labelTitulo.grid(column=1, columnspan=3, row=0)

    # Segunda Fila = Tecla de meditar
    labelMeditar = Label(window, text="Tecla de Meditar", font=("Arial Bold", 18))
    labelMeditar.grid(column=0, row=1)
    txtFieldTeclaMeditar = Entry(window,width=20, textvariable=txtTeclaMeditar)
    txtFieldTeclaMeditar.grid(column=1, row = 1, pady=20, padx = 10)
    botonTeclaMeditar = Button(window, text="Aceptar", width = 20, command=lambda: mostrarTexto(txtTeclaMeditar.get()))
    botonTeclaMeditar.grid(column=2, row=1)

    window.mainloop()

