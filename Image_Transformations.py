from urllib.request import urlopen
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Image Transformations 
original_image ='http://i.imgur.com/GAazZeX.png'
after_homo = 'http://i.imgur.com/KqMjJWV.png'

def get_image(image_url='http://i.imgur.com/8vuLtqi.png', size=(128, 128)):
	file_descriptor = urlopen(image_url)
	image_file = io.BytesIO(file_descriptor.read())
	image = Image.open(image_file)
	img_color = image.resize(size, 1)
	img_grey = img_color.convert('L')
	img = np.array(img_grey, dtype=np.float)
	# This returns a 128*128 size matrix
	return img

np_image_before = get_image(original_image,(384,510))
np_image_after = get_image(after_homo,(384,510))

print("\nWe have the greyscale version of the original image image of size - "+str(np_image_before.shape))
print(np_image_before)
print(np.max(np_image_before))
print(np.min(np_image_before))

print("\nWe have the greyscale version of the image  after filtering of size - "+str(np_image_after.shape))
print(np_image_after)
print(np.max(np_image_after))
print(np.min(np_image_after))


img_before = Image.fromarray(np_image_before)
img_before.show()

img_after = Image.fromarray(np_image_after)
img_after.show()

# This is consistent with the actual image as we have 250 as the whitest pixel while after filtering its 114 (no really white area after filtering)
print("\n\nSo as we can see larger values closer to 256 is white, smaller values close to 0 are black")
# if you are confused about the white edges as seen in the image and the numpy array - its because i couldnt crop it properly.

''' Based on my [Post on Homomorphic filtering](http://adityaarpitha.blogspot.in/2015/10/homomorphic-filtering_7.html)
Okay so reflectence is what we get after filtering - 'np_image_after' - r(x,y)
? or is it, maybe its original-filtered or something?

and image itself is 'np_image_before' - i(x,y)

Based on the illumination-reflectance model of images, we can find illumination by dot division
'''
np_image_illumination = np.divide(np_image_before,np_image_after)
print(np_image_illumination)

img_illumination = Image.fromarray(np_image_illumination)
img_illumination.show()