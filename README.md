# object-detection
# YOLOv8x Object Detection Project

Welcome to the YOLOv8x Object Detection Project! This repository demonstrates the implementation of the YOLOv8x model for real-time object detection tasks.

## Overview

YOLOv8x is a state-of-the-art object detection model that processes entire images in a single pass, enabling real-time performance. Unlike traditional models that rely on anchor boxes, YOLOv8x employs an anchor-free approach, directly predicting object centers and dimensions, resulting in enhanced speed and accuracy.

## Features

- **Single-Pass Detection**: Processes images in one go, ensuring rapid inference.
- **Anchor-Free Mechanism**: Simplifies architecture by eliminating predefined anchor boxes.
- **Multi-Scale Feature Extraction**: Efficiently detects objects of varying sizes.
- **High Accuracy**: Achieves impressive mean Average Precision (mAP) scores.
- **Real-Time Performance**: Suitable for applications requiring immediate object detection.

## Installation

To get started with this project, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Maahirrrr/object-detection/edit/main/obdect.py
   cd your obdect.py
2. Set Up the Environment:

Ensure you have Python 3.8 or later installed. It's recommended to use a virtual environment:


python3 -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
Install Dependencies:

3. Install the required packages using pip:

pip install ultralytics

pip install torch
pip install opencv-python
pip install numpy
pip install matplotlib


Usage
After installation, you can use the YOLOv8x model for object detection on images, videos, or real-time webcam feeds.


4. Real-Time Object Detection with Webcam
Use the obdect.py script to perform real-time object detection using your webcam:

python obdect.py
