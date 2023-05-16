import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

usecols=["tc","Vc","td","Vd"]
usecols2=["t","Vc","Vd"]
usecols3=["t","Vc"]
datosUno=pd.read_csv("serie1.csv",sep=";",decimal=",",header=1,usecols=usecols)
datos_Serie=pd.read_csv("serie2.csv",sep=";",decimal=",",header=1,usecols=usecols2)
datos_paralelos=pd.read_csv("paralelos.csv",sep=";",decimal=",",header=1,usecols=usecols3)

#POTENCIAL ELECTRICO EN LA CARGA DEL UN CONDENSADOR 
potentialUno=datosUno["Vc"]
#POTENCIAL ELECTRICO EN LA DESCARGA DE DOS CONDENSADORES EN SERIE
potentialSerie=datos_Serie["Vc"]
#POTENCIAL ELECTRICO EN LA DESCARGA DE DOS CONDENSADORES EN PARALELO
potentialParalelo=datos_paralelos["Vc"]

time=datosUno["tc"]
timeSerie=datos_Serie["t"]
timeParalelos=datos_paralelos["t"]

#SE CONFIGURA EL DIAGRAMA DE DISPERSION
plt.ylabel("Potencial V (V)")
plt.xlabel("Tiempo(s)")

plt.title("Carga de condensadores")
plt.scatter(time,potentialUno,c="r",label="Condensador Solo")
plt.scatter(timeSerie,potentialSerie,c="b",label="Condensadores Serie")
plt.scatter(timeParalelos,potentialParalelo,c="g",label="Condensadores Paralelos")
plt.legend()
plt.show()

print(datosUno)
