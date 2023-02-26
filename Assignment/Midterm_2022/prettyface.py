#
# prettyface.py - Question 4b
#

import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

face = misc.face(gray=True) 
plt.imshow(face)
plt.imshow(face, cmap=plt.cm.gray) 
plt.show()

# shift the image
shifted_face = ndimage.shift(face, (50,50))
plt.imshow(shifted_face)
plt.show()

# rotate the image
rotated_face = ndimage.rotate(face, 30)
plt.imshow(rotated_face)
plt.show()

# crop the image
cropped_face = face[100:-100,100:-100]
plt.imshow(cropped_face)
plt.show()
