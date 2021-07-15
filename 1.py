import cv2
import numpy as np

image = np.ones((800, 800))*255

rows, columns = image.shape

for i in range(rows):
    for j in range(columns):
        if (i // 100) % 2 == 0:
            if (j // 100) % 2 == 1:
                image[i, j] = 0
        else:
            if (j // 100) % 2 == 0:
                image[i, j] = 0
cv2.imshow('Chess', image)
cv2.waitKey()
