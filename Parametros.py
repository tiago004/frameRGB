##busco en quw rango esta los identificadores, camibnaod un posible rango de RGB
##si tomo una foto ya sea con "TomarFotos" o  (Screen Capture) para ver en paint, puedo ver mas o menos el rango del color
## existen rangos altos y bajo ejemplo R-H y R-L
import cv2
import numpy as np
import os
def nothing(x):
    pass

cv2.namedWindow("Trackbars")

desiredWidth=320
desiredheight=240
cv2.resizeWindow("Trackbars", desiredWidth,desiredheight)
cv2.createTrackbar("R-L","Trackbars",0,255,nothing)
cv2.createTrackbar("G-L","Trackbars",0,255,nothing)
cv2.createTrackbar("B-L","Trackbars",0,255,nothing)
cv2.createTrackbar("R-H","Trackbars",0,255,nothing)
cv2.createTrackbar("G-H","Trackbars",0,255,nothing)
cv2.createTrackbar("B-H","Trackbars",0,255,nothing)

cap=cv2.VideoCapture(0)
while True:
    ret, frame= cap.read()


    hsv= cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)

    r_h=cv2.getTrackbarPos("R-H","Trackbars")
    g_h=cv2.getTrackbarPos("G-H","Trackbars")
    b_h=cv2.getTrackbarPos("B-H","Trackbars")
    r_l=cv2.getTrackbarPos("R-L","Trackbars")
    g_l=cv2.getTrackbarPos("G-L","Trackbars")
    b_l=cv2.getTrackbarPos("B-L","Trackbars")

    lower_color=np.array([r_l, g_l,b_l])#pro barras
    upper_color=np.array([r_h, g_h,b_h])# por barras
    #lower_color = np.array([20, 102, 16])## valores fijos
    #upper_color = np.array([72, 139, 75])## valores fijos
    mask=cv2.inRange(hsv,lower_color,upper_color)
    blur = cv2.blur(mask, (4, 4))
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("frame",frame)
    cv2.imshow("mask",mask)
    cv2.imshow("result",result)
    cv2.imshow("hsv",hsv)
    cv2.imshow("blur", blur)

    key=cv2.waitKey(1)
    if key==27:
        break
cap.release()
cv2.destroyAllWindows()