def suma(a,b):
    #sumita=a+b
    return a+b
resultado=suma(2,2)
#print(resultado)
#el*con un nombre aagarra todo los elementos y los convierte en unoi solo
#en este caso no puedo agregar mas parametros al final
def sumita(tipo,*numbers) :
    return f' Su tipo es: {tipo} y el maximo es: {max(numbers)}'
salida=sumita("entero",1,2,3)
print(salida)
#ahora utilizando ñlistas en estas si nos permite aumentar mas parametros al final de los args
def sumota(tipo,numbers, tamaño) :
    return f'el tipo es: {tipo} el numero maximo es: {max([*numbers])} '
salida1=sumita("entero",1,2,3)
print(salida1)
