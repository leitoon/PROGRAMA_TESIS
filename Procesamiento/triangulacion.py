from ctypes.wintypes import PINT
from gettext import find
from pyexpat import features
import numpy as np
from math import tan
import pandas as pd
import os
import math
import cv2

pathInput = "D:\\PROGRAMA_TESIS\\segmentadaFinal"
nombreImagenes = os.listdir(pathInput)

X=[]
Y=[]
Z=[]
for im in range(len(nombreImagenes)):
    angulo=69.44
    angulo=np.radians(angulo)
    f=2087
    b=75
    cot=1/tan(angulo)
    desfase=im*2
    x=[]
    y=[]
    pres=3 #Presicion para redondear
    
    pathImagen = os.path.join(pathInput,nombreImagenes[im])
    
    imagen=cv2.imread(pathImagen)
    imagenGray = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
    pixel=np.argwhere(imagenGray == 255)
    pixel_lista=pixel.tolist()
    for k,j in pixel_lista:
        y.append(k)
        x.append(j)

    for i in range(len(x)):
        xn=((b)/((f*cot)-x[i])*x[i])+desfase
        xn=np.round(xn,pres)
        X.append(xn)
        
        ##Y
        yn=((b)/((f*cot)-x[i])*y[i])
        yn=np.round(yn,pres)
        Y.append(yn)
        ##Z
        zn=((b)/((f*cot)-x[i])*f)
        zn=np.round(zn,pres)
        Z.append(zn)
        
XYZ={
    "X": X,
    "Y": Y,
    "Z": Z,
    }   
#CICLO PARA RESULTADOS DE Y
def printDict(caracteristicas={"valor":"vacio"},nombre="vacio"):
    print("\n================ Caracteristicas de {} ================\n".format(nombre))
    for key in caracteristicas:
        print(key,":",caracteristicas[key])

rutaArchivotxt = "D:\\PROGRAMA_TESIS\\data_frame\\XYZtotal.txt"
data = pd.DataFrame(XYZ)
data.to_csv(rutaArchivotxt,index=False)
