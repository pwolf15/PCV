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

pil_im = Image.open('../data/empire.jpg')
# pil_im.show()

pil_im = Image.open('../data/empire.jpg').convert('L')
# pil_im.show()

pil_im.thumbnail((128, 128))
# pil_im.show()

pil_im = Image.open('../data/empire.jpg')
box = (100,100,400,400)
region = pil_im.crop(box)
# region.show()

region = region.transpose(Image.ROTATE_180)
pil_im.paste(region, box)
# pil_im.show()

out = pil_im.resize((128,128))
# out.show()

out = pil_im.rotate(45)
# out.show()

im = array(Image.open('../data/empire.jpg'))
# imshow(im)
x = [100,100,400,400]
y = [200,500,200,500]

# plot(x,y,'ks:')
# plot(x[:2],y[:2])
# axis('off')

im = array(Image.open('../data/empire.jpg').convert('L'))

figure()
gray()
contour(im, origin='image')
axis('equal')
axis('off')

# figure()
# hist(im.flatten(),128)
# show()

im = array(Image.open('../data/empire.jpg'))
# imshow(im)
# print('Please click 3 points')
# x = ginput(3)
# print('you clicked:',x)
# show()

# title('Plotting: "empire.jpg"')
# # show()

im = array(Image.open('../data/empire.jpg'))
print(im.shape, im.dtype)
value = im[0,0,0]
print(value)

im = array(Image.open('../data/empire.jpg').convert('L'),'f')
print(im.shape, im.dtype)

j = 25
i = 100

im[i,:] = im[j,:]
im[:,i] = 100
im[:100,:50].sum()
im[50:100,50:100]
im[i].mean()
im[:,-1]
im[-2,:]

im = array(Image.open('../data/empire.jpg').convert('L'))

# graylevel transforms

## inversion
im2 = 255 - im

## clamping range between 100 and 200
im3 = (100.0/255) * im + 100

## make darker values darker (quadratic transformation)
im4 = 255.0 * (im/255.0)**2

print(int(im.min()), int(im.max()))
print(int(im2.min()), int(im2.max()))
print(int(im3.min()), int(im3.max()))
print(int(im4.min()), int(im4.max()))

pil_im = Image.fromarray(im4)
# pil_im.show()

# histogram equalization
# use-case: equalize intensities, increase contrast
im = array(Image.open('../data/AquaTermi_lowcontrast.JPG').convert('L'))
pil_im = Image.fromarray(im)
# pil_im.show()
im2, cdf = imtools.histeq(im)
pil_im = Image.fromarray(im2)
# pil_im.show()

imlist = imtools.get_imlist("../data/a_thumbs")
im = array(Image.open(imlist[0]))
m,n = im.shape[0:2]
imnbr = len(imlist)

immatrix = array([array(Image.open(im)).flatten()
            for im in imlist],'f')

# perform PCA
V,S,immean = pca.pca(immatrix)

# show some images (mean and 7 first modes)
# figure()
gray()
subplot(2,4,1)
# imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

# show()

# save mean and principal components
with open('font_pca_modes.pkl', 'wb') as f:
    pickle.dump(immean,f)
    pickle.dump(V,f)
    f.close()

with open('font_pca_modes.pkl', 'rb') as f:
    immean = pickle.load(f)
    V = pickle.load(f)
    f.close()

# savetxt('test.txt',x,'%i')

im = array(Image.open('../data/empire.jpg').convert('L'))
im2 = filters.gaussian_filter(im, 5)

im = array(Image.open('../data/empire.jpg'))
im2 = zeros(im.shape)
for i in range(3):
    im2[:,:,i] = filters.gaussian_filter(im[:,:,i],1)
im2 = uint8(im2)
pil_im = Image.fromarray(im2)
# pil_im.show()

im = array(Image.open('../data/empire.jpg').convert('L'))

# Sobel derivative filter
imx = zeros(im.shape)
filters.sobel(im,1,imx)

imy = zeros(im.shape)
filters.sobel(im,0,imy)

magnitude = sqrt(imx**2+imy**2)

pil_im = Image.fromarray(imy)
# pil_im.show()

pil_im = Image.fromarray(imx)
# pil_im.show()

pil_im = Image.fromarray(magnitude)
# pil_im.show()

# Gaussian filters
im = array(Image.open('../data/empire.jpg').convert('L'))
pil_im = Image.fromarray(im)
# pil_im.show()

sigmas = [2, 5, 10]
for sigma in sigmas:

    imx = ones(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (0,1), output=imx)
    pil_im = Image.fromarray(imx)
    # pil_im.show()

    imy = zeros(im.shape)
    filters.gaussian_filter(im, (sigma,sigma), (1,0), imy)
    pil_im = Image.fromarray(imy)
    # pil_im.show()

    magnitude = sqrt(imx**2 + imy**2)
    pl_im = Image.fromarray(magnitude)
    # pil_im.show()

im = array(Image.open('../data/houses.png').convert('L'))
im = 1*(im<128)

labels, nbr_objects = measurements.label(im)
print("Number of objects: ", nbr_objects)

# morphology - opening to separate objects better
im_open = morphology.binary_opening(im,ones((9,5)),iterations=1)
labels_open, nbr_objects_open = measurements.label(im_open)
print("Number of objects:",nbr_objects_open)

# MATLAB file I/O
data = {}
data['x'] = 1234
scipy.io.savemat('test.mat',data)
data2 = scipy.io.loadmat('test.mat')
print(data2)

imageio.imwrite('test.jpg', im)

# create synthetic image with noise
im = zeros((500,500))
im[100:400,100:400] = 128
im[200:300,200:300] = 255
im = im + 30*random.standard_normal((500,500))

U,T = rof.denoise(im,im)
G = filters.gaussian_filter(im,10)

# save the result
imageio.imwrite('synth_rof.png',Image.fromarray(U))
imageio.imwrite('synth_gaussian.png',Image.fromarray(G))

im = array(Image.open('../data/empire.jpg').convert('L'))
U,T = rof.denoise(im,im)

figure()
gray()
# imshow(U)
# axis('equal')
# axis('off')
# show()

im = array(Image.open('../data/tubingen.jpg').convert('L'))

for sigma in range(1,4):

    im2 = filters.gaussian_filter(im, sigma)
    pil_im = Image.fromarray(im2)
    # pil_im.show(title='sigma ' + str(sigma))

# unsharp masking

## grayscale
pil_im = Image.fromarray(im)
# pil_im.show()
blurred = filters.gaussian_filter(im, 1)
unsharp_masked = im - blurred
pil_im = Image.fromarray(unsharp_masked)
# pil_im.show()

im = array(Image.open('../data/lenna.png').convert('L'))

pil_im = Image.fromarray(im)
# pil_im.show()
blurred = filters.gaussian_filter(im, 1)
unsharp_masked = im - blurred
pil_im = Image.fromarray(unsharp_masked)
# pil_im.show()

# color
im_r, im_g, im_b = Image.open('../data/lenna.png').split()
im_r = array(im_r)
im_g = array(im_g)
im_b = array(im_b)

blurred = filters.gaussian_filter(im_r, 1)
unsharp_masked = im_r - blurred
im_r = unsharp_masked
# pil_im.show()

blurred = filters.gaussian_filter(im_g, 1)
unsharp_masked = im_g - blurred
im_g = unsharp_masked

blurred = filters.gaussian_filter(im_b, 1)
unsharp_masked = im_b - blurred
im_b = unsharp_masked

im_r = Image.fromarray(im_r)
im_g = Image.fromarray(im_g)
im_b = Image.fromarray(im_b)

pil_im = Image.merge('RGB', (im_r, im_g, im_b))
pil_im.show()