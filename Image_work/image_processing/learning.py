from cv2 import cv2

# load image
img = cv2.imread('galaxy.jpg', -1) # 0 for greyscale; 1 for color
print(type(img)) 
print(img.shape) # get resolution list [y, x], where y is height and x is width
print(img.ndim) # how many dimensions

# resize image
# it will resize by getting averages from near by pixels and create a new image of lower resolution
resized_img= cv2.resize(img, (800, 600))

# To resize based on the original to maintain scale, you can divide the existing .shape
# Has to be an int
resized_img_proportional = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))

# Write the new resized image
cv2.imwrite("Galaxy_resized.jpeg", resized_img_proportional)
# Display image in window
cv2.imshow("Boom", resized_img_proportional) # display image
cv2.waitKey(0) # if 0, user can close window with any button
cv2.destroyAllWindows()

# Resize all images in the current folder and save them
import glob

images=glob.glob("*.jpg")

for image in images:
    img=cv2.imread(image,0)
    re=cv2.resize(img,(100,100))
    cv2.imshow("Hey",re)
    cv2.waitKey(500)
    cv2.destroyAllWindows()
    cv2.imwrite("resized_"+image,re)