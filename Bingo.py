import tkinter as tk
import random

# Crear ventana principal
root = tk.Tk()
root.title("BINGO")

# Diccionario para guardar los botones de cada número
botones = {}

# Crear marco principal para la cuadrícula
frame = tk.Frame(root)
frame.pack(side="right", padx=10, pady=10)

# Definir rangos de columnas B, I, N, G, O
columnas = {
    "B": range(1, 16),
    "I": range(16, 31),
    "N": range(31, 46),
    "G": range(46, 61),
    "O": range(61, 76)
}

# Crear la cuadrícula de números
for col_index, (letra, numeros) in enumerate(columnas.items()):
    tk.Label(frame, text=letra, font=("Arial", 14, "bold")).grid(row=0, column=col_index, padx=5, pady=5)
    for row_index, numero in enumerate(numeros, start=1):
        boton = tk.Label(frame, text=str(numero), width=4, height=2,
                         bg="white", fg="black", relief="solid", borderwidth=1)
        boton.grid(row=row_index, column=col_index, padx=2, pady=2)
        botones[numero] = boton

# Lista de números disponibles
numeros_disponibles = list(range(1, 76))

# Crear un Canvas para mostrar el número grande en círculo
canvas = tk.Canvas(root, width=300, height=300, bg="white")
canvas.pack(side="left", padx=20, pady=20)

# Función para dibujar el círculo con el número
def mostrar_numero(letra, numero):
    canvas.delete("all")  # limpiar antes de dibujar
    # Dibujar círculo amarillo
    canvas.create_oval(20, 20, 280, 280, fill="yellow", outline="black", width=3)
    # Escribir número con letra
    canvas.create_text(150, 150, text=f"{letra}-{numero}", font=("Arial", 32, "bold"), fill="black")

# Función para girar
def girar():
    global numeros_disponibles
    if numeros_disponibles:
        numero = random.choice(numeros_disponibles)
        numeros_disponibles.remove(numero)
        botones[numero].config(bg="yellow")  # iluminar el número

        # Determinar la letra según el rango
        if 1 <= numero <= 15:
            letra = "B"
        elif 16 <= numero <= 30:
            letra = "I"
        elif 31 <= numero <= 45:
            letra = "N"
        elif 46 <= numero <= 60:
            letra = "G"
        else:
            letra = "O"

        mostrar_numero(letra, numero)
    else:
        canvas.delete("all")
        canvas.create_text(150, 150, text="Fin", font=("Arial", 32, "bold"), fill="red")

# Función para reiniciar
def reiniciar():
    global numeros_disponibles
    numeros_disponibles = list(range(1, 76))
    for boton in botones.values():
        boton.config(bg="white")
    canvas.delete("all")  # borrar círculo y número

# Botón girar
girar_btn = tk.Button(root, text="Girar", command=girar, font=("Arial", 12))
girar_btn.pack(pady=5)

# Botón reiniciar
reiniciar_btn = tk.Button(root, text="Reiniciar", command=reiniciar, font=("Arial", 12))
reiniciar_btn.pack(pady=5)

# Iniciar la aplicación
root.mainloop()
