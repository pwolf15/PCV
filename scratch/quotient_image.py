from PIL import Image
from pylab import *
from numpy import *
import imtools
import pca
import pickle
from scipy.ndimage import filters
from scipy.ndimage import measurements, morphology
import scipy.io
import scipy.misc
import imageio
from numpy import random
import rof

def quotient_image(path):
    
    # blurred image
    im = array(Image.open(path).convert('L'))
    pil_im = Image.fromarray(im)
    pil_im.show()

    # gaussian
    G = filters.gaussian_filter(im,5)
    pil_im = Image.fromarray(G)

    # quotient image: Q = im / gaussian
    #   quotient image is a technique in image normalization
    #   it's an alternative to histogram normalization
    Q = im / (G + 0.0001)
    Q = Q * im

    pil_im = Image.fromarray(Q)
    pil_im.show()

quotient_image('../data/empire.jpg')
quotient_image('../data/tubingen.jpg')
