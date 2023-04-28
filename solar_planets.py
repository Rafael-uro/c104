import cv2

img = cv2.imread("solar-system.jpg")


text = "Sol"
text1 = "Mercurio"
text2 = "Venus"
text3 = "Terra"
text4 = "Marte"
text5 = "Jupiter"
text6 = "Saturno"
text7 = "Urano"
text8 = "Netuno"

cv2.putText(img, text, (100,80), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 1.6, color=(0,0,255))
cv2.putText(img, text1, (100,180), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text2, (200,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text3, (300,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text4, (400,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text5, (500,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text6, (800,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text7, (1000,155), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))
cv2.putText(img, text8, (1200,190), fontFace=cv2.FONT_HERSHEY_COMPLEX_SMALL, fontScale = 0.6, color=(255,255,255))

cv2.imwrite("Solar_systemwithname.jpg",img)
cv2.imshow("resultado", img)
cv2.waitKey(0)