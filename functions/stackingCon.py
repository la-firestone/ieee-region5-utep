import cv2
import numpy as np

img1 = cv2.imread('C:/Users/bryan/PycharmProjects/pythonProject/Resources/quack.png',0)
img2 = cv2.imread('C:/Users/bryan/PycharmProjects/pythonProject/Resources/quack.png',0)
# img2 = cv2.imread('C:/Users/bryan/OneDrive - University of Texas at El Paso/Pictures/quack.png')
print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1, (0, 0), None, 0.5, 0.5)
img2 = cv2.resize(img2, (0, 0), None, 0.5, 0.5)

# img1 = cv2.cvtColor(img1, cv2.COLOR_GRAY2BGR)

hor = np.hstack((img1, img2))
ver = np.vstack((img1, img2))

cv2.imshow('Vertical', ver)
cv2.imshow('Horizontal', hor)

cv2.waitKey(0)
