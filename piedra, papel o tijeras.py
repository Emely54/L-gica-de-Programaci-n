# PROYECTO: PIEDRA, PAPEL O TIJERAS
# Estudiante: Emely Yersabel Castillo Tuarez
# Juego de piedra papel o tijeras 
# El usuario compite contra la computadora eleigiendo piedra papel o tijeras
# El ganador se decide dependiendo la opcion elegida entre ambos

import random   

# Se establece las opciones

lista = ("piedra", "papel", "tijera")

computadora = random.choice(lista)
jugador = None

while jugador not in lista:
 jugador = input ("Elije Piedra, Papel o Tijeras:").lower()

# Se establecen las condiciones de victoria, derrota o empate del jugador

if jugador == computadora:
 print ("Computadora: ", computadora) 
 print("Jugador: ", jugador)
 print("Empate")

elif jugador == "piedra":
 if computadora == "papel":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Perdiste ") 
 if computadora == "tijera":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Ganaste") 

elif jugador == "Papel":
 if computadora == "tijera":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Perdiste")
 if computadora == "piedra":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Ganaste") 

elif jugador == "tijera":
 if computadora == "Papel":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Ganaste")
 if computadora == "piedra":
  print ("Computadora: ", computadora) 
  print("Jugador: ", jugador)
  print("Perdiste") 



  
