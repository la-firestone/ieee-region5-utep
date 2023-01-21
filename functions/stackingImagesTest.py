import cv2
import numpy as np
from myUti import stackImages


frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)

while True:
    success, img = cap.read()
    cv2.imshow("Result", img)

    kernel = np.ones((5,5),np.uint8)
    print(kernel)

    #path = r'C:\Users\bryan\PycharmProjects\pythonProject\Resources\quack.png'
    # path = "Resources/quack.png"
    #img = cv2.imread(path)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
    imgCanny = cv2.Canny(imgBlur,100,200)
    imgDilation = cv2.dilate(imgCanny,kernel,iterations=2)
    imgEroded = cv2.erode(imgDilation,kernel,iterations=2)

    imgBlank = np.zeros((200,200),np.uint8)

    StackedImages = stackImages(0.3,([img,imgGray,imgBlur, imgCanny,imgDilation,imgEroded],
                                     [imgCanny,imgDilation,imgEroded, img,imgGray,imgBlur],
                                     [img, imgGray, imgBlur, imgCanny, imgDilation, imgEroded],
                                     [imgCanny, imgDilation, imgEroded, img, imgGray, imgBlur]))
    cv2.imshow("Stacked Images", StackedImages)

    # cv2.imshow("Lena",img)
    # cv2.imshow("GrayScale",imgGray)
    # cv2.imshow("Img Blur",imgBlur)
    # cv2.imshow("Img Canny",imgCanny)
    # cv2.imshow("Img Dilation",imgDilation)
    # cv2.imshow("Img Erosion",imgEroded)
    # cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
