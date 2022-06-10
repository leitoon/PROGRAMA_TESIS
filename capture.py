#PROGRAMA PARA CALIBRAR LA CAMARA
import cv2 

cam = cv2.VideoCapture(1) #Defino el puerto de la camara, en este caso cuando se conecta al puerto 1 ya que es una camara externa

cv2.namedWindow("test") #Nombre de la ventana que visualiza a la camara
 
img_counter = 0 #Genero la variable img_counter para que vaya contando
#Se crea un ciclo while para almacenar las imagenes, si no encuentra la camara el puerto de la camara, no funciona
while True:
    ret, frame = cam.read()
    if not ret:
        print("No se encontro un puerto para la cámara")
        break
    cv2.imshow("test", frame)
 
    k = cv2.waitKey(1) #waitKey permite mantener la ventana de la aplicación x tiempo, en este caso esta condicionado por ESC y SPACE
    if k%256 == 27:
        # Si se presiona ESC
        print("Fin de la aplicación")
        break
    elif k%256 == 32:
        # Si se presiona SPACE  guarda la imagen
        img_name = "imagen{}.jpg".format(img_counter)
        cv2.imwrite(img_name, frame)
        print("{} guardada!".format(img_name))
        img_counter += 1
 
cam.release() #release libera el bloqueo
 
cv2.destroyAllWindows() #Cierra la ventana