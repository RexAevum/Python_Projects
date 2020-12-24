import cv2, time
from cv2 import cv2

# get the idoe either from a file or a camera
video = cv2.VideoCapture(0) # .VideoCapture({int to which cammera to use or str of video file})

frameCount = 0

while True:
    frameCount = frameCount + 1
    check, frame = video.read()
    # check - checks if camera/video is working
    # frame - first image that the camera captures
    print(check, frame)
    # a frame is a normal image
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    time.sleep(0)
    cv2.imshow("", frame)

    # Disconnects from the camera
    key = cv2.waitKey(1) #wait for n amount of milliseconds before continuing 

    #
    if  key==ord(chr(27)): # chr(27) == Esc key
        break

print(frameCount)
video.release()
cv2.destroyAllWindows()