import numpy # Used to perform quickl mathematical operations on an array
from cv2 import cv2 # Used for image processing

# Creates an array [0:26]
n = numpy.arange(27)

# Can reshape the data set for different layouts
newN = n.reshape(3, 3, 3)
print(n)

#
imageFilepath = r"data\smallgray.png"
# Import image as an array
# the flag after the filepath for image, will decide the color of the image ( 1 = BGR(RGB) and 0 = grayscale)
image = cv2.imread(imageFilepath, 1) # works with error 
print(image)

# Getting specific pixel values - slicing
# image_array[x-axis(row index), y-axis(columns)]
print(image[2, 4])

# Itorating through a numpy array
for i in image:
    print(i)

# .flat - lets you acces all the array values in succession
for i in image.flat:
    print(i)

# stocking 2 numpy arrays
# Create new array by stacking 2 or more arrays - the second array will be under first
# Must pass a tuple in .hstack (hight stack)
newArr = numpy.hstack((image, image))
# Create new array by stacking 2 or more arrays - the second array will be next to the first on the right of first
# Must pass a tuple in .vstack (vertical stack)
newArr = numpy.vstack((image, image))
