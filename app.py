#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
import random
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

# Al final de cada ronda, el jugador debe responder si quiere jugar de nuevo o no.
# El minijuego debe terminar cuando el jugador no quiera jugar más.
respuesta = "si"
while respuesta == "si":
    print("Hola jugador, vamos a jugar piedra, papel o tijera")
    print("Escribe tu elección: ")
    jugador = input()
    print("Tu elección es: " + jugador)
    while jugador != "piedra" and jugador != "papel" and jugador != "tijera":
        print("Escribe tu elección piedra/papel/tijera: ")
        jugador = input()
        print("Tu elección es: " + jugador)
    print("Ahora es mi turno")
    
    computadora = random.randint(1,3)
    if computadora == 1:
        computadora = "piedra"
    elif computadora == 2:
        computadora = "papel"
    else:
        computadora = "tijera"
    print("Mi elección es: " + computadora)
    if jugador == computadora:
        print("Empate")
    elif jugador == "piedra":
        if computadora == "papel":
            print("Perdiste")
        else:
            print("Ganaste")
    elif jugador == "papel":
        if computadora == "tijera":
            print("Perdiste")
        else:
            print("Ganaste")
    elif jugador == "tijera":
        if computadora == "piedra":
            print("Perdiste")
        else:
            print("Ganaste")
    print("¿Quieres jugar de nuevo?")
    respuesta = input()
    while respuesta != "si" and respuesta != "no":
        print("¿Quieres jugar de nuevo?")
        respuesta = input()
