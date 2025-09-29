import time
import os

filename = "image-service.txt"
images = os.listdir('./images')

def writeImage(prngResponse):
    with open(filename, 'w') as f:
        index = int(prngResponse) % len(images)
        image_path = os.path.join("images", images[index])
        abs_path = os.path.abspath(image_path)
        f.write(abs_path)

while True:
    with open(filename, 'r') as f:
        f.seek(0)
        response = f.read()
        if(response.isdigit() and response != ''):
            time.sleep(1)
            writeImage(response)
    time.sleep(0.5)
