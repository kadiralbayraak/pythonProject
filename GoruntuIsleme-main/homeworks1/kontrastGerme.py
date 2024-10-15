import cv2
import numpy as np

image = cv2.imread('images/picture1.jpg', cv2.IMREAD_GRAYSCALE)

# Görüntünün minimum ve maksimum değerlerini bul
min_val = np.min(image)
max_val = np.max(image)

# Kontrast germe işlemi
stretched_image = cv2.normalize(image, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('Original Image', image)
cv2.imshow('Stretched Image', stretched_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('sonucFoto/stretched_image.jpg', stretched_image)
