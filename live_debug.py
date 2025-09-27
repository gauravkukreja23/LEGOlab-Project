import cv2
import time

print("Starting live debug script...")
print("Press 'q' on the keyboard while the camera windows are active to quit.")

# Use 0 for the default webcam
cap = cv2.VideoCapture(0)

# Give the camera a moment to initialize and adjust exposure
time.sleep(2)

if not cap.isOpened():
    print("Error: Cannot open webcam. Check if it's connected or being used by another app.")
    exit()

while True:
    # Read a new frame from the webcam
    ret, frame = cap.read()
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break

    # --- Image Processing Pipeline ---

    # 1. Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Apply a blur to reduce noise
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # 3. Perform Canny edge detection
    # These two numbers (50, 150) are the thresholds.
    # This is the most likely place for adjustments!
    canny_edges = cv2.Canny(blurred, 10, 70)

    # --- Display the results ---

    # Show the original, unprocessed camera feed
    cv2.imshow('Original Webcam View', frame)

    # Show what the Canny edge detector is seeing
    cv2.imshow('Canny Edges (The Silhouette)', canny_edges)

    # Wait for a key press. If 'q' is pressed, exit the loop.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture and destroy windows
print("Exiting script.")
cap.release()
cv2.destroyAllWindows()