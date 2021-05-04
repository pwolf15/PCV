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

# pil_im = Image.fromarray(im)
# # pil_im.show()

# pil_im = Image.fromarray(unsharp_masked)
# # pil_im.show()

# # color
# im_r, im_g, im_b = Image.open('../data/lenna.png').split()
# im_r = array(im_r)
# im_g = array(im_g)
# im_b = array(im_b)

# blurred = filters.gaussian_filter(im_r, 1)
# unsharp_masked = im_r - blurred
# im_r = unsharp_masked
# # pil_im.show()

# blurred = filters.gaussian_filter(im_g, 1)
# unsharp_masked = im_g - blurred
# im_g = unsharp_masked

# blurred = filters.gaussian_filter(im_b, 1)
# unsharp_masked = im_b - blurred
# im_b = unsharp_masked

# im_r = Image.fromarray(im_r)
# im_g = Image.fromarray(im_g)
# im_b = Image.fromarray(im_b)

# pil_im = Image.merge('RGB', (im_r, im_g, im_b))
# pil_im.show()