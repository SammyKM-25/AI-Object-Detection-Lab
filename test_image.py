from ultralytics import YOLO

model = YOLO("yolov8n.pt")

source = r"Asian market.jpg"

if source.lower().endswith((".jpg", ".jpeg", ".png", ".bmp")):
    results = model.predict(source=source, conf=0.35, save=True)
    print("Image detection complete!")
    print("Check runs/detect/predict/ folder for output")
