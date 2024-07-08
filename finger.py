import cv2
import numpy as np

def empty(a):
    pass

# Capture video from the webcam
cap = cv2.VideoCapture(0)

# Create a black image with the same size as the frame
height, width = cap.get(cv2.CAP_PROP_FRAME_HEIGHT), cap.get(cv2.CAP_PROP_FRAME_WIDTH)
background = np.zeros((int(height), int(width), 3), np.uint8)

# Define trackbars for background subtraction
cv2.namedWindow("Parameters")
cv2.resizeWindow("Parameters", 640, 240)
cv2.createTrackbar("Threshold", "Parameters", 75, 255, empty)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian Blur filter
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Subtract the background
    subtracted = cv2.absdiff(blur, background)

    # Threshold the subtracted frame to obtain binary image
    threshold = cv2.getTrackbarPos("Threshold", "Parameters")
    _, thresholded = cv2.threshold(subtracted, threshold, 255, cv2.THRESH_BINARY)

    # Find contours in the binary image
    contours, _ = cv2.findCont