import cv2
import numpy as np
import winsound

# Initialize OpenCV's face detector (Haar Cascade classifier)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Define a function to detect if a person is sleeping


def detect_sleeping(frame):
    # Convert the frame to grayscale for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces using OpenCV's face detector
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # If no faces are detected, return False
    if len(faces) == 0:
        return False

    # Loop through the detected faces
    for (x, y, w, h) in faces:
        # Extract the face region from the frame
        roi_gray = gray[y:y+h, x:x+w]

        # Calculate the standard deviation of the face region to determine if the person's eyes are closed
        std = np.std(roi_gray)

        # If the standard deviation is below the threshold, the person is sleeping
        if std < 37:
            return True

    # If none of the faces are sleeping, return False
    return False

# Define a function to play an alarm sound


def play_alarm():
    # Play the alarm sound using the built-in Windows sound player
    frequency = 4000  # Set frequency to 2500 Hertz
    duration = 100  # Set duration to 5000 milliseconds (5 seconds)
    winsound.Beep(frequency, duration)


# Open the video capture device
cap = cv2.VideoCapture(0)

# Start processing frames from the video capture device
while True:
    # Read a frame from the video capture device
    ret, frame = cap.read()

    # If the frame is not captured, break the loop
    if not ret:
        break

    # Detect if the person is sleeping
    sleeping = detect_sleeping(frame)

    # If the person is sleeping, play an alarm sound to wake them up
    if sleeping:
        play_alarm()
        # Draw a red rectangle on the video stream
        cv2.rectangle(frame, (0, 0), (50, 50), (0, 0, 255), -1)

    # Detect faces using OpenCV's face detector and display the video stream with bounding boxes around detected faces
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
    cv2.imshow('Frame', frame)

    # If the 'q' key is pressed, break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and destroy all windows
cap.release()
cv2.destroyAllWindows()
