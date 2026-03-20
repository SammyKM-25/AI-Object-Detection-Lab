import cv2

print("Testing webcam...")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("ERROR: Cannot open webcam!")
    exit()

print("✓ Webcam opened. Showing preview for 5 seconds...")

# Show webcam for 5 seconds
start = cv2.getTickCount()
while (cv2.getTickCount() - start) / cv2.getTickFrequency() < 5:
    ret, frame = cap.read()
    if ret:
        cv2.putText(frame, "Webcam Working - No Detection", (10, 30), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Webcam Test", frame)
        cv2.waitKey(30)

cap.release()
cv2.destroyAllWindows()
print("✓ Webcam test complete")
