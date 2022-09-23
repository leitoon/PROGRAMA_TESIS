import cv2 

cam = cv2.VideoCapture(0) #Defino el puerto de la camara, en este caso cuando se conecta al puerto 1 ya que es una camara externa
while True:
    ret, frame = cam.read() #leo la camara
    if not ret:
        print("No se encontro un puerto para la cámara")
        break
    img=cv2.line(frame,(320,0),(320,480),(255,0,0),5) #Genero linea en la mitad de la cámara para ajustar el láser
    cv2.imshow('Linea guia',img)#Nombre de la ventana 
    k=cv2.waitKey(1) #waitKey permite mantener la ventana de la aplicación x tiempo, en este caso esta condicionado por ESC y SPACE
    if k%256 == 49: #si es igual a 1 se cierra la app
       print("Fin de la aplicación")
       break
cam.release() #release libera el bloqueo
cv2.destroyAllWindows() #Cierra la ventana