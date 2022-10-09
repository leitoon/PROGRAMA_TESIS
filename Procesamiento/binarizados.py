import numpy as np 
import cv2
import mahotas as mt
import os
import pandas as pd
#se declara varible que contien la carpeta donde se tienes las imagenes capturadas
pathInput = "D:\\PROGRAMA_TESIS\\imagenes_capturadas"
#nombreImagenes me permite conocer el nombre de los archivos que se tienen en la carpeta de pathInput 
nombreImagenes = os.listdir(pathInput)
#se declara varible que contien la carpeta donde se guardaran las imagenes segmentadas
pathOutput = "D:\\PROGRAMA_TESIS\\imagenes_bi"
#Se crea ciclo for del tamaño de elementos de las imagenes_procesamiento para 
#Que recorra todas las imagenes y haga el procesamiento
for i in range(len(nombreImagenes)):
    #pathImagen contiene la dirección y nombre de cada imagen contenidas en imagenes_procesamiento
    pathImagen = os.path.join(pathInput,nombreImagenes[i])
    #pathImagenOut contiene la dirección y nombre de cada imagen contenidas que se almacenara en segmentada
    pathImagenOut = os.path.join(pathOutput,nombreImagenes[i])
    imagen = cv2.imread(pathImagen,cv2.COLOR_BGR2RGB)
    imagenbinaria=cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
    #if(imagenbinaria>220):
    cv2.imwrite(pathImagenOut,imagenbinaria)