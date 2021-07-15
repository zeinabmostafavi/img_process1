import cv2

# _____________img1________________________
image1 = cv2.imread('q1_2/1.jpg')
image1 = cv2.cvtColor(image1, cv2.COLOR_RGB2GRAY)
# _____________img2________________________
image2 = cv2.imread('q1_2/2.jpg')
image2 = cv2.cvtColor(image2, cv2.COLOR_RGB2GRAY)


# _____________img1________________________
rows = image1.shape[0]
cols = image1.shape[1]
# _____________img2________________________
rows2 = image2.shape[0]
cols2 = image2.shape[1]

# __________process_________________
for i in range(rows):
    for j in range(cols):
        image1[i, j] = 255-image1[i, j]
# _______process__________________
for i in range(rows2):
    for j in range(cols2):
        image2[i, j] = 255-image2[i, j]


cv2.imshow('image1', image1)
cv2.imshow('image2', image2)
cv2.waitKey()
