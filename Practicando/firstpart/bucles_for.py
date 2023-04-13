list=["juan","pedro","pepe"]
#primerq ejecucion de un for nos muestra el primer elemento asi sucesivamente hasta que el array o lista termine hace su recorridp
for nombres in list :
    print(nombres)
    
#para iterar dos listas necesariamente ddeben tener la misma cantidad deelmentos funciona elemento 1 de lista 1 con elmneto 1 de lista 2
equipos=["the strongest","bolivar", "wilstermann"]
copas=[15, 30, 14]
for equipos,copas in zip(equipos,copas) :
    print(f'equipo:{equipos}')
    print(f'copas: +{copas}')