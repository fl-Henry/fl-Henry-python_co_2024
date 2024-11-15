import cv2
import numpy as np

# Чтение изображения
image = cv2.imread('image.png')

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение порога для бинаризации изображения
ret, thresh_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Поиск контуров
contours, hierarchy = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Отображение контуров
cv2.drawContours(image, contours, -1, (0, 255, 0), 3)  # Рисуем контуры на исходном изображении

# Отображение изображения с контурами
cv2.imshow('Contours', image)
cv2.waitKey(0)
cv2.destroyAllWindows()