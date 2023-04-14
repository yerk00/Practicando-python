# 'w' sirve para poder escribir

#lo que hace essobreescribir el contenido que tenia el txt con el que puse
with open ("archivos\\leer.txt",'w',encoding="UTF-8") as archivo:
    escribir=archivo.write("hola bro")