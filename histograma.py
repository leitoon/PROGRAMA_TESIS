import cv2 
import numpy as np
from matplotlib import pyplot as plt


def histogramaRGB(imagen):
    imagen = cv2.cvtColor(imagen,cv2.COLOR_BGR2RGB)
    histR = cv2.calcHist([imagen], [0], None, [255], [0, 255])
    histR = 1*((histR-np.min(histR))/(np.max(histR)-np.min(histR)))

    histG = cv2.calcHist([imagen], [1], None, [255], [0, 255])
    histG = 1*((histG-np.min(histG))/(np.max(histG)-np.min(histG)))

    histB = cv2.calcHist([imagen], [2], None, [255], [0, 255])
    histB = 1*((histB-np.min(histB))/(np.max(histB)-np.min(histB)))
    
    fig, ax=plt.subplots(2)
    ax[1].plot(histR, color = 'r')
    ax[1].plot(histG, color = 'g')
    ax[1].plot(histB, color = 'b')
    ax[1].set_title("Histograma R-G-B")
    ax[0].imshow(imagen)
    ax[0].set_title("Imagen")
    ax[0].axis("off")
    plt.show()

def histogramaGray(img):
    height = img.shape[0]
    width  = img.shape[1]
    #valores de histograma normalizados
    hist_1 = cv2.calcHist([img], [0], None, [255], [0, 255])
    hist = 1*((hist_1-np.min(hist_1))/(np.max(hist_1)-np.min(hist_1)))
    
    #valores de histograma vertical normalizados
    profile_W= np.sum(img, axis=1)
    Profile_W = 1*((profile_W-np.min(profile_W))/(np.max(profile_W)-np.min(profile_W)))
    
    #valores de histograma Horizontal normalizados
    profile_H = np.sum(img, axis=0)
    Profile_H = 1*((profile_H-np.min(profile_H))/(np.max(profile_H)-np.min(profile_H)))

    fig, ax=plt.subplots(2,2)
    ax[0,0].imshow(img,cmap='gray' )
    ax[0,0].set_title('Imagen '+ 'W: '+ str(width) + ' H: ' + str(height) )
    ax[0,0].axis('off')
    
    ax[0,1].plot(hist, color ='gray' )
    ax[0,1].set_title('Overall Histogram')
    ax[0,1].set_ylabel('Number of Pixels')

    ax[1,0].plot(Profile_H, color = 'gray')
    ax[1,0].set_title(' Horizontal Profile')
    ax[1,0].set_xlabel('Horizontal Axe')
    ax[1,0].set_ylabel('Cumulative sum of grays')
  
    
    ax[1,1].plot(Profile_W, color = 'gray')
    ax[1,1].set_title(' Vertical Profile')
    ax[1,1].set_xlabel('Vertical Axe')
    ax[1,1].set_ylabel('Cumulative sum of grays')
   
    plt.show()
imgGray=cv2.imread('D:\\PROGRAMA_TESIS\\imagenes_bi\\imagen10.jpg')
histogramaGray(imgGray)