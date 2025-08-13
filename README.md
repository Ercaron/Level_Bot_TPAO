# Bot de auto-lanzar hechizos.

**Liberías utilizadas:**
- Tkinter
- Pynput
- FuncTools
- Threading

## Posición del boton lanzar según Resolución:
 - **1920x1080:** X= 1446 Y=659
 - **1600x900**: X=1300 Y=570
 - **1366x768:** X=1192 Y=507
 - **1280x720:** X=1143 Y=481
 - **fullScreen** X=1138 Y=4750

## Información de Uso:
 - Si es la primera vez que se abre el programa, tocar el botón configurar.
    - Ingresar la tecla en la cual tiene seteada la acción de meditar (Letra o número)
    - Ingresar la posición en X e Y según la resolución (Ver mas arriba)
 - Al tocar aceptar, dichos valores se guardarán en un archivo "Configuracion.txt" dentro de la carpeta del bot.
 - Al tocar la combinación de teclas **"X" + "C"** al mismo tiempo, el bot comenzará a ejecutar el auto lanzado del hechizo seleccionado sobre el monstruo sobre el que se haya colocado el cursor.
 - Al tocar la misma combinación de teclas se detiene el bot.
 - Si se usa la combinacion **"X" + "B"**, se sale del proceso del bot.   
 
 ## Link de descarga:
  - **[MEGA](https://mega.nz/file/hEMxBAjS#kzf8llqPyQbyLrkdv5sXD4ehCs__JAMkQof0Prn-OMA)** 


## Historial de revisiones:
- **10/9:** Creación del script
- **12/9:** Inicio de creación de UI. Permite ingresar una tecla y que valide el texto ingresado
- **13/9:** Cambios y novedades:
    - Punto de entrada a la app es la UI
    - Si hay un archivo de configuración válido => Se inicia el bot automaticamente (Falta armar el otro camino)
    - Se puede leer y crear un archivo de configuración en la carpeta del bot para levantar la info de la tecla de meditar, posicion en x e y del botón lanzar
- **14/9:** Novedades:
    - Ventana inicial para seleccionar si se quiere iniciar la aplicación o configurarla. En el caso de que no existe configuración, es obligatoria hacerla previo a ejecutar.
    - BugFix a la hora de guardar los valores ingresados por teclado ya que guardaba un espacio en blanco extra.
- **15/9:** Novedades:
    - Solucionado bug al guardar la información en un txt.
    - Agregado mensaje al finalizar la ejecución del programa.
    - Primera versión ejecutable (Ver link)
