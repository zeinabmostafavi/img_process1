import cv2

image = cv2.imread('q1_3/3.jpg')

# _____________resize_____________________
image = cv2.resize(image, (600, 600))
# ____________ratate__________________________
image_rotated = cv2.rotate(image, cv2.ROTATE_180)
# _____________________________________________________


cv2.imshow('smile', image_rotated)
cv2.waitKey()
