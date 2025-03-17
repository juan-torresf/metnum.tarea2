import cv2, numpy as np

# Cargar la imagen en escala de grises
imagen = cv2.imread(r"C:\Users\jgpca\Downloads\uanl\ib\semestre vol.IV\METNUM\tarea2\a.png", cv2.IMREAD_GRAYSCALE)

# Aplicar binarización invertida
_, imagen_binarizada = cv2.threshold(imagen, 79, 255, cv2.THRESH_BINARY_INV)

kernel = np.ones((3,3), np.uint8)  # Puedes probar con (2,2) o (3,3) según el grosor deseado

# Aplicar erosión para adelgazar las áreas blancas
imagen_erosionada = cv2.erode(imagen_binarizada, kernel, iterations=1)

# Guardar la imagen procesada
cv2.imwrite(r"C:\Users\jgpca\Downloads\uanl\ib\semestre vol.IV\METNUM\tarea2\ab.png", imagen_binarizada)

print("Imagen binarizada invertida guardada como 'imagen_binarizada.jpg'")
