import tkinter as tk

def felicitar():
    print("jaja al final si te la bancaste 🥳👏👏👏")


ventana = tk.Tk() #Creamos una ventana principal 
ventana.title("Comisión 7 😎")
ventana.geometry("1200x900") # ancho x alto

texto = tk.Label(ventana, text="Bueeenos días Comisión Siete", font=('Arial', 30))
texto.pack(side="left")

boton = tk.Button(ventana, text="Hace click si te la bancas 😈", font=('Arial', 20), command=felicitar)
boton.pack(side="right")

ventana.mainloop()