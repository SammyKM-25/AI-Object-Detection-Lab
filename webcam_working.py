import cv2
from ultralytics import YOLO

print("=" * 50)
print("WEBCAM DETECTION")
print("=" * 50)
print("Instructions:")
print("1. Look at the camera")
print("2. Press 'q' to quit")
print("3. Press 's' to save a screenshot")
print("=" * 50)

# Load model
model = YOLO("yolov8n.pt")

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open webcam!")
    exit()

print("✓ Webcam opened successfully")
print("Press 'q' to quit, 's' to save screenshot")

# Set resolution
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

screenshot_count = 0
frame_count = 0

while True:
    # Read frame
    ret, frame = cap.read()
    
    if not ret:
        print("Error reading frame")
        break
    
    frame_count += 1
    
    # Run detection every 5 frames to make it faster
    if frame_count % 5 == 0:
        results = model(frame, verbose=False)
        if results[0].boxes is not None:
            frame = results[0].plot()
    
    # Show frame
    cv2.imshow('YOLOv8 Webcam - Press q to quit', frame)
    
    # Check for key press
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord('q'):
        print("\n✓ Quit signal received")
        break
    elif key == ord('s'):
        screenshot_count += 1
        cv2.imwrite(f'webcam_screenshot_{screenshot_count}.jpg', frame)
        print(f"✓ Screenshot saved: webcam_screenshot_{screenshot_count}.jpg")

# Clean up
cap.release()
cv2.destroyAllWindows()

print(f"\n" + "=" * 50)
print("WEBCAM SESSION SUMMARY")
print("=" * 50)
print(f"✓ Total frames processed: {frame_count}")
print(f"✓ Screenshots saved: {screenshot_count}")
print("✓ Webcam closed successfully")
print("=" * 50)
