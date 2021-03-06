import base64
import io
import cv2
from imageio import imread
import matplotlib.pyplot as plt
import numpy as np

filename = "/home/ubuntu/testImage"
with open(filename, "rb") as fid:
    data = fid.read()

#b64_bytes = base64.b64encode(data)
b64_bytes = data
b64_string = b64_bytes.decode()

# reconstruct image as an numpy array
img = imread(io.BytesIO(base64.b64decode(b64_string)))
height, width, channels = img.shape
print(height)
print(width)
print(channels)

# show image
plt.figure()
plt.imshow(img, cmap="gray")

# finally convert RGB image to BGR for opencv
# and save result
cv2_img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
cv2.imwrite("reconstructed.jpg", cv2_img)
plt.show()
