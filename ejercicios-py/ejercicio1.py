import random
import string

# 1. Calculadora básica
def calculadora():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    operacion = input("Ingrese la operación (+, -, *, /): ")
    
    if operacion == '+':
        resultado = num1 + num2
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 if num2 != 0 else "Error: División por cero"
    else:
        resultado = "Operación no válida"
    
    print(f"Resultado: {resultado}")
