import cv2 
import numpy as np
from matplotlib import pyplot as plt


imgGray=cv2.imread('D:\\PROGRAMA_TESIS\\imagenes_procesamiento\\imagen28.jpg',0)
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
datoFinal=verificacion_laser(imgGray)
print(datoFinal)