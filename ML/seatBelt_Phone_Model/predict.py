#!/bin/python3

import os

from ultralytics import YOLO
import cv2


VIDEOS_DIR = os.path.join('.', 'videos')

video_path = os.path.join(VIDEOS_DIR, 'test_Trim.mp4')
video_path_out = '{}_out.mp4'.format(video_path)

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
H, W, _ = frame.shape
out = cv2.VideoWriter(video_path_out, cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))

model_path = '/home/nader/Desktop/dataset/SS_dataset/train4-20231111T231400Z-001/train4/weights/last.pt'
# Load a model
model = YOLO(model_path)  # load a custom model

threshold = 0.5

while ret:

    results = model(frame)[0]

    for result in results.boxes.data.tolist():
        x1, y1, x2, y2, score, class_id = result

        if score > threshold:
            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 4)
            cv2.putText(frame, results.names[int(class_id)].upper(), (int(x1), int(y1 - 10)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.3, (0, 255, 0), 3, cv2.LINE_AA)

    out.write(frame)
    ret, frame = cap.read()

cap.release()
out.release()
cv2.destroyAllWindows()



# import cv2
# from ultralytics import YOLO
# import numpy as np

# # Load YOLOv8 model
# model = YOLO('ultralytics/yolov5:v6.0')
# model.load_state_dict(torch.load('/home/nader/Desktop/dataset/SS_dataset/train4-20231111T231400Z-001/train4/weights/last.pt', map_location='cpu'))
# model.eval()

# # Open video file
# video_path = '/home/nader/Desktop/dataset/SS_dataset/test_Trim.mp4'
# cap = cv2.VideoCapture(video_path)

# # Get video properties
# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# # Create video writer
# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), fps, (width, height))

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         break

#     # Preprocess the frame
#     img = model.preprocess(frame)

#     # Make prediction
#     with torch.no_grad():
#         pred = model(img)[0]

#     # Post-process the prediction
#     pred = model.postprocess(pred, frame.shape[:2], frame.shape[:2])[0]

#     # Draw bounding boxes on the frame
#     frame_with_boxes = model.plot(pred, frame)

#     # Write the frame to the output video
#     out.write(frame_with_boxes)

#     # Display the frame
#     cv2.imshow('YOLOv8 Object Detection', frame_with_boxes)

#     # Break the loop if 'q' key is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release resources
# cap.release()
# out.release()
# cv2.destroyAllWindows()


















# import os , ultralytics , cv2

# Videos_Dir="/home/nader/Desktop/dataset/SS_dataset"

# Vid_path='/home/nader/Desktop/dataset/SS_dataset/test_Trim.mp4' 
# Vid_out_path='{}_out.mp4'.format(Vid_path)

# cap=cv2.VideoCapture(Vid_path)
# ret,frame=cap.read()
# H,W,_=frame.shape


