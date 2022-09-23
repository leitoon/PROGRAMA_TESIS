from email.mime import image
import cv2 
import numpy as np
from matplotlib import pyplot as plt
import mahotas as mt
img=cv2.imread('D:\\PROGRAMA_TESIS\\Segmentada\\imagen2.jpg',0)
pathOutput = "D:\\PROGRAMA_TESIS\\segmentada2\\imagensegmentada2.jpg"

def solopixel(imagen):
    imgsegmentada2=imagen       
    imagenW=imagen.shape[1]
    imagenH=imagen.shape[0]
    cnt=0
    for i in range(imagenH):
        cnt=0
        for j in range(imagenW):
            if imgsegmentada2[i][j]==255:
                #print('pixel blanco encontrado')
                cnt=cnt+1
                if cnt>1:
                    #print('modificando pixel blanco encontrado')
                    imgsegmentada2[i][j]=0
    return imgsegmentada2
img2=solopixel(img)
cv2.imwrite(pathOutput,img2)





