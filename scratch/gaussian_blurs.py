from PIL import Image
from pylab import *
from numpy import *
import imtools
from scipy.ndimage import filters
import scipy.io
import scipy.misc
import imageio

im = array(Image.open('../data/tubingen.jpg').convert('L'))

figure(figsize=(16,16))
gray()
subplot(2, 3, 1)
title('original')
imshow(im)

# gaussian filtering
for sigma in range(5):

    subplot(2, 3, sigma + 2)
    im1 = filters.gaussian_filter(im, sigma)
    title(label='sigma=' + str(sigma))
    imshow(im1)

show()

figure(figsize=(16,16))
gray()
subplot(2, 3, 1)
title('original')
imshow(im)

# create a new figure
figure()
# don’t use colors
gray()
# show contours with origin upper left corner
contour(im, origin="image")
axis("equal")
axis("off")

# for sigma in range(5):
#     subplot(2, 3, sigma + 2)
#     title(label='sigma=' + str(sigma))
#     im1= filters.gaussian_filter(im, sigma)
#     imx = zeros(im1.shape)
#     filters.sobel(im1, 1, imx)
#     imy = zeros(im1.shape)
#     filters.sobel(im1, 0, imy)
#     imxy = sqrt(imx**2 + imy**2)
#     imshow(imxy)
#     contour(im, origin=’image’)
    

show()