import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def funcion(t,m,v):
    return v*(np.exp(m*t))


usecols1=["t","Vc"]
usecols2=["td","Vd"]
datosCond1=pd.read_csv("cond1000.csv",sep=";",decimal=",",header=1,usecols=usecols1)
datosCond2=pd.read_csv("cond1000.csv",sep=";",decimal=",",header=1,usecols=usecols2)


#POTENCIAL ELECTRICO EN LA CARGA DEL UN CONDENSADOR DE 2200microF
potentialC1=datosCond1["Vc"]
#POTENCIAL ELECTRICO EN LA DESCARGA DE UN CONDENSADOR DE 1000microF
potentialC2=datosCond2["Vd"]

timeC1=datosCond1["t"]
timeC2=datosCond2["td"]

#SE CONFIGURA EL DIAGRAMA DE DISPERSION
plt.ylabel("Potencial V (V)")
plt.xlabel("Tiempo(s)")

plt.title("Potencial eletrico medido en la resistencia durante la carga y descarga de un condensador.")
plt.scatter(timeC1,potentialC1,c="r",label="Carga Cond 1000 microF")
plt.scatter(timeC2,potentialC2,c="b",label="Descarga Cond 1000 microF")


#FIT CONDENSADOR 1
fitCond1=np.polyfit(timeC1,np.log(potentialC1),1)
m1=fitCond1[0]
v1=np.exp(fitCond1[1])
print(m1,v1)

#FIT CONDENSADOR 2
fitCond2=np.polyfit(timeC2,np.log(potentialC2),1)
m2=fitCond2[0]
v2=np.exp(fitCond2[1])
print(m2,v2)


valores1=range(min(timeC1),max(timeC1))
valores2=range(min(timeC2),max(timeC2))

plt.plot(valores1,[funcion(i,m1,v1) for i in valores1],c='black', linewidth=2)
plt.plot(valores2,[funcion(i,m2,v2) for i in valores2],c='black', linewidth=2)
print(funcion(68,m2,v2))
plt.legend()
plt.show()

    


