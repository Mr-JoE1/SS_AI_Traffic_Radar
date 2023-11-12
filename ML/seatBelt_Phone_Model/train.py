from google.colab import drive
from tqdm.notebook import tqdm
from google.colab import drive
from ultralytics import YOLO
import os
import shutil
import random



drive.mount('/content/drive')



model = YOLO('yolov8n.yaml')
model = YOLO('yolov8n.pt')

results = model.train(data='/content/drive/MyDrive/ssEdge/config.yaml', epochs=5)

