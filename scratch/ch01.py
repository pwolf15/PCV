from PIL import Image
from pylab import *

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

figure()
hist(im.flatten(),128)
show()

title('Plotting: "empire.jpg"')
show()
