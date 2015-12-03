from urllib.request import urlopen
import io
from PIL import Image
import numpy as np
from scipy import fftpack
from skimage.measure import block_reduce
from scipy.misc import imresize

# Analyse upsampling and downsampling

def get_image_online(image_url='http://i.imgur.com/8vuLtqi.png', size=(512, 512)):
	file_descriptor = urlopen(image_url)
	image_file = io.BytesIO(file_descriptor.read())
	image = Image.open(image_file)
	img_color = image.resize(size, 1)
	img_grey = img_color.convert('L')
	img = np.array(img_grey, dtype=np.float)
	return img

# Use this if you have the lenna picture in your local directory
def get_image():
	pic_color = Image.open("lenna.png")
	pic_grey = pic_color.convert('L')
	return(np.array(pic_grey))

#np_image = get_image()

np_image = get_image_online()

print("\nWe have the greyscale version of the image as a numpy array of size - "+str(np_image.shape))
print(np_image)
print("\n the maximum and minimum intensity levels in the image is as follows")
print(np.max(np_image))
print(np.min(np_image))

img = Image.fromarray(np_image)
img.show()

# Down sampling and Decimation

downsampled_np_img = block_reduce(np_image, block_size=(3, 3), func=np.mean)
print(downsampled_np_img.shape)
downsampled_img = Image.fromarray(downsampled_np_img)
downsampled_img.show()

# Upsampling

upsampled_np_img = imresize(downsampled_np_img, 3.0)
upsampled_img = Image.fromarray(upsampled_np_img)
upsampled_img.show()