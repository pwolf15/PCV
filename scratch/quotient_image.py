from PIL import Image
from pylab import *
from numpy import *
import imtools
from scipy.ndimage import filters
import scipy.misc

def quotient_image(im):
    
    pil_im = Image.fromarray(im)
    pil_im.show()

    # gaussian
    G = filters.gaussian_filter(im,5)
    pil_im = Image.fromarray(G)

    # quotient image: Q = im / gaussian
    #   quotient image is a technique in image normalization
    #   it's an alternative to histogram normalization
    Q = im / (G + 0.0001)
    Q = clip(128 * Q, 0, 255)

    return Q

# original
path = '../data/empire.jpg'
im = array(Image.open(path).convert('L'))
hist_im, cdf = imtools.histeq(im)
Q = quotient_image(im)

figure(figsize=(16,16))
gray()
subplot(3,2,1)
title('original')
imshow(im)

subplot(3,2,2)
title('original hist')
hist(im.flatten(), 256)

