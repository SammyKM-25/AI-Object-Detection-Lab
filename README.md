# YOLOv8 Object Detection Lab

## Project Information
- **Module**: CMPG 313 - Artificial Intelligence
- **Student**: SammyKM-25
- **Date**: March 2026

## Test Results

### 1. Image Detection
- **Input**: Asian market.jpg
- **Detected Objects**: 9 persons
- **Confidence**: Various (shown in output)
- **Output**: runs/detect/predict/Asian market.jpg

### 2. Video Tracking
- **Input**: Cars Moving On Road Footage.mp4
- **Objects Tracked**: Vehicles
- **Tracking Method**: ByteTrack
- **Output**: Processed video with tracking IDs

### 3. Webcam Detection
- **Mode**: Real-time detection
- **Status**: Successful
- **Evidence**: Screenshots included in screenshots folder

## Files in This Repository

| File | Description |
|------|-------------|
| test_image.py | Image detection script |
| test_video.py | Video tracking script |
| test_webcam.py | Webcam detection script |
| Asian market.jpg | Test image |
| Cars Moving On Road Footage.mp4 | Test video |
| runs/detect/predict/ | Detected image output |
| screenshots/ | Evidence screenshots |

## How to Run

### Image Detection
```bash
python test_image.py
