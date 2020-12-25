"""
    This app will allow users using any 3rd party camera that connects to a computer to track motion, once motion is detected
    the opbject that's moving will bi highlighted using a rectangle on the video feed and will change the status that there is
    detected motion in the room and save the times this has happened.

    When setting up the system the first_frame has to be a static image without any moving objects, otherwise it will not be able
    to detect a differnece
"""
import cv2, numpy
from pandas import pandas
from datetime import datetime
from cv2 import cv2

first_frame = None
contour_limit = 1000

statuses = [None, None]
time_stamps = [[], []]
fileName = r'logs\times.csv'


video = cv2.VideoCapture(0)# 0 for primary cam of comp

def gray_out(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


while True:
    # Get the frame
    check, frame = video.read()
    status = 0
    # Apply grayscale
    gray_img = gray_out(frame)
    # Blur the img to improve motion detection accuracy
    gray_img = cv2.GaussianBlur(gray_img, (21, 21), 0)

    if first_frame is None:
        first_frame = gray_img
        continue

    # Will calculate the difference between the 2 frames and the difference will be in a lighter color
    delta_frame = cv2.absdiff(gray_img, first_frame)
    cv2.imshow("Delta", delta_frame)

    # Change the image to where all the areas that are in motion or the pixel value us above 
    # a certain thershold will be set to a specific value (ex. if a pixel is above 50 change it to white, the rest to black)
    # Use the .threshold (image, threshold limit, what color to change to, threshold method (check doc))
    # It returns a tuple -> (value for threshold, frame)
    threshold_delta_frame = cv2.threshold(delta_frame, 50, 255, cv2.THRESH_BINARY)[1]

    # Smooth threshold frame
    threshold_delta_frame = cv2.dilate(threshold_delta_frame, None, iterations=5)

    # Get the contours of the frame -> find the areas of movment and return the coordionates
    (cnts, _) = cv2.findContours(threshold_delta_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check all the found areas and make sure they are above a certain pixel size to filter out
    # unwanted sections (small areas that have changed color due to light changes)
    for contour in cnts:
        # if a contourd area is less than n pixes, , do not inclood it
        if cv2.contourArea(contour) < contour_limit:
            continue
        status = 1
        # get the rectangle frame info from the contour
        (x, y, w, h) = cv2.boundingRect(contour)
        # draw a rectangle on the initieal nonporcessed frame
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 10), 2)
    # Add current status to statuses for comparison
    statuses.append(status)
    # check to see if any moption / change in status has occured
    if statuses[-1] == 1 and statuses[-2] == 0:
        time_stamps[0].append(datetime.now())
    elif statuses[-1] == 0 and statuses[-2] == 1:
        time_stamps[1].append(datetime.now())
    elif len(statuses) > 10:
        statuses = statuses[-4:]

    # display image
    cv2.imshow("thresh", threshold_delta_frame)
    cv2.imshow("Live", frame)
    # key can be used to specify a key to exit window
    key = cv2.waitKey(1)
    # if user presses eskape
    if key == ord(chr(27)):
        # In case an interrup happens while there is motion, register the exit time as end of motion
        if statuses[-1] == 1:
            time_stamps[1].append(datetime.now())
        break

# Release the camera and close all windows of imshow
video.release() # release the camera
cv2.destroyAllWindows() # Close the windows

# save the time stamps to a file using pandas
times = {'motion_start' : time_stamps[0], 'motion_stop' : time_stamps[1]}
df = pandas.DataFrame(times)
df.to_csv(fileName)    
