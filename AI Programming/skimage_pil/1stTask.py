import numpy as np
import skimage
from skimage import data
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean

astronaut = skimage.data.astronaut()
rocket = skimage.data.rocket()




pixel = rocket[0:427,0:512]
pixel2 = astronaut[0:427,0:512]
print(pixel.shape)
print(pixel2.shape)
skimage.io.imshow(pixel2)
skimage.io.show()
skimage.io.imshow(pixel)
skimage.io.show()
