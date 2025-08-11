import cv2

# Load OpenCV's built-in Haar cascade classifier for face detection
TrainedData = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Check if the cascade loaded successfully
if TrainedData.empty():
    print("Error: Could not load Haar cascade. Check the file path.")
    exit()

# Start video capture from the default webcam (0)
cap = cv2.VideoCapture(0)

# Check if the webcam is accessible
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Webcam is on. Press 'q' to quit.")

while True:
    success, frame = cap.read()  # Read a frame from webcam
    if not success:
        print("Failed to grab frame.")
        break

    # Convert to grayscale for face detection
    Grayimg = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    facecoordinates = TrainedData.detectMultiScale(Grayimg)

    # Draw rectangles around detected faces
    for (x, y, w, h) in facecoordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the frame
    cv2.imshow("Webcam Face Detection", frame)

    # Exit loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close all windows
cap.release()
cv2.destroyAllWindows()
