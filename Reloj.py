from tkinter import Tk, Label
import time

ventana= Tk()
ventana.config(bg="gray")
ventana.geometry("500x400")
ventana.wm_attributes("-transparentcolor","gray")
ventana.overrideredirect(True) #Quitar bordes de la ventaja

def salir():
        ventana.destroy()
        ventana.quit()

def obtener_hora():
        hora = time.strftime("%H:%M:%S")
        fecha_formato12 = time.strftime("%A %d %B %Y")

        texto_hora["text"] = hora  # Assign a value to the "text" attribute of "texto_hora"
        texto_fecha12["text"] = fecha_formato12  # Assign a value to the "text" attribute of "texto_fecha12"
        texto_hora.after(1000,obtener_hora)  # Call the function "obtener_hora" every 1000 milliseconds

texto_hora = Label(ventana, font=("Arial", 30), fg="white", bg="gray", width=20)
texto_hora.grid(row=0, column=0, ipadx=1, ipady=1)

texto_fecha12 = Label(ventana, font=("Arial", 20), fg="white", bg="gray", width=20)
texto_fecha12.grid(row=1, column=0, ipadx=1, ipady=1)

obtener_hora()
ventana.mainloop()
ventana.bind("<KeyPress-Escape>", salir)

texto_hora= Label(ventana, font=("Arial", 30), fg="white", bg="gray", width=20)
texto_hora.grid(row=0, column=0, ipadx=1, ipady=1)

texto_fecha12= Label(ventana, font=("Arial", 20), fg="white", bg="gray", width=20)
texto_fecha12.grid(row=1, column=0, ipadx=1, ipady=1)

obtener_hora()
ventana.mainloop()