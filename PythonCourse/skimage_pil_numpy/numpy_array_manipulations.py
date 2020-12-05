#! /usr/bin/python3
from PIL import Image
import numpy as np


def greyscale(colors):
    red, green, blue = colors
    return 0.07 * red + 0.72 * green + 0.21 * blue


image_frame = Image.open('ROS_Crystal_Logo.png')
np_image = np.array(image_frame)

np_image_in_greyscale = np.apply_along_axis(greyscale, 2, np_image)

np_grey_image_int = np_image_in_greyscale.astype(np.uint8)
print(np_grey_image_int.shape)

grey_image = Image.fromarray(np_grey_image_int)
filename = "ros_crystal_grey.png"

grey_image.save(filename)

cropped_np_grey_image_int = np_grey_image_int[0:632, 0:632]
print(cropped_np_grey_image_int.shape)

cropped_image_grey = Image.fromarray(cropped_np_grey_image_int)
filename = "cropped_ros_crystal_grey.png"

cropped_image_grey.save(filename)