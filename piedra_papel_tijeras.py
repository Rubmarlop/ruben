


import random
import sys

def jugar_piedra_papel_tijeras():
    #  opciones válidas  
    opciones_validas = ["piedra", "papel", "tijeras"]

     
    # Usamos random.choice para elegir una opción de la lista
    eleccion_cpu = random.choice(opciones_validas)

  
    # Solicitamos la entrada al usuario
    entrada_usuario = input("Elige una opción (Piedra, Papel, Tijeras): ")

    # Normalizamos la entrada: quitamos espacios al inicio/final y convertimos a minúsculas y esto hace que "Piedra", "PIEDRA" o " piedra " sean válidos.
    
    eleccion_usuario = entrada_usuario.strip().lower()

    # Validación de la entrada
     
    if eleccion_usuario not in opciones_validas:
        print(f"Error: La palabra '{entrada_usuario}' no ha sido reconocida.")
         
        sys.exit()

    # Mostramos qué ha elegido cada uno.
     
    print("-" * 40)
    print(f"Has elegido: {eleccion_usuario.capitalize()}")
    print(f"La CPU ha elegido: {eleccion_cpu.capitalize()}")
    print("-" * 40)

     # Empate 
    if eleccion_usuario == eleccion_cpu:
        print("¡Se ha producido un empate!")
    # Casos en los que el usuario gana:
    elif (eleccion_usuario == "piedra" and eleccion_cpu == "tijeras") or \
         (eleccion_usuario == "papel" and eleccion_cpu == "piedra") or \
         (eleccion_usuario == "tijeras" and eleccion_cpu == "papel"):
        print("¡Felicidades! ¡Has ganado!")
    # Si no es empate y no gana el usuario, entonces gana la CPU:
    else:
        print("¡Lástima! La CPU ha ganado.")
    print("-" * 40)

 if __name__ == "__main__":
    jugar_piedra_papel_tijeras()