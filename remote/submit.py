import requests
import json
from camera import capture_frame
import sys

def send_image(url, image, measurements):
    
    request = requests.post(url, files={"test.jpg": image}, params=measurements)
    

if __name__ == "__main__":
    url = sys.argv[1]
    image_stream = capture_frame(800, 600)
    measurements = {"foo": "bar"}
    send_image(url, image_stream.getvalue(), measurements)