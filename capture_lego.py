import cv2
import numpy as np
import time # <-- Import the time library
import os

def capture_and_process():
    print("Initializing webcam...")
    cap = cv2.VideoCapture(0)

    # --- THIS IS THE FIX ---
    # Give the camera 2 seconds to auto-adjust its exposure and focus.
    print("Letting camera adjust...")
    time.sleep(2)
    # ---------------------

    if not cap.isOpened():
        raise IOError("Cannot open webcam. Check permissions and connections.")

    print("Capturing frame...")
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture frame from webcam.")
        return

    # --- Add this line to debug ---
    # It saves the raw image before processing. If this image is all white,
    # the problem is definitely camera exposure.
    cv2.imwrite("debug_raw_capture.png", frame)
    print("Saved a raw debug image: 'debug_raw_capture.png'")
    # ----------------------------

    print("Processing image...")
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (7, 7), 0)

    # === IMPORTANT CHECK ===
    # Make sure these Canny numbers are the EXACT same numbers
    # that looked good in your live_debug.py script!
    edges = cv2.Canny(blurred, 10, 70)
    # =======================

    home_dir = os.path.expanduser("~")
    output_path = os.path.join(home_dir, "ComfyUI/input/lego_silhouette.png")

    cv2.imwrite(output_path, edges)
    print(f"✅ Silhouette saved successfully to: {output_path}")

if __name__ == "__main__":
    capture_and_process()