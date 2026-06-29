
---

## Project 2: yolo-object-detection

```markdown
# YOLOv8 Real-Time Object Detection

> Real-time object detection and tracking system using YOLOv8 with support for images, videos, and live webcam streams.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8+-orange.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>

---

## Table of Contents

- [Overview](#overview)
- [The Problem It Solves](#the-problem-it-solves)
- [Key Features](#key-features)
- [What YOLO Can Detect](#what-yolo-can-detect)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Author](#author)

---

## Overview

This project implements **real-time object detection** using the state-of-the-art YOLOv8 (You Only Look Once) architecture. The system supports multiple input sources including static images, video files, and live webcam streams. It includes **ByteTrack integration** for real-time object tracking across video frames.

The project demonstrates practical application of computer vision to solve real-world detection problems with high accuracy and real-time performance.

---

## The Problem It Solves

Object detection is critical in many real-world applications:

- **Security & Surveillance** – Detecting people, vehicles, suspicious objects
- **Autonomous Vehicles** – Identifying pedestrians, other vehicles, traffic signs
- **Retail** – Customer counting, shelf monitoring, inventory management
- **Healthcare** – Medical image analysis, patient monitoring
- **Manufacturing** – Quality control, defect detection
- **Agriculture** – Crop monitoring, pest detection, yield estimation

---

## Key Features

- ✅ **YOLOv8 Object Detection** with configurable confidence thresholds (0.25-0.35)
- ✅ **ByteTrack Integration** for real-time object tracking across video frames
- ✅ **Multiple Input Sources**:
  - Static images (.jpg, .jpeg, .png, .bmp)
  - Video files (.mp4, .avi, .mov)
  - Live webcam stream (device 0)
- ✅ **Real-Time Visualisation**:
  - Bounding boxes with class labels
  - Confidence scores (percentage)
  - Detection count display
- ✅ **Interactive Controls**:
  - Press `q` to quit
  - Press `s` to save screenshot
- ✅ **Performance Optimised** – Processes every 5th frame for smooth real-time performance

---

## What YOLO Can Detect

YOLOv8 is trained on the COCO dataset with **80 object classes**:

### People
- Person

### Vehicles
- Bicycle, Car, Motorcycle, Airplane, Bus, Train, Truck, Boat

### Common Objects
- Traffic Light, Fire Hydrant, Stop Sign, Parking Meter, Bench
- Bird, Cat, Dog, Horse, Sheep, Cow, Elephant, Bear, Zebra, Giraffe
- Backpack, Umbrella, Handbag, Tie, Suitcase
- Frisbee, Skis, Snowboard, Sports Ball, Kite, Baseball Bat, Baseball Glove, Skateboard, Surfboard, Tennis Racket
- Bottle, Wine Glass, Cup, Fork, Knife, Spoon, Bowl
- Banana, Apple, Sandwich, Orange, Broccoli, Carrot, Hot Dog, Pizza, Donut, Cake
- Chair, Couch, Potted Plant, Bed, Dining Table, Toilet, TV, Laptop, Mouse, Remote, Keyboard, Cell Phone, Microwave, Oven, Toaster, Sink, Refrigerator
- Book, Clock, Vase, Scissors, Teddy Bear, Hair Drier, Toothbrush

---

## Technologies Used

| **Category** | **Technology** | **Version** |
| :--- | :--- | :--- |
| Language | Python | 3.8+ |
| Deep Learning | Ultralytics YOLOv8 | 8.0+ |
| Computer Vision | OpenCV | 4.8+ |
| Tracking | ByteTrack | - |
| Version Control | Git, GitHub | - |

---

## Installation
Prerequisites
Python 3.8 or higher

pip (Python package manager)

Steps
1. Clone the repository:

git clone https://github.com/decodb/yolo-object-detection.git
cd yolo-object-detection

2. Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3. Install dependencies:

pip install ultralytics opencv-python

 #Author

**Kulani Maphosa**
**GitHub**: decodb
**LinkedIn**: Kulani Maphosa
**Email**: kulanimaphosa@gmail.com
