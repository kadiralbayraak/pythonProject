import cv2
import numpy as np

image = cv2.imread('images/picture1.jpg', cv2.IMREAD_GRAYSCALE)

# İlk dilim: 50 ile 100 arasındaki piksel değerlerini seç
lower_bound1 = 50
upper_bound1 = 100
mask1 = cv2.inRange(image, lower_bound1, upper_bound1)

# İkinci dilim: 150 ile 200 arasındaki piksel değerlerini seç
lower_bound2 = 150
upper_bound2 = 200
mask2 = cv2.inRange(image, lower_bound2, upper_bound2)

# İlk dilimi görüntüde seç
result1 = cv2.bitwise_and(image, image, mask=mask1)

# İkinci dilimi görüntüde seç
result2 = cv2.bitwise_and(image, image, mask=mask2)

# Orijinal görüntü ve dilimleri göster
cv2.imshow('Original Image', image)
cv2.imshow('Slice 1 (50-100)', result1)
cv2.imshow('Slice 2 (150-200)', result2)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('sonucFoto/slice1_50_100.jpg', result1)
cv2.imwrite('sonucFoto/slice2_150_200.jpg', result2)
