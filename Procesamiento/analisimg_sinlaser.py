import cv2 
import numpy as np
from matplotlib import pyplot as plt
import os

#se declara varible que contien la carpeta donde se tienes las imagenes capturadas
pathInput = "D:\\PROGRAMA_TESIS\\imagenes_bi"
#nombreImagenes me permite conocer el nombre de los archivos que se tienen en la carpeta de pathInput 
nombreImagenes = os.listdir(pathInput)
#se declara varible que contien la carpeta donde se guardaran las imagenes segmentadas
pathOutput = "D:\\PROGRAMA_TESIS\\segmentada2"

def verificacion_laser(img):
    #valores de histograma Vertical normalizados
    profile_H = np.sum(img, axis=0)
    Profile_H = 1*((profile_H-np.min(profile_H))/(np.max(profile_H)-np.min(profile_H)))
    DatoMax= np.max(Profile_H)
    Profile_H=Profile_H.tolist()
    indexDatoMax=Profile_H.index(DatoMax)
    Rango100=100
    for i in range((indexDatoMax+Rango100),len(Profile_H)):
        x=Profile_H[i]
        if(x>=0.4):         
           return False
        else:
            return True
      

#Se crea ciclo for del tamaño de elementos de las imagenes_procesamiento para 
#Que recorra todas las imagenes y haga el procesamiento
for i in range(len(nombreImagenes)):
    #pathImagen contiene la dirección y nombre de cada imagen contenidas en imagenes_procesamiento
    pathImagen = os.path.join(pathInput,nombreImagenes[i])
    #pathImagenOut contiene la dirección y nombre de cada imagen contenidas que se almacenara en segmentada
    pathImagenOut = os.path.join(pathOutput,nombreImagenes[i])
    # imagen se creo para pasar las imagenes de imagenes_procesamiento a RGB
    imagen = cv2.imread(pathImagen,cv2.COLOR_BGR2RGB)
    
    if(verificacion_laser(imagen)):
        cv2.imwrite(pathImagenOut,imagen)
    




