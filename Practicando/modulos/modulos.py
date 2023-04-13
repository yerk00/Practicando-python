#lo que importa se comporta como un objeto y el contenido como un metodo
#tambien podremos renombrarlos o darles un alias est con un as

#import modulo_team as equipo

#modulo_team vendria a ser un modulo namespace que se refiere al nombre del contenido del contenido de ese modulo
#-------------------------------------------------------------------------------------------------------

# para solo llamar a una fincion especifica dntro de un modulo
from modulo_team import equipo,equipo2
mejor_equipo2=equipo2("bolivar")
mejor=equipo("the strongest")
print(mejor_equipo2)
print(mejor)

#ENRUTAMIENTO

# Para acceder a un modulo dentro de otra carpeta lo que se hace es "nombre del archivo.modulo"