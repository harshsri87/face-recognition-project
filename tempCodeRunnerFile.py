
    exit()

print("Webcam is on. Press 'q' to quit.")

while True:
    success, frame = cap.read()  # Read a frame from webcam