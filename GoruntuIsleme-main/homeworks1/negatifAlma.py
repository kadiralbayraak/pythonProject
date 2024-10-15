import cv2
import numpy as np

image = cv2.imread('images/picture1.jpg')
negative_image = 255 - image
cv2.imshow('Original Image', image)
cv2.imshow('Negative Image', negative_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('sonucFoto/negative_image.jpg', negative_image)
