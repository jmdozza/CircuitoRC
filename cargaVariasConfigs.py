import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def funcion(t,m,v):
    return v*(np.exp(m*t))

usecols=["tc","Vc","td","Vd"]
usecols2=["t","Vc","Vd"]
usecols3=["t","Vc"]

datos_Serie=pd.read_csv("serie2.csv",sep=";",decimal=",",header=1,usecols=usecols2)
datos_paralelos=pd.read_csv("paralelos.csv",sep=";",decimal=",",header=1,usecols=usecols3)

#POTENCIAL ELECTRICO EN LA CARGA DEL UN CONDENSADOR 

#POTENCIAL ELECTRICO EN LA DESCARGA DE DOS CONDENSADORES EN SERIE
potentialSerie=datos_Serie["Vc"]
#POTENCIAL ELECTRICO EN LA DESCARGA DE DOS CONDENSADORES EN PARALELO
potentialParalelo=datos_paralelos["Vc"]

#TIEMPOS
timeSerie=datos_Serie["t"]
timeParalelos=datos_paralelos["t"]

#SE CONFIGURA EL DIAGRAMA DE DISPERSION
plt.ylabel("Potencial V (V)")
plt.xlabel("Tiempo(s)")

plt.title("Potencial électrico en la carga entre circuito RC Serie y RC paralelo")
plt.scatter(timeSerie,potentialSerie,c="b",label="Condensadores Serie")
plt.scatter(timeParalelos,potentialParalelo,c="g",label="Condensadores Paralelos")

#FIT CONDENSADOR SERIE
fitCondserie=np.polyfit(timeSerie,np.log(potentialSerie),1)
m1=fitCondserie[0]
v1=np.exp(fitCondserie[1])
print(m1,v1)

#FIT CONDENSADOR PARALELO
fitCondparalelo=np.polyfit(timeParalelos,np.log(potentialParalelo),1)
m2=fitCondparalelo[0]
v2=np.exp(fitCondparalelo[1])
print(m2,v2)

valores1=range(min(timeSerie),max(timeSerie))
valores2=range(min(timeParalelos),max(timeParalelos))

plt.plot(valores1,[funcion(i,m1,v1) for i in valores1],c='black', linewidth=2)
plt.plot(valores2,[funcion(i,m2,v2) for i in valores2],c='black', linewidth=2)



plt.legend()
plt.show()

