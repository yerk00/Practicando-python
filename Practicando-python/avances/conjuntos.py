conjunto1= set({"pedrito"})
conjunto2=frozenset({"juan"})
#para crear un conjunto dentro de otro conjunto utilizamos el frozenset que sirve para crear un conjunto inmutable es decir un conjunto dentro de otro conjunto
conjunto={conjunto2,"lolo"}
print(conjunto)
#pára subconjuntos 
conj1={1,2,3,4,5}
conj2={1,2,3,4}
#utiliazmos el issubset que significa que pregunta si es un subconjunto de otro conjunto este nos retorna un booleano
conjunt=conj2.issubset(conj1)
print(conjunt)
#isdisjoint nos indica si los subconjuntos son iguales 
