

import random

# El programa genera un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0
adivinado = False

print("¡Bienvenido al juego del número secreto!")
print("He elegido un número entre 1 y 100. ¡Intenta adivinarlo!")

# El bucle continúa hasta que el usuario adivina el número
while not adivinado:
    try:
        
        estimacion = int(input("Introduce tu número: "))
        intentos += 1

        
        if estimacion < numero_secreto:
            print("Mi número es mayor.")
        elif estimacion > numero_secreto:
            print("Mi número es menor.")
        else:
            adivinado = True
    except ValueError:
         número entero
        print("Por favor, introduce un número entero válido.")


print(f"Has adivinado el número {numero_secreto} en {intentos} intentos.")