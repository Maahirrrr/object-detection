from ultralytics import YOLO  # Import the YOLO class from the ultralytics library
import cv2  # Import the OpenCV library for computer vision tasks

# Load the pre-trained YOLOv8x model
model = YOLO("yolov8x.pt")

# Initialize the webcam (device 0 typically refers to the default webcam)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  # Set the frame width to 640 pixels
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)  # Set the frame height to 480 pixels

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()  # Exit the program if the webcam cannot be opened

print("Press 'q' to exit.")  # Inform the user how to exit the loop
while True:
    ret, frame = cap.read()  # Read a frame from the webcam
    if not ret:
        break  # Exit the loop if the frame is not read correctly

    # Flip the frame horizontally to create a mirror effect
    flipped_frame = cv2.flip(frame, 1)

    # Perform object detection on the flipped frame with a confidence threshold of 0.5
    results = model.predict(flipped_frame, conf=0.5, show=False)

    # Annotate the frame with the detection results
    annotated_frame = results[0].plot()

    # Display the annotated frame in a window titled "YOLOv8 Real-Time Detection (Mirrored)"
    cv2.imshow("YOLOv8 Real-Time Detection (Mirrored)", annotated_frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the webcam and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
