'''
@Author : infinity tech ltd http://infinitytech.ltd/
@date   : 24 Sep 2023
@file   : videoGenerator.py
@brief  : this code will be responsible for creating videos from images


dependencies : 
    sudo pip install imageio numpy PIL
    pip install imageio[ffmpeg]
    pip install imageio[pyav]

'''


import os
import imageio
import numpy as np
from PIL import Image

def create_video_from_images(input_dir, output_file, fps=30):
    image_files = [f for f in os.listdir(input_dir) if f.endswith(('.jpg', '.jpeg', '.png', '.gif'))]
    image_files.sort()
    images = []
    for image_file in image_files:
        image_path = os.path.join(input_dir, image_file)
        img = Image.open(image_path)
        img_np = np.array(img)
        images.append(img_np)
    with imageio.get_writer(output_file, fps=fps) as writer:
        for image in images:
            writer.append_data(image)