from ultralytics import YOLO

model = YOLO("yolov8n.pt")

source = 0  # Webcam

results = model.track(source=source, tracker="bytetrack.yaml", conf=0.35, show=True, save=True)

print("Webcam demo complete!")
