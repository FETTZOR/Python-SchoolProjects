import numpy as np
import skimage
from skimage import data
from skimage import data, color
from skimage.transform import rescale, resize, downscale_local_mean
from scipy.misc import face
import numpy as np
import matplotlib.pyplot as plt

astronaut = skimage.data.astronaut()
rocket = skimage.data.rocket()
pixel = rocket[0:427,0:512]
pixel2 = astronaut[0:427,0:512]
#
# merge1 = np.concatenate((pixel, pixel2), axis=1)

# vertically
# merge = np.concatenate((face1,face2))
# vertically
# plt.gray()
# plt.imshow(merge)
merge = np.concatenate((pixel2, pixel), axis=1)
flip = np.flip((merge), axis=0)


print(pixel.shape)
print(pixel2.shape)
# skimage.io.imshow(merge1)
# skimage.io.show()
# skimage.io.imshow(pixel)
# skimage.io.show()
skimage.io.imshow(flip)
skimage.io.show()
# skimage.io.show()