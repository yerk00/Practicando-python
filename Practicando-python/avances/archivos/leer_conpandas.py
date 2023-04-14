# para analisis de datos e i.a csv pero son mejores los pandas
#asignar los pandas como pd siempre
#jupiternotebook es mas optimo para ia
# df es el dataframe son estructuras bidimensionales (como hojas de calculos) trabaja con filas y columnas
import pandas as pd

df= pd.read_csv("archivos\\dato.csv")
df2= pd.read_csv("archivos\\dato.csv")
nombres= df["club"]
#print(nombres)

#cadena="abcdefg"
#print(cadena[2:5]) #slizing sirve para seleccionar el inicio y el fin que se reecorrera

#ordenando el dataframe por edad
df_ordenado_asc=df.sort_values("edad")
#de forma decendente
df_ordenado_descendente=df.sort_values("edad",ascending=False)
#print(df_ordenado_descendente)
#para concatenar dos datas frames
df_concateando=pd.concat([df,df2])
#print(df_concateando)
#para acceder a lla cabeza o head 
df_cabeza=df.head(1)
#print(df_cabeza)
#estadistica del data frame
df_estadistica=df.describe()
print(df_estadistica)
#para acceder a un determinado elemento es con loc que accede a la fila y el elemento que quiera y el iloc las posiciones
#para eliminar filas repetidas utilizamos el dropna() con datos faltantes en filas y columnas se utiliza el dropna(axis=1) y axis=0
#para convertir a string los datos de la columna utilizamos astype(str)
#para elmiar las filas repetidas drop_duplicates()
#para crear un csv se utiliza to_csv

