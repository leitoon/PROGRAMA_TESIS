import numpy as np
import cv2
import glob
#Determino las dimensiones del tablero, contando las aristas
DIMX=9;
DIMY=6;
square_size=27

# termination criterio
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
 
# preparar puntos de objeto, como (0,0,0,0), (1,0,0,0), (2,0,0,0)...., (6,5,0)
objp = np.zeros((DIMY*DIMX,3), np.float32)
objp[:,:2] = np.mgrid[0:DIMX,0:DIMY].T.reshape(-1,2)
objp*=square_size

print(objp)
# Arrays para almacenar puntos de objeto y puntos de imagen de todas las imágenes.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
 
images = glob.glob('*.jpg')
 
for fname in images:
  img = cv2.imread(fname) #leo la imagen
  gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #la convierto a escala de grises
 
  # Encuentra las esquinas del tablero de ajedrez
  ret, corners = cv2.findChessboardCorners(gray, (DIMY,DIMX),None)
 
  # Si se encuentran, añada puntos de objeto, puntos de imagen (después de refinarlos)
  if ret == True:
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray,corners,(8,8),(-1,-1),criteria)
    imgpoints.append(corners2)
 
    # Dibuja y muestra las esquinas
    img = cv2.drawChessboardCorners(img, (DIMX,DIMY), corners2,ret)
    cv2.imshow('img',img)
    cv2.waitKey(1000)

	
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)
print(mtx)
cv2.destroyAllWindows()
	
