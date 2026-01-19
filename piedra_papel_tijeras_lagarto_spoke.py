






import random

REGLAS = {
    "tijera": ["papel", "lagarto"],
    "papel": ["piedra", "spock"],
    "piedra": ["lagarto", "tijera"],
    "lagarto": ["spock", "papel"],
    "spock": ["tijera", "piedra"]
}
OPCIONES_VALIDAS = list(REGLAS.keys())

def jugar():
    eleccion_cpu = random.choice(OPCIONES_VALIDAS)

    print("Opciones disponibles: piedra, papel, tijera, lagarto, spock")
    entrada_usuario = input("Elige tu opción: ").strip().lower()

    if entrada_usuario not in OPCIONES_VALIDAS:
        print(f"Error: La opción '{entrada_usuario}' no es válida.")
        return

    print("-" * 30)
    print(f"Tú elegiste: {entrada_usuario.capitalize()}")
    print(f"La CPU eligió: {eleccion_cpu.capitalize()}")
    print("-" * 30)

    if entrada_usuario == eleccion_cpu:
        print("¡Empate!")
    elif eleccion_cpu in REGLAS[entrada_usuario]:
        print("¡Ganaste!")
    else:
        print("¡La CPU gana!")
    print("-" * 30)

if __name__ == "__main__":
    jugar()