import random
while True:
    pedida= input("ingrese la opcion que elija piedra papel o tijera: ")
    diccionario ={
    1: "piedra",
    2: "papel",
    3: "tijera"
     }
    numero_aleatorio = random.randint(1, 3)
    keys=diccionario[numero_aleatorio]
    print("la maquina saco: ")
    print(keys)
    if pedida==keys :
      print("empate")
    else :
      if pedida=="piedra" and keys=="tijera" :
           print("ganaste")
      if pedida=="tijera" and keys=="piedra" :
          print("perdiste")
      if pedida=="piedra" and keys=="papel" :
          print("perdiste")
      if pedida =="tijera" and keys=="papel" :
          print("ganaste")
      if pedida=="papel" and keys=="tijera" :
          print("perdiste")
      if pedida=="papel" and keys=="piedra" :
          print("ganaste")
    
       
    print("Desea jugar otra vez?")

