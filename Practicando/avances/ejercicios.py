numeros = []
for i in range(5):
    edad = int(input("dam tu edad: "))
    numeros.append(edad)
#def alumnos(edad):
#    comparar=list(edad)
comparacion=filter(lambda edades: max(edades), edad)
print(list(comparacion))
