import re

#Definimos una cadena de texto para buscar
texto = "El club the strongest es el mas grande de bolivia"

#Creamos una expresión regular para buscar la palabra "rojo"
res = r"bolivia"

#Usamos la función search() de la biblioteca re para buscar una coincidencia de bolivia en el texto
match = re.search(res, texto)

# Si se encontró una coincidencia, imprimimos el resultado
""" if match:
    print("Se encontró una coincidencia")
else:
    print("No se encontró una coincidencia")
 """
#pero tambienpodriamos utilizar el findall que nos dara todass las coincidencias
resultado= re.findall("bolivia",texto)
print(resultado)