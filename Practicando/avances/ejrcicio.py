texto=input("Dame un texto.  ")
pp=texto.split(" ") #en este caso los espacios se contarian como el num de palabras 
#print(pp)
cant_pal=len(pp)
print(f'lo quese tarda en estas palabras es : {cant_pal/2} segundos y son {cant_pal} palabras')
