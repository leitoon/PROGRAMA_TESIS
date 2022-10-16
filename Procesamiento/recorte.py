import cv2
import os
# Leemos la imagen de entrada, la mostramos e imprimimos sus dimensiones.
#se declara varible que contien la carpeta donde se tienes las imagenes capturadas
pathInput = "D:\\PROGRAMA_TESIS\\segmentada2"
#nombreImagenes me permite conocer el nombre de los archivos que se tienen en la carpeta de pathInput 
nombreImagenes = os.listdir(pathInput)
#se declara varible que contien la carpeta donde se guardaran las imagenes segmentadas
pathOutput = "D:\\PROGRAMA_TESIS\\Recorte_imagen"
cont=0

for i in range(len(nombreImagenes)):
    pathImagen = os.path.join(pathInput,nombreImagenes[i])
    #pathImagenOut contiene la dirección y nombre de cada imagen contenidas que se almacenara en segmentada
    pathImagenOut = os.path.join(pathOutput,nombreImagenes[i])
    imagen = cv2.imread(pathImagen) #leo las imagenes
    cropped=(imagen[38:443, 322:374]) #recorto la imagen 
    cv2.imwrite(pathImagenOut,cropped) #almaceno el recorte

