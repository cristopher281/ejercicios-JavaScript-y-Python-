import random
# 2. Verificador de par/impar
def par_impar():
    numero = random.randint(1, 100)
    resultado = "par" if numero % 2 == 0 else "impar"
    print(f"El número {numero} es {resultado}.")

