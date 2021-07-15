import cv2


image = cv2.imread('q1_4/4.jpg')
image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

rows = image.shape[0]
cols = image.shape[1]

# _________process________________
for i in range(rows):
    for j in range(cols):
        if image[i, j] > 50:
            image[i, j] = 255


cv2.imshow('smile', image)
cv2.waitKey()
