import numpy as np 
import cv2
import mahotas as mt
import os
import pandas as pd
from math import tan

#se declara varible que contien la carpeta donde se tienes las imagenes capturadas
pathInput = "D:\\PROGRAMA_TESIS\\Recorte_imagen"
#nombreImagenes me permite conocer el nombre de los archivos que se tienen en la carpeta de pathInput 
nombreImagenes = os.listdir(pathInput)
#se declara varible que contien la carpeta donde se guardaran las imagenes segmentadas
pathOutput = "D:\\PROGRAMA_TESIS\\segmentada"
#Se crea ciclo for del tamaño de elementos de las imagenes_procesamiento para 
#Que recorra todas las imagenes y haga el procesamiento
def coordenadasxy(imagen):
    imagenHeight = imagen.shape[0]
    imagenWidth = imagen.shape[1]
    CX = int(imagenHeight/2)
    CY = int(imagenWidth/2)
    CoordenadasPixeles = [] 
    for i in range(imagenHeight):
        for j in range(imagenWidth):
            if imagen[i][j] != 0:
                features = { # caracteristicas cambiando el centro y modificando la distancia al centro
                    "x": (j - CY),
                    "y": (CX - i)
                }
                # features = {
                #     "x": (i),
                #     "y": (j)
                # }
                CoordenadasPixeles.append(features)
    return CoordenadasPixeles

def coordenadasXYZ(coordenasxy):
    #Datos constante Calculados del experimento 
    angulo=69.44
    angulo=np.radians(angulo)
    f=2087
    b=7.5
    cot=1/tan(angulo)

    coordenadasXYZ = []
    for i in range(len(coordenasxy)):
        caracteristicasPixel = coordenasxy[i]
        x = caracteristicasPixel["x"]
        y = caracteristicasPixel["y"]

        
        

        X = (b/(f*(cot)-x))*x
        Y = (b/(f*(cot)-x))*y
        Z = (b/(cot)-x)

        features = {
            "X": X,
            "Y": Y,
            "Z": Z
        }
        coordenadasXYZ.append(features)
    return coordenadasXYZ

for i in range(len(nombreImagenes)):
    #pathImagen contiene la dirección y nombre de cada imagen contenidas en imagenes_procesamiento
    pathImagen = os.path.join(pathInput,nombreImagenes[i])
    #pathImagenOut contiene la dirección y nombre de cada imagen contenidas que se almacenara en segmentada
    pathImagenOut = os.path.join(pathOutput,nombreImagenes[i])
    # imagen se creo para pasar las imagenes de imagenes_procesamiento a RGB
    
    imagen = cv2.imread(pathImagen,cv2.COLOR_BGR2RGB)
    #imagenGray se creo para pasar las imagenes de imagenes_procesamiento a escalas de grises
    imagenGray = cv2.cvtColor(imagen,cv2.COLOR_RGB2GRAY)
    imagenGray = cv2.GaussianBlur(imagenGray,(5,5),0.5) # suavizar bordes con filtro gaussiano
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
    ############### Extraccion de caracteristicas ###################
    caracteristicasImagen = coordenadasxy(imagenBinaria)
    print(caracteristicasImagen)
    caracteristicasEspaciales = coordenadasXYZ(caracteristicasImagen)
    # # Creacion del archivo CSV para mesh lab 
    df = pd.DataFrame(caracteristicasEspaciales)
    print(df.head())
    print(df.tail())
    cv2.imwrite(pathImagenOut,imagenBinaria)
    # # Visualizacion 
    imagenRectangulo = np.zeros((imagenBinaria.shape[0],imagenBinaria.shape[1]),dtype=np.uint8)
