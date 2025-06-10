import random
# 3. Contador de vocales
def contador_vocales():
    palabras = [
        "Aceituna", "Murciélago", "Educación", "Aeropuerto",
        "Otorrinolaringólogo", "Euforia", "Aceite", 
        "Paleontólogo", "Arquitectura", "Hipopótamo"
    ]
    palabra = random.choice(palabras)
    vocales = set("AEIOUÁÉÍÓÚ")
    vocales_en_palabra = set([letra for letra in palabra.upper() if letra in vocales])
    print(f"Palabra: {palabra}, Vocales: {', '.join(vocales_en_palabra)}")
