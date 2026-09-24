import random

def lanzar_dado():
    # La función genera un número aleatorio entre 1 y 6
    resultado = random.randint(1, 6)
    print(f"Lanzaste el dado y salió: {resultado}")

# Para ejecutarla, solo escribes su nombre con paréntesis vacíos:
lanzar_dado()
lanzar_dado()