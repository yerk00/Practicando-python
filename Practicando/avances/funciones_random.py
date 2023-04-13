def equipos(club,copas,edad):
    return f'el club: {club} tiene {copas} y una edad de: {edad}' #aqui se pueden darles unos valores obligatorios a los parametros
hincha=equipos("the strongest",15,115)
print(hincha)
#funciones lambda
#crea funciones anonimas
#filterlo que hace es como un pequeño bucle agresg a los true y lo almacena en una lista
numeros={1,2,3,4,5,6}
nump=filter(lambda numero: numero%2==0, numeros)
print(list(nump))