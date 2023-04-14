# los archivos csv utiliza para almacenar datos tabulares en forma de filas y columnas útiles para compartir datos entre diferentes aplicaciones y sistemas
import csv


with open("archivos\\dato.csv") as archivo:
    #print("leido")
    reader= csv.reader(archivo)
    for row in reader:
        print(row)

