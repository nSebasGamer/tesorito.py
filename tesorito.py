import tkinter as tk
import win32print
import win32api
from datetime import datetime
import random
from tkinter import filedialog
from tkinter import messagebox

turnos_ocupados = []


def abrir_configuracion():
    # Aquí puedes agregar la lógica para la ventana de configuración
    pass

def imprimir_turno(turno):
    # Obtener la impresora predeterminada
    impresora = win32print.GetDefaultPrinter()

    # Establecer la impresora predeterminada (opcional, si no está configurada)
    win32print.SetDefaultPrinter(impresora)

    # Obtener una manija a la impresora
    hPrinter = win32print.OpenPrinter(impresora)

    # Configurar las propiedades de impresión
    properties = {
        win32print.PRINTER_ENUM_DEFAULT: {
            "DesiredAccess": win32print.PRINTER_ALL_ACCESS
        }
    }

    # Iniciar el documento de impresión
    hJob = win32print.StartDocPrinter(hPrinter, 1, ("Python Print", None, "RAW"))

    # Iniciar una página de impresión
    win32print.StartPagePrinter(hPrinter)

    # Diseño del turno
    texto = f"=====================\n"
    texto += f"   TESORITO TEMPLO DE FATIMA\n"
    texto += f"=====================\n\n"
    texto += f"  Numero: {turno}\n\n"
    texto += f"  Fecha: {datetime.now().strftime('%Y-%m-%d')}\n"
    texto += f"  Hora: {datetime.now().strftime('%H:%M:%S')}\n\n"
    texto += f"=====================\n"

    # Imprimir el turno
    win32print.WritePrinter(hPrinter, texto.encode())

    # Finalizar la página de impresión
    win32print.EndPagePrinter(hPrinter)

    # Finalizar el documento de impresión
    win32print.EndDocPrinter(hPrinter)

    # Cerrar la impresora
    win32print.ClosePrinter(hPrinter)

def generar_nuevo_turno():
    turno_actual = obtener_turno_actual()

    if turno_actual <= 100:
        turno = random.randint(1, 100)
        turnos_ocupados.append(turno)

        imprimir_turno(turno)
        incrementar_turno(turno_actual)
        guardar_turno(turno)
    else:
        print("Se ha alcanzado el límite de 100 turnos.")

def obtener_turno_actual():
    try:
        with open("turno.txt", "r") as file:
            turno_actual = int(file.read())
    except FileNotFoundError:
        turno_actual = 1
    
    return turno_actual

def incrementar_turno(turno_actual):
    turno_siguiente = turno_actual + 1
    with open("turno.txt", "w") as file:
        file.write(str(turno_siguiente))

def guardar_turno(turno):
    with open("turnos_generados.txt", "a") as file:
        file.write(f"{turno}\n")

def restablecer_turnos():
    global turnos_ocupados
    turnos_ocupados = []
    with open("turno.txt", "w") as file:
        file.write("1")
    with open("turnos_generados.txt", "w") as file:
        file.write("")
    print("Se han restablecido los tickets.")

def generar_archivo_turnos():
    global turnos_ocupados
    if turnos_ocupados:
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for turno in turnos_ocupados:
                    file.write(f"{turno}\n")
            print("Archivo guardado exitosamente.")
        else:
            print("No se ha seleccionado un archivo.")
    else:
        print("No hay turnos generados para guardar.")

def seleccionar_premiados():
    if len(turnos_ocupados) >= 5:
        premiados_window = tk.Toplevel(root)
        premiados_window.title("Premiados")
        premiados_window.geometry("300x200")

        estilo_label = {"font": ("Arial", 14), "padx": 10, "pady": 5}

        premiados = random.sample(turnos_ocupados, 5)

        for premiado in premiados:
            label_premiado = tk.Label(premiados_window, text=f"Premiado: {premiado}", **estilo_label)
            label_premiado.pack()

    else:
        print("No hay suficientes turnos generados para seleccionar 5 premiados.")

def mostrar_informacion():
    mensaje = "TESORITO TEMPLO DE FATIMA\n\n"
    mensaje += "Esta aplicación permite generar Numeros para el Tesorito Del Templo de Fatima.\n"
    mensaje += "Los turnos se generan al azar y se pueden imprimir.\n\n"
    mensaje += "El numero premiado es aleatorio y dependera de tu suerte\n\n"
    mensaje += "© 2023 Todos los derechos reservados."

    messagebox.showinfo("Información", mensaje)

def abrir_tesorito():
    # Crea la ventana principal del Tesorito
    ventana_tesorito = tk.Tk()
    ventana_tesorito.title("TESORITO TEMPLO DE FATIMA - Generar Turno")
    ventana_tesorito.geometry("650x350")


    # Resto del código del Tesorito (tal como lo tenías)

    ventana_tesorito.mainloop()

from tkinter import Tk
import os
from PIL import Image, ImageTk
from tkinter import Tk, Label

root = tk.Tk()
root.title("TESORITO TEMPLO DE FATIMA - Generar Turno")
root.geometry("650x350")


# Obtiene la ruta absoluta del script actual
ruta_script = os.path.abspath(__file__)

# Obtiene la carpeta del script
carpeta_script = os.path.dirname(ruta_script)

# Carpeta de imágenes
carpeta_imagenes = os.path.join(carpeta_script, "imagenes")

# Ruta del archivo de icono
ruta_icono = os.path.join(carpeta_imagenes, "icono.ico")

# Abre el archivo de icono y conviértelo en una imagen compatible
imagen_icono = Image.open(ruta_icono)

# Convierte la imagen en un objeto PhotoImage de Tkinter
icono = ImageTk.PhotoImage(imagen_icono)

# Establece el icono en la ventana
root.tk.call('wm', 'iconphoto', root._w, icono)

ruta_script = os.path.abspath(__file__)

# Obtiene la carpeta del script
carpeta_script = os.path.dirname(ruta_script)

# Carpeta de imágenes
carpeta_imagenes = os.path.join(carpeta_script, "imagenes")

# Ruta de la imagen
ruta_imagen = os.path.join(carpeta_imagenes, "imagen.png")

# Abre la imagen y conviértela en una imagen compatible
imagen = Image.open(ruta_imagen)
imagen = imagen.resize((300, 400))

# Convierte la imagen en un objeto PhotoImage de Tkinter
imagen_tk = ImageTk.PhotoImage(imagen)

# Crea un widget de etiqueta para mostrar la imagen
label_imagen = Label(root, image=imagen_tk)
label_imagen.place(x=0 , y= 0)


boton_informacion = tk.Button(root, text="?", font=("Arial", 14), bg="#808080", fg="white", command=mostrar_informacion)
boton_informacion.place(x=600, y= 310)

label_titulo = tk.Label(root, text="TESORITO TEMPLO DE FATIMA", font=("Calibri", 25, "bold"))
label_titulo.place(x=200, y=20)

boton_generar_turno = tk.Button(root, text="Generar Turno", font=("Arial", 14), bg="#4287f5", fg="white", command=generar_nuevo_turno)
boton_generar_turno.place(x=450, y=100)

boton_restablecer = tk.Button(root, text="Restablecer Turnos", font=("Arial", 14), bg="#f54242", fg="white", command=restablecer_turnos)
boton_restablecer.place(x=450, y=150)

boton_guardar_archivo = tk.Button(root, text="Guardar Turnos", font=("Arial", 14), bg="#42f57a", fg="white", command=generar_archivo_turnos)
boton_guardar_archivo.place(x=450, y=200)

boton_premiados = tk.Button(root, text="Premiados", font=("Arial", 14), bg="#f5c842", fg="white", command=seleccionar_premiados)
boton_premiados.place(x=450, y=250)

ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio - TESORITO TEMPLO DE FATIMA")
ventana_inicio.geometry("400x150")

label_titulo_inicio = tk.Label(ventana_inicio, text="TESORITO TEMPLO DE FATIMA", font=("Calibri", 18, "bold"))
label_titulo_inicio.pack(pady=20)

boton_configuracion = tk.Button(ventana_inicio, text="Configurar", font=("Arial", 14), bg="#4287f5", fg="white", command=abrir_configuracion)
boton_configuracion.pack()

boton_tesorito = tk.Button(ventana_inicio, text="Tesorito", font=("Arial", 14), bg="#f54242", fg="white", command=abrir_tesorito)
boton_tesorito.pack()

boton_informacion = tk.Button(ventana_inicio, text="?", font=("Arial", 14), bg="#808080", fg="white", command=mostrar_informacion)
boton_informacion.pack(pady=10)

ventana_inicio.mainloop()