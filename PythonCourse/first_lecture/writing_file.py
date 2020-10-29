#! /usr/bin/python3

import requests
import os

url = 'https://upload.wikimedia.org/wikipedia/commons/3/30/ROS_Crystal_Logo.png'
filename = url.split('/')[-1]

if not os.path.exists(filename):
    image_to_save = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(image_to_save.content)
    print("file is saved")
else:
    print("file all ready saved")
