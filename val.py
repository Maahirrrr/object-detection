from ultralytics import YOLO

# Load your trained YOLOv8 model
model = YOLO('/home/maahir/Documents/yolov8x.pt')

# Perform validation
results = model.val(data='/home/maahir/Documents/coco8/data.yaml')
