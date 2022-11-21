https://powcoder.com
代写代考加微信 powcoder
Assignment Project Exam Help
Add WeChat powcoder

from image import image_to_greyscale, combine_images
import matplotlib.pyplot as plt
import skimage.io as io
import numpy as np

def normalize(image): # normalize image to [0, 1] if it has integer dtype
    if np.issubdtype(image.dtype, np.integer):
        return image.astype(float) / 255.0
    return image


#Example 1
greyscale = image_to_greyscale("flower.jpg", (0.2125, 0.7154, 0.0721))
print(greyscale.dtype)
print(greyscale.shape)
print(greyscale)
io.imshow(normalize(greyscale))
io.show()

#Example 2
image = combine_images("monkey.jpg", "tiger.jpg", [600, 900], [50, 550], 400, 400)
plt.imshow(image)
plt.show()


#Example 3
image = combine_images("tiger.jpg", "monkey.jpg", [50, 550], [600, 900], 600, 400)
plt.imshow(image)
plt.show()

#Example 4
image = combine_images("monkey.jpg", "tiger.jpg", [600, 900], [450, 1100], 400, 400)
plt.imshow(image)
plt.show()

