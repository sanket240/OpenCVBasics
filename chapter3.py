import cv2
img=cv2.imread("Resource/rohit-sharma_1603803462.jpg")
print(img.shape)

imgResize=cv2.resize(img,(1920,1080))
print(imgResize.shape)

imgCropped =img[0:200,200:500]
cv2.imshow("Image",imgResize)
cv2.imshow("Image Cropped",imgCropped)
cv2.waitKey(0)