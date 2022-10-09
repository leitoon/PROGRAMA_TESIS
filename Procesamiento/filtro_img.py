import numpy as np 
import cv2
import mahotas as mt
import os
import pandas as pd
#se declara varible que contien la carpeta donde se tienes las imagenes capturadas
pathInput = "D:\\PROGRAMA_TESIS\\Recorte_imagen"
#nombreImagenes me permite conocer el nombre de los archivos que se tienen en la carpeta de pathInput 
nombreImagenes = os.listdir(pathInput)
#se declara varible que contien la carpeta donde se guardaran las imagenes segmentadas
pathOutput = "D:\\PROGRAMA_TESIS\\segmentadaFinal"
#Se crea ciclo for del tamaño de elementos de las imagenes_procesamiento para 
#Que recorra todas las imagenes y haga el procesamiento

for i in range(len(nombreImagenes)):
    #pathImagen contiene la dirección y nombre de cada imagen contenidas en imagenes_procesamiento
    pathImagen = os.path.join(pathInput,nombreImagenes[i])
    #pathImagenOut contiene la dirección y nombre de cada imagen contenidas que se almacenara en segmentada
    pathImagenOut = os.path.join(pathOutput,nombreImagenes[i])
    # imagen se creo para pasar las imagenes de imagenes_procesamiento a RGB
    imagen = cv2.imread(pathImagen,cv2.COLOR_BGR2RGB)
    ### FILTRO GAUSSIANO
    imagen= cv2.GaussianBlur( imagen,(5,5),0.5) 
    #imagenGray se creo para pasar las imagenes de imagenes_procesamiento a escalas de grises
    imagenGray = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
    #threshold crea un umbral Si el valor del píxel es menor que el umbral, se establece en 0; de lo contrario, se establece en un valor máximo
    ret, imagenBinaria = cv2.threshold(imagenGray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    #kernel 
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10))
    kernel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(10,10)) 
    #Operaacion morfologica elimina el ruido de la imagen
    imagenBinaria = cv2.morphologyEx(imagenBinaria,cv2.MORPH_CLOSE,kernel)
    imagenBinaria = cv2.morphologyEx(imagenBinaria,cv2.MORPH_ERODE,kernel2)
    imagenBinaria = mt.thin(imagenBinaria)*255
    #Se escoje la imagen binaria y se le agrea la mascara del procesamiento
    imagenSegmentada = cv2.bitwise_and(imagenGray,imagenGray,mask=imagenBinaria)
    #se guardan las imagenes esqueletizadas
    cv2.imwrite(pathImagenOut,imagenBinaria)
    # # Visualizacion 
    imagenRectangulo = np.zeros((imagenBinaria.shape[0],imagenBinaria.shape[1]),dtype=np.uint8)
