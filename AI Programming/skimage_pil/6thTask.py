import numpy as np
import skimage
from skimage import data
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
from scipy.misc import face
import numpy as np
import matplotlib.pyplot as plt
from skimage.color import rgb2gray
from skimage.filters import threshold_otsu
from skimage.filters import try_all_threshold

astronaut = skimage.data.astronaut()
rocket = skimage.data.rocket()
pixel = rocket[0:427, 0:512]
pixel2 = astronaut[0:427, 0:512]
#
# merge1 = np.concatenate((pixel, pixel2), axis=1)

# vertically
# merge = np.concatenate((face1,face2))
# vertically
# plt.gray()
# plt.imshow(merge)
invert = np.invert(pixel2)



print(pixel.shape)
print(pixel2.shape)
# skimage.io.imshow(merge1)
# skimage.io.show()
# skimage.io.imshow(pixel)
# skimage.io.show()
skimage.io.imshow(invert)
skimage.io.show()
# skimage.io.show()