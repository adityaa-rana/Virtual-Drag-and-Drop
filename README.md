# 🖐️ Virtual Drag & Drop Interface with Hand Gestures

This project is a virtual drag-and-drop UI built using Python, OpenCV, and cvzone (based on MediaPipe). It allows users to interact with on-screen rectangles using just hand gestures, eliminating the need for a mouse or touchscreen. Built during free time to explore hand tracking, gesture interaction, and basic computer vision UI design.

## Features

- Real-time hand tracking using webcam
- Drag and reposition rectangles using finger pinch gesture
- Gesture detection via distance between index and middle finger
- Transparent overlays with OpenCV for clean visuals
- Easily extendable for other gesture-based UI projects

## Tech Stack

- Python 3
- OpenCV
- cvzone (MediaPipe-based hand tracking)
- NumPy

## Installation

Make sure Python is installed, then install the required libraries:


Ensure your webcam is connected.

## How It Works

The webcam feed is captured and mirrored. The HandDetector from cvzone detects hand landmarks. The distance between the index (point 8) and middle (point 12) fingers is computed. If the distance is less than 40 pixels, it activates drag mode. If the fingertip is inside the rectangle, its center is updated to follow the finger. When fingers are apart, dragging stops. A transparent overlay (`imgnew`) is used to render draggable rectangles.

## Project Structure

- `virtual_dragger.py` – Main Python script
- `README.md` – This file

## DragRect Class

A class to define draggable rectangles.

- `centre`: (x, y) position of the rectangle center
- `size`: dimensions of the rectangle
- `color`: changes from pink to green when being dragged
- `update(cursor)`: updates position when dragged
- `stopdrag()`: stops dragging and resets color

## Future Improvements

- Multi-hand support
- Rotation and resizing via additional gestures
- Snap to grid or zone boundaries
- Support for images, UI elements instead of rectangles

## Credits

- cvzone by Murtaza Hassan
- MediaPipe by Google
- OpenCV


