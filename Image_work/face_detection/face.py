import cv2
from cv2 import cv2

# Create a face cascade object - the interpreter
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Search for a face in an image
img = cv2.imread("news.jpg", 1)
# Greyscale images are better for face recognition
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Will return a list of coordionates [upper_left_of_face_x, upper_left_of_face_y, face_width, face_length]
# To increase or decrease precision, must increase and decrease scaleFactor
faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)

# Draw a rectangle in the image around the face
for x, y, w, h in faces:
    #
    img_new = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)

cv2.imshow("Face", img_new)
cv2.imshow("Gray", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()