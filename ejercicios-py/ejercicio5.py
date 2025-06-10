import random

# 5. Adivina el número
def adivina_numero():
    numero_secreto = random.randint(1, 100)
    intento = 0
    while True:
        intento += 1
        adivina = int(input("Adivina el número (1-100): "))
        if adivina < numero_secreto:
            print("Mayor")
        elif adivina > numero_secreto:
            print("Menor")
        else:
            print(f"¡Correcto! El número era {numero_secreto}. Intentos: {intento}")
            break

