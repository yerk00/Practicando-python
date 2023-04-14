#para abrir un archivo txt
#abrir=open("archivos\\leer.txt", encoding="UTF-8")
#Para poder eleer el contenido del archivo completo utilizamos la funcion read
#leer=abrir.read()
#print(leer) 
#para leer linea por linea
#linea=abrir.readlines()
#print(linea)

#---------------------------------------------------------------------------------------------
#Otra forma de leer de manera mas optima es con el width tiene menores errores de excepciones
with open ("archivos\\leer.txt",encoding="UTF-8") as archivo:
    print("SE ABRIO CORRECTAMENTE")
    print(archivo.read())