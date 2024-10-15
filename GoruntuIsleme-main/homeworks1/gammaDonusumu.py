import cv2
import numpy as np

image = cv2.imread('images/picture1.jpg')

gamma = 2.0  # 1'den küçük olursa parlaklık artar, 1'den büyük olursa parlaklık azalır

# Gamma dönüşüm fonksiyonu oluştur
inv_gamma = 1.0 / gamma
table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

# Görüntüye gamma dönüşümünü uygula
gamma_corrected = cv2.LUT(image, table)

# Orijinal ve Gamma düzeltilmiş görüntüyü göster
cv2.imshow('Original Image', image)
cv2.imshow('Gamma Corrected Image', gamma_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('sonucFoto/gamma_corrected_image.jpg', gamma_corrected)
