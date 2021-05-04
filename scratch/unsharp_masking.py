from PIL import Image
from pylab import *
from numpy import *
import imtools
from scipy.ndimage import filters
import scipy.io
import scipy.misc
import imageio

def unsharp_mask(im):

    blurred = filters.gaussian_filter(im, 4)
    unsharp_mask = 1.0*blurred - im

    return unsharp_mask

im = array(Image.open('../data/lenna.png').convert('L'))
mask = unsharp_mask(im)
masked = clip(im - 1*mask, 0, 255) # back to uint

# original
figure(figsize=(16,16))
subplot(2,2,1)
imshow(uint8(im))
title('original')

# blurred
blurred = filters.gaussian_filter(im, 4)
subplot(2,2,2)
imshow(uint8(blurred))
title('blurred')

# mask
subplot(2,2,3)
title('unsharp mask')
imshow(uint8(mask + 128))

# masked
subplot(2,2,4)
title('masked')
imshow(uint8(masked))

show()

# color
im_r, im_g, im_b = Image.open('../data/lenna.png').split()
im_r = array(im_r)
im_g = array(im_g)
im_b = array(im_b)
mask_r = unsharp_mask(im_r)
mask_g = unsharp_mask(im_g)
mask_b = unsharp_mask(im_b)
masked_r = clip(im_r - 1*mask_r, 0, 255) # back to uint
masked_g = clip(im_g - 1*mask_g, 0, 255) # back to uint
masked_b = clip(im_b - 1*mask_b, 0, 255) # back to uint
im_r = Image.fromarray(masked_r)
im_g = Image.fromarray(masked_g)
im_b = Image.fromarray(masked_b)

# original
figure(figsize=(16,16))
subplot(2,2,1)
title('original')
imshow(Image.open('../data/lenna.png'))

# sharpened
rgbArray = np.zeros((512,512,3), 'uint8')
rgbArray[..., 0] = im_r
rgbArray[..., 1] = im_g
rgbArray[..., 2] = im_b
subplot(2,2,2)
title('sharpened')
imshow(rgbArray)

show()