import cv2
import numpy as np
import matplotlib.pyplot as plt

from src.segmentation.threshold_segmentation import threshold_segment
from src.feature_analysis.image_projections import (
    horizontal_projection,
    vertical_projection,
)
from src.feature_analysis.run_length_encoding import rle_encode, rle_decode

image = cv2.imread("data/example.png")
if image is None:
    raise FileNotFoundError("Place an example image at data/example.png")

binary, _ = threshold_segment(image)
hp = horizontal_projection(binary)
vp = vertical_projection(binary)

values, counts, shape = rle_encode(binary)
reconstructed = rle_decode(values, counts, shape)

print("Lossless reconstruction:", np.array_equal(binary, reconstructed))
print("Number of RLE runs:", len(values))

plt.figure()
plt.plot(vp)
plt.xlabel("Column")
plt.ylabel("Foreground count")
plt.title("Vertical Projection")
plt.grid(True)
plt.show()

plt.figure()
plt.plot(hp)
plt.xlabel("Row")
plt.ylabel("Foreground count")
plt.title("Horizontal Projection")
plt.grid(True)
plt.show()
