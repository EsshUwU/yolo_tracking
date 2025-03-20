# Object Tracking with Servo Control

This project implements real-time object tracking using YOLOv8 and controls a servo motor to follow the detected object.

## Components

- Arduino with servo motor
- USB webcam
- Computer with CUDA-capable GPU
- YOLOv8 trained model (`best.pt`)

## System Overview

The system consists of two main parts:

1. **Python Script (`main.py`)**
   - Uses YOLOv8 for object detection
   - Processes webcam feed in real-time
   - Communicates object position to Arduino via serial
   - Displays detection visualization

2. **Arduino Code (`main.ino`)**
   - Controls servo motor position
   - Receives X-coordinates via serial communication
   - Maps detection coordinates to servo angles

## Setup

1. Connect the servo motor to Arduino pin 3
2. Upload `main.ino` to Arduino
3. Install Python dependencies:
   ```bash
   pip install ultralytics opencv-python pyserial
   ```
4. Place your trained YOLO model as `best.pt` in the project directory

## Usage

1. Connect Arduino to USB port
2. Run the Python script:
   ```bash
   python main.py
   ```
3. The system will:
   - Start webcam capture
   - Detect objects using YOLOv8
   - Move servo to track detected objects
   - Display video feed with detection boxes

Press 'q' to quit the application.

## Technical Details

- Serial Communication: 9600 baud rate
- Frame Width: 640 pixels and can be scaled more
- Servo Range: 0-180 degrees
- CUDA acceleration enabled for inference

# Future Updates 

- Two axis servo