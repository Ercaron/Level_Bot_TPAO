import threading
import os
import tkinter as tk
import Chinese as ch
from pynput.mouse import Button, Controller
from tkinter.messagebox import showinfo
from functools import partial

NOMBREARCHIVO = "configuracion.txt"
PORCENTAJEANCHO = 35
PORCENTAJEALTO = 25

class UiBot(tk.Frame):

    def __init__(self, master):
        self.master = master
        self.window = tk.Toplevel()
        self.txtTeclaMeditar = tk.StringVar(self.window)
        self.txtPosicionX = tk.StringVar(self.window)
        self.txtPosicionY = tk.StringVar(self.window)


    def abrirArchivo(self):
        if(os.path.isfile(NOMBREARCHIVO)):
            file = open(NOMBREARCHIVO,"r")
            return file
        else :
            file = open(NOMBREARCHIVO,"w")
            file.write("TECLA_MEDITAR= \n")
            file.write("POSICION_LANZAR_X= \n")
            file.write("POSICION_LANZAR_Y= \n")
            return file

    def escribirArchivo(self,teclaMeditar, posX, posY):
        nuevaTeclaMeditar="TECLA_MEDITAR=" + teclaMeditar + "\n"
        nuevaPosX="POSICION_LANZAR_X=" + posX + "\n"
        nuevaPosY="POSICION_LANZAR_Y=" + posY + "\n"
        file = open(NOMBREARCHIVO,"w")
        file.write(nuevaTeclaMeditar.strip())
        file.write(nuevaPosX.strip())
        file.write(nuevaPosY.strip())
        file.close()
        showinfo("Éxito", "Información guardada satisfactoriamente")

    def validarTeclaMeditar(self,txtMeditar):
        if(len(txtMeditar) == 0):
            showinfo("Error", "Debe ingresar un caracter para la Tecla de Meditación")
            return False
        elif len(txtMeditar) != 1 :
            showinfo("Error", "La tecla de meditación debe ser un único caracter")
            return False
        else :
            return True

    def comenzarEjecucionPrograma(self,txtMeditar,txtPosX, txtPosY):
        button = Button.left
        self.master.destroy()
        click_thread = ch.ClickMouse(button,txtMeditar,txtPosX,txtPosY)
        ch.start(click_thread)

    def validarInput(self):
        txtMeditar = self.txtTeclaMeditar.get()
        txtPosX = self.txtPosicionX.get()
        txtPosY = self.txtPosicionY.get()
        if(self.validarTeclaMeditar(txtMeditar)) :
            if(self.validarPosicion(txtPosX, txtPosY)):
                self.escribirArchivo(txtMeditar,txtPosX,txtPosY)
                self.comenzarEjecucionPrograma(txtMeditar, txtPosX, txtPosY)

    def obtenerValue(self,line):
        return (line.split("=")[1]).strip()

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

    def centrarPantalla(self):
        w = self.window.winfo_reqwidth()
        h = self.window.winfo_reqheight()
        ws = self.window.winfo_screenwidth()
        hs = self.window.winfo_screenheight()
        x = (ws/2) - (w/2)
        y = (hs/2) - (h/2)
        self.window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def start(self):
        self.window.title("Configuración de atajos")

        self.centrarPantalla()

        anchoPantalla = self.window.winfo_screenwidth()
        altoPantalla = self.window.winfo_screenheight()

        anchoWidget = (PORCENTAJEANCHO * anchoPantalla) / 100
        altoWidghet = (PORCENTAJEALTO * altoPantalla) / 100

        resolucionWidget = str(int(anchoWidget)) + "x" + str(int(altoWidghet))
        self.window.geometry(resolucionWidget)

        # Primera fila: Titulo de la aplicación
        labelTitulo = tk.Label(self.window, text="Bienvenido, Sr trolo", anchor='center', font=("Arial Bold", 25))
        labelTitulo.place(relx = 0.5, rely = 0.1, anchor = "center")

        # Segunda Fila = Tecla de meditar
        labelMeditar = tk.Label(self.window, text="Tecla de Meditar", font=("Arial Bold", 18))
        labelMeditar.place(relx = 0.2, rely = 0.3, anchor = "center")
        txtFieldTeclaMeditar = tk.Entry(self.window,width=20, textvariable=self.txtTeclaMeditar)
        txtFieldTeclaMeditar.place(relx = 0.6, rely = 0.3, anchor = "center")

        # Tercera fila = Posición X e Y
        labelPosicionX = tk.Label(self.window, text="Posición Horizontal", font=("Arial Bold", 18))
        labelPosicionX.place(relx = 0.2, rely = 0.5, anchor = "center")
        txtFieldPosicionX = tk.Entry(self.window, width = 20, textvariable=self.txtPosicionX)
        txtFieldPosicionX.place(relx = 0.6, rely = 0.5, anchor = "center")

        labelPosicionY = tk.Label(self.window, text="Posición Vertical", font=("Arial Bold",18))
        labelPosicionY.place(relx = 0.2, rely = 0.7, anchor = "center")
        txtFieldPosicionY = tk.Entry(self.window, width=20, textvariable=self.txtPosicionY)
        txtFieldPosicionY.place(relx = 0.6, rely = 0.7, anchor = "center")

        # Cuarta fila = Boton aceptar

        botonAceptar = tk.Button(self.window, width = 20, text="Aceptar", command= self.validarInput)
        botonAceptar.place(relx = 0.5, rely = 0.9, anchor = "center")

        self.window.mainloop()



