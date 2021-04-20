from PIL import Image
from pylab import *
from numpy import *
import imtools
import pca

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
figure()
gray()
subplot(2,4,1)
imshow(immean.reshape(m,n))
for i in range(7):
    subplot(2,4,i+2)
    imshow(V[i].reshape(m,n))

show()