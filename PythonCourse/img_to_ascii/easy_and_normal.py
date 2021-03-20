#! /usr/bin/python3
import binascii
import urllib.request
from PIL import Image
import sys
import numpy as np
import PIL.ImageFont
import PIL.ImageOps
import PIL.ImageDraw

"""
urllib.request.urlretrieve('pixlink.jpg', 'jeans.jpg')
img = Image.open('jeans.jpg').convert('L').resize((80,40))
img.save('jeans_gray.jpg')
"""

urllib.request.urlretrieve('https://upload.wikimedia.org/wikipedia/commons/3/30/ROS_Crystal_Logo.png', 'ros_logo.jpg')
# img = Image.open('ros_logo/jpg').convert('L').resize((120,120))

image_path = input("Hello, please write a image name like hello.jpg(it should be in same folder as script!): ")
img = Image.open(image_path).convert('L').resize((40, 40))
# img.save('ros_logo_grey.jpg')


np_image = np.array(img)


class Image_to_ascii:
    """
    Takes in numpy array, returns ascii print of picture
    optional parameters:
    asciis = list of chars
    """

    def __init__(self, np_image, asciis=None, filename="default.txt"):
        if asciis is None:
            asciis = [' ', 'e', 'w', 'y', 'e', '*', '+', '-']
            self.asciis = asciis
            self.np_image = np_image
            self.filename = filename

    def image_to_ascii(self):
        for index_x in range(np_image.shape[0]):
            print("")
            for index_y in range(np_image.shape[1]):
                multiplier = 255 // len(self.asciis)
                for asc in range(len(self.asciis)):
                    if self.np_image[index_x, index_y] >= (255 - (asc + 1) * multiplier):
                        print(self.asciis[asc], end='')
                        break

    # Easy
    # instead of printing to the terminal, saves ascii picture as text file
    def ascii_image_to_text(self):
        orig_stdout = sys.stdout
        sys.stdout = open('easy.txt', "w+")
        Image_to_ascii.image_to_ascii(self)
        sys.stdout.close()
        sys.stdout = orig_stdout
        print("ascii to .txt DONE!(easy.txt in script folder!!!)")


    # Normal
    # method to the class, that instead of printing to the terminal, saves ascii picture as jpg file

    def ascii_image_to_jpg(self, path_to_font=None):
        pixel_vkl = 0
        pixel_vikl = 255

        print("Hello, I convert ascii to .jpg! and save it!\n")

        orig_stdout = sys.stdout
        sys.stdout = open('normal.txt', "w+")
        Image_to_ascii.image_to_ascii(self)
        sys.stdout.close()

        grayscale = 'L'
        with open('normal.txt') as text_file:
            stroki = tuple(s.rstrip() for s in text_file.readlines())

        font_size = 20
        path_to_font = path_to_font or 'cour.ttf'
        try:
            shrift = PIL.ImageFont.truetype(path_to_font, size=font_size)
        except IOError:
            shrift = PIL.ImageFont.load_default()
            print('Could not use chosen shrift. Using default.')

        topx = lambda pt: int(round(pt * 96.0 / 72))
        max_shirina_strioki = max(stroki, key=lambda s: shrift.getsize(s)[0])
        test = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        h_max = topx(shrift.getsize(test)[1])
        w_max = topx(shrift.getsize(max_shirina_strioki)[0])
        h = h_max * len(stroki)
        w = int(round(w_max + 40))
        picture = PIL.Image.new(grayscale, (w, h), color=pixel_vikl)
        draw = PIL.ImageDraw.Draw(picture)

        v_pos = 5
        h_pos = 5
        str_sp = int(round(h_max * 0.8))
        for line in stroki:
            draw.text((h_pos, v_pos),
                      line, fill=pixel_vkl, font=shrift)
            v_pos += str_sp
        yashik = PIL.ImageOps.invert(picture).getbbox()
        picture = picture.crop(yashik)
        picture.save('result.jpg')
        sys.stdout = orig_stdout
        print("ascii to .jpg DONE!(result.jpg in script folder)")

# Hard
    def take_www_address_and_make_ascii_conversion_from_that(self):
        urllib.request.urlretrieve('pixlink.jpg', 'jeans.jpg')
        img = Image.open('jeans.jpg').convert('L').resize((80, 40))
        img.save('jeans_gray.jpg')
Image_to_ascii.__doc__

print("Please select by integer 1-3 what you want to do")
print("1. Convert ascii to text")
print("2. Convert ascii to jpg")
text_or_jpg = input()
if text_or_jpg == '1':
    Image_to_ascii(np_image).ascii_image_to_text()


elif text_or_jpg == '2':
    Image_to_ascii(np_image).ascii_image_to_jpg()

else:
    print("sry cant understand!!!")

# Image_to_ascii(np_image, [' ', 'e', 'y', 'e', '*', '+', '-']).image_to_ascii()
