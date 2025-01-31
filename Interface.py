import tkinter as tk

def convertir():
    try:
        celcius = float(entry.get())
        farenheit = (celcius * 9/5)+ 32
        resultado.config(text=f"Resultado: {farenheit:.2f}°F")
    except:
       resultado.config(text="Ingrese un número valido")

#configuración de la ventana
root = tk.Tk()
root.title("Conversor de Temperatura")#Definir titulo
root.geometry("300x200")#Definir tamaño



#widgets
tk.Label(root, text="Ingrese temperatura en °C:").pack(pady=5)
entry = tk.Entry(root)
entry.pack(pady=5)
tk.Button(root, text="Convertir", command=convertir).pack(pady=5)
resultado = tk.Label(root, text="Resultado: ")
resultado.pack(pady=5)

root.mainloop()

