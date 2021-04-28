#Importa el modulo multiprocessing
import multiprocessing

#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time

#Crea la ventana principal
main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char):
    mylabel = createLabel(a,b)
    texto=""
    retardo: float=0.25
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update_idletasks()
        main_window.update()

#Crea los tres procesos de las animaciones
if __name__ == '__main__':
    proceso_1 = multiprocessing.Process(target=crearAnimacion,args=(10,10, 'X'))
    proceso_2 = multiprocessing.Process(target=crearAnimacion,args=(10,10, 'Y'))
    proceso_3 = multiprocessing.Process(target=crearAnimacion,args=(10,10, 'Z'))

    #Inicia llos 3 procesos de las animaciones
    proceso_1.start()
    proceso_2.start()
    proceso_3.start()

    #Lanza los 3 procesos de las animaciones
    proceso_1.join()
    proceso_2.join()
    proceso_3.join()


    # Mantener las siguientes líneas siempre al final del script y en el mismo orden.
    #Coloca la opcion "Salir"
    opcionFinalizar()

    #Bucle principal de la ventana
    main_window.mainloop()
