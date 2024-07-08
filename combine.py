import cv2
import dlib
import numpy as np

# Initialize the hand tracker
hand_tracker = HandTracker()

# Initialize the eye blinking detection
eye_detector = EyeDetector()

# Open the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Apply the hand tracker to the frame
    hand_positions = hand_tracker.detect(frame)

    # Apply the eye blinking detection to the frame
    eye_blinking = eye_detector.detect(frame)

    # Combine the results
    output = {
        "hand_positions": hand_positions,
        "eye_blinking": eye_blinking
    }

    # Display the output
    cv2.imshow("Output", frame)

    # Wait for key press
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# Release the resources
cap.release()
cv2.destroyAllWindows()
