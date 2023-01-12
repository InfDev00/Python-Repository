import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye.xml')

ff = np.fromfile(r'C:\Users\ugane\PycharmProjects\pythonProject\human.jpg', np.uint8)
img = cv2.imdecode(ff, cv2.IMREAD_UNCHANGED)
ori_img = cv2.resize(img, dsize=(0,0), fx=1.0 , fy=1.0, interpolation=cv2.INTER_LINEAR)
img = ori_img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#검출을 위해서는 회색으로 만들어야 함

faces = face_cascade.detectMultiScale(gray, 1.2, 5)#1.2 = 감도, 5=최소중복개수
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0,0),2)#얼굴 사각형 생성

    roi_gray = gray[y:y+h, x:x+w]#눈 추출을 위해 다시 회색
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.2)#감도 1.2
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex,ey), (ex+ew, ey+eh), (0, 255, 0), 2)#눈 사각형 생성

cv2.imshow('face_find', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#######그림으로 변환
img = ori_img.copy()
def onChange(pos):
    pass

cv2.namedWindow("Trackbar Windows")
cv2.createTrackbar("sigma_s", "Trackbar Windows", 0, 200, onChange)
cv2.createTrackbar("sigma_r", "Trackbar Windows", 0, 100, onChange)

cv2.setTrackbarPos('sigma_s', "Trackbar Windows", 100)
cv2.setTrackbarPos('sigma_r', "Trackbar Windows", 10)

while True:

    if cv2.waitKey(100) == ord('q'):
        break

    sigma_s_value = cv2.getTrackbarPos("sigma_s", "Trackbar Windows")
    sigma_r_value = cv2.getTrackbarPos("sigma_r", "Trackbar Windows")/100.0

    print("sigma_s_value: ", sigma_s_value)
    print("sigma_r_value: ", sigma_r_value)

    cartoon_img = cv2.stylization(img, sigma_s=sigma_s_value, sigma_r=sigma_r_value)

    cv2.imshow('Trackbar Windows', cartoon_img)

cv2.destroyAllWindows()