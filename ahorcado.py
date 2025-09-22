import random
print("------Bienvenido al ahorcado------")
print("1. Fácil")
print("2. Normal")
print("3. Difícil")
respuesta = input("Elige una dificultad: ")

if respuesta == "1":

    facil = [
        "sol", "luz", "mar", "casa", "perro",
        "gato", "libro", "mesa", "silla", "piedra"
    ]

    palabra_secreta = random.choice(facil)
    contador_intentos = 30
    progreso = ["_"] * len(palabra_secreta)

    while True:
        letra = input("Escribe una letra: ")
        for i, caracter in enumerate(palabra_secreta):
            if caracter == letra:
                progreso[i] = letra
        print(" ".join(progreso))
        
        contador_intentos -= 1
        print("Intentos restantes: ", contador_intentos)
        
        if "_" not in progreso:
            print("¡Felicidades, has ganado :D!")
            break
        
        if contador_intentos == 0:
            print("Ohh, has perdido :(")
            print("La palabra era", palabra_secreta)
            break
elif respuesta == "2":

    normal = [
    "python", "raton", "teclado", "pantalla", "internet",
    "juego", "variable", "funcion", "tupla", "codigo"
    ]

    palabra_secreta = random.choice(normal)
    contador_intentos = 20
    progreso = ["_"] * len(palabra_secreta)

    while True:
        letra = input("Escribe una letra: ")
        for i, caracter in enumerate(palabra_secreta):
            if caracter == letra:
                progreso[i] = letra
        print(" ".join(progreso))
        
        contador_intentos -= 1
        print("Intentos restantes: ", contador_intentos)
        
        if "_" not in progreso:
            print("¡Felicidades, has ganado :D!")
            break
        
        if contador_intentos == 0:
            print("Ohh, has perdido :(")
            print("La palabra era", palabra_secreta)
            break
elif respuesta == "3":

    dificil = [
    "programacion", "inteligencia", "algoritmo", "astronauta",
    "universo", "galaxia", "ciencia", "misterio", "aventura", "diccionario"
    ]

    palabra_secreta = random.choice(dificil)
    contador_intentos = 15
    progreso = ["_"] * len(palabra_secreta)

    while True:
        letra = input("Escribe una letra: ")
        for i, caracter in enumerate(palabra_secreta):
            if caracter == letra:
                progreso[i] = letra
        print(" ".join(progreso))
        
        contador_intentos -= 1
        print("Intentos restantes: ", contador_intentos)
        
        if "_" not in progreso:
            print("¡Felicidades, has ganado :D!")
            break
        
        if contador_intentos == 0:
            print("Ohh, has perdido :(")
            print("La palabra era", palabra_secreta)
            break
else:
    print("Respuesta no válida")
        