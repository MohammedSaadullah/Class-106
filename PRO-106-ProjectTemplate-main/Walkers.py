import cv2

# Load the cascade classifier file
body_classifier = cv2.CascadeClassifier('path/to/your/cascade_classifier_file.xml')

# Initialize the video capture
cap = cv2.VideoCapture('path/to/your/video_file.mp4')

while True:
    # Capture a frame from the video
    ret, frame = cap.read()

    # If the frame was not captured successfully, break the loop
    if not ret:
        break

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect bodies in the frame
    bodies = body_classifier.detectMultiScale(gray)

    # Draw rectangles around the detected bodies
    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow('frame', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy all windows
cap.release()
cv2.destroyAllWindows()