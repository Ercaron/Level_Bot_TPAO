import tkinter as tk
import os
import threading
import ui as ui
from tkinter.messagebox import showinfo
import Chinese as ch
from pynput.mouse import Button, Controller


NOMBREARCHIVO = "configuracion.txt"

class InitScreen(tk.Frame):
    def __init__(self):
        self.window = tk.Tk()
        self.inicializar()

    def abrirVentanaConfigurar(self):
       uiIngresarDatos = ui.UiBot(self.window)
       self.window.withdraw()
       uiIngresarDatos.start()

    def existeArchivo(self):
        return os.path.isfile(NOMBREARCHIVO)

    def obtenerValue(self,line):
        return (line.split("=")[1]).strip()

    def validarTeclaMeditar(self,txtMeditar):
        if(len(txtMeditar) == 0):
            showinfo("Error", "Debe ingresar un caracter para la Tecla de Meditación")
            return False
        elif len(txtMeditar) != 1 :
            showinfo("Error", "La tecla de meditación debe ser un único caracter")
            return False
        else :
            return True

    def validarPosicion(self,posX, posY):
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

    def comenzarEjecucionPrograma(self,txtMeditar,txtPosX, txtPosY):
        button = Button.left
        self.window.destroy()
        click_thread = ch.ClickMouse(button,txtMeditar,txtPosX,txtPosY)
        ch.start(click_thread)

    def abrirArchivo(self):
        if(self.existeArchivo()):
            archivo = open(NOMBREARCHIVO,"r")
            filaTeclaMeditar = archivo.readline()
            filaPosX = archivo.readline()
            filaPosY = archivo.readline()
            teclaMeditar = self.obtenerValue(filaTeclaMeditar)
            posX = self.obtenerValue(filaPosX)
            posY = self.obtenerValue(filaPosY)
            if(self.validarTeclaMeditar(teclaMeditar)):
                if(self.validarPosicion(posX,posY)):
                    self.comenzarEjecucionPrograma(teclaMeditar,posX,posY)
        else :
            showinfo("Error", "El archivo de configuración no existe. Tocá el botón Configurar")      

    def centrarPantalla(self):
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def inicializar(self):
        self.window.title("Herramienta de Lanzamiento Automático de Hechizos para TPAO")
        self.window.geometry("1024x720")
        self.centrarPantalla()

        labelTitulo = tk.Label(self.window, text="WC Bot", anchor='center', font=("Arial Bold", 25))
        labelTitulo.place(relx= 0.5, rely = 0.1, anchor="center")

        botonConfigurar = tk.Button(self.window, width = 20, text="Configurar", command=self.abrirVentanaConfigurar)
        botonConfigurar.place(relx= 0.5, rely = 0.4, anchor="center")

        botonIniciar = tk.Button(self.window, width = 20, text="Iniciar", command=self.abrirArchivo)
        botonIniciar.place(relx= 0.5, rely = 0.7, anchor="center")

        self.window.mainloop()




