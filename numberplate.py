import cv2

numberCascade = cv2.CascadeClassifier("Resource/haarcascade_russian_plate_number.xml")
print('Package imported')
color=255,0,255
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(10, 50)

while True:
    success, img = cap.read()

    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    numberPlate = numberCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlate:
        area=w*h
        if area>500:
            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
            imgRoi=img[y:y+h,x:x+w]
            cv2.imshow("ROI",imgRoi)
    cv2.imshow("Result", img)
    #cv2.waitKey(0)
    #cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
