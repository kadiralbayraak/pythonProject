import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('images/picture1.jpg', cv2.IMREAD_GRAYSCALE)

hist = cv2.calcHist([image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Original Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(hist)
plt.xlim([0, 256])
plt.show()

cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Kontrast germe işlemi
stretched_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

# Kontrastı gerilmiş görüntü için histogram çıkarma
hist_stretched = cv2.calcHist([stretched_image], [0], None, [256], [0, 256])

plt.figure()
plt.title("Stretched Image Histogram")
plt.xlabel("Pixel Value")
plt.ylabel("Frequency")
plt.plot(hist_stretched)
plt.xlim([0, 256])
plt.show()

cv2.imshow('Stretched Image', stretched_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('sonucFoto/stretched_image.jpg', stretched_image)

