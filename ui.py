import threading
import os
import tkinter as tk
#import Chinese as ch
from tkinter.messagebox import showinfo
from functools import partial



NOMBREARCHIVO = "configuracion.txt"
window = tk.Tk()
txtTeclaMeditar = tk.StringVar(window)
txtPosicionX = tk.StringVar(window)
txtPosicionY = tk.StringVar(window)

def abrirArchivo():
    if(os.path.isfile(NOMBREARCHIVO)):
        file = open(NOMBREARCHIVO,"r")
        return file
    else :
        file = open(NOMBREARCHIVO,"w")
        file.write("TECLA_MEDITAR= \n")
        file.write("POSICION_LANZAR_X= \n")
        file.write("POSICION_LANZAR_Y= \n")
        return file

def escribirArchivo(teclaMeditar, posX, posY):
    nuevaTeclaMeditar="TECLA_MEDITAR=" + teclaMeditar + "\n"
    nuevaPosX="POSICION_LANZAR_X=" + posX + "\n"
    nuevaPosY="POSICION_LANZAR_Y=" + posY + "\n"
    file = open(NOMBREARCHIVO,"w")
    file.write(nuevaTeclaMeditar)
    file.write(nuevaPosX)
    file.write(nuevaPosY)
    file.close()
    showinfo("Éxito", "Información guardada satisfactoriamente")

def validarTeclaMeditar(txtMeditar):
    if(len(txtMeditar) == 0):
        showinfo("Error", "Debe ingresar un caracter para la Tecla de Meditación")
        return False
    elif len(txtMeditar) != 1 :
        showinfo("Error", "La tecla de meditación debe ser un único caracter")
        return False
    else :
        return True

def validarPosicion(posX, posY):

    try:
        int(posX)
        int(posY)
    except ValueError:
        showinfo("Error", "Las posiciones deben ser numéricas")
        return False

    posicionX = int(posX)
    posicionY = int(posY)
    if(posicionX < 0 or posicionX > 1920):
        showinfo("Error", "La posición en X debe ser un número entre 0 y 1920")
        return False
    
    if(posicionY < 0 or posicionY > 1080):
        showinfo("Error", "La posición en Y debe ser un número entre 0 y 1080")
        return False

    return True

#def comenzarEjecucionPrograma(txtMeditar,txtPosX, txtPosY):
    #button = pynput.Button.left
    #click_thread = ch.ClickMouse(button,txtMeditar,txtPosX,txtPosY)
    #click_thread.start()
            
def validarInput(txtMeditar, txtPosX, txtPosY):
    if(validarTeclaMeditar(txtMeditar)) :
        if(validarPosicion(txtPosX, txtPosY)):
            escribirArchivo(txtMeditar,txtPosX,txtPosY)
            #comenzarEjecucionPrograma(txtMeditar, txtPosX, txtPosY)

class UiBot(threading.Thread):

    def __init__(self):
        super(UiBot, self).__init__()
        self.window = window
        self.txtTeclaMeditar = txtTeclaMeditar
        self.txtPosicionX = txtPosicionX
        self.txtPosicionY = txtPosicionY

    window.title("Herramienta de Lanzamiento Automático de Hechizos para TPAO")
    window.geometry("1024x720")

    PORCENTAJEANCHO = 35
    PORCENTAJEALTO = 25

    anchoPantalla = window.winfo_screenwidth()
    altoPantalla = window.winfo_screenheight()

    anchoWidget = (PORCENTAJEANCHO * anchoPantalla) / 100
    altoWidghet = (PORCENTAJEALTO * altoPantalla) / 100

    resolucionWidget = str(int(anchoWidget)) + "x" + str(int(altoWidghet))
    window.geometry(resolucionWidget)

    # Primera fila: Titulo de la aplicación
    labelTitulo = tk.Label(window, text="Bienvenido, Sr trolo", anchor='center', font=("Arial Bold", 25))
    labelTitulo.grid(column=0, columnspan=3, row=0)

    # Segunda Fila = Tecla de meditar
    labelMeditar = tk.Label(window, text="Tecla de Meditar", font=("Arial Bold", 18))
    labelMeditar.grid(column=0, row=1)
    txtFieldTeclaMeditar = tk.Entry(window,width=20, textvariable=txtTeclaMeditar)
    txtFieldTeclaMeditar.grid(column=1, row = 1, pady=20, padx = 10)

    # Tercera fila = Posición X e Y
    labelPosicionX = tk.Label(window, text="Posición Horizontal", font=("Arial Bold", 18))
    labelPosicionX.grid(column=0 , row=2)
    txtFieldPosicionX = tk.Entry(window, width = 20, textvariable=txtPosicionX)
    txtFieldPosicionX.grid(column=1, row = 2, pady = 20)

    labelPosicionY = tk.Label(window, text="Posicion Vertical", font=("Arial Bold",18))
    labelPosicionY.grid(column=2, row=2)
    txtFieldPosicionY = tk.Entry(window, width=20, textvariable=txtPosicionY)
    txtFieldPosicionY.grid(column=3, row=2, pady=20)

    # Cuarta fila = Boton aceptar

    botonAceptar = tk.Button(window, width = 20, text="Aceptar", command=lambda: validarInput(txtTeclaMeditar.get(), txtPosicionX.get(), txtPosicionY.get()))
    botonAceptar.grid(column=1, columnspan=2, row=3)

    window.mainloop()



