import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

usecols=["tc","Vc"]
usecols2=["t","Vc"]
datosCond1=pd.read_csv("serie1.csv",sep=";",decimal=",",header=1,usecols=usecols)
datosCond2=pd.read_csv("cond1000.csv",sep=";",decimal=",",header=1,usecols=usecols2)

#POTENCIAL ELECTRICO EN LA CARGA DEL UN CONDENSADOR DE 2200microF
potentialC1=datosCond1["Vc"]
#POTENCIAL ELECTRICO EN LA DESCARGA DE UN CONDENSADOR DE 1000microF
potentialC2=datosCond2["Vc"]

timeC1=datosCond1["tc"]
timeC2=datosCond2["t"]

#SE CONFIGURA EL DIAGRAMA DE DISPERSION
plt.ylabel("Potencial V (V)")
plt.xlabel("Tiempo(s)")

plt.title("Carga de condensadores")
plt.scatter(timeC1,potentialC1,c="r",label="Condensador 2200 microF")
plt.scatter(timeC2,potentialC2,c="b",label="Condensador 1000 microF")
plt.legend()
plt.show()

