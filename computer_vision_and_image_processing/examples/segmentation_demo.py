import cv2
import matplotlib.pyplot as plt

from src.enhancement.grayscale import to_grayscale
from src.enhancement.histogram_equalization import equalize_grayscale
from src.segmentation.threshold_segmentation import threshold_segment
from src.segmentation.object_measurements import measure_largest_object

image = cv2.imread("data/example.png")
if image is None:
    raise FileNotFoundError("Place an example image at data/example.png")

gray = to_grayscale(image)
equalized = equalize_grayscale(gray)
binary, threshold = threshold_segment(equalized)
measurement = measure_largest_object(binary)

print("Threshold:", threshold)
if measurement:
    printable = {k: v for k, v in measurement.items() if k != "contour"}
    print("Largest object:", printable)

plt.figure()
plt.imshow(binary, cmap="gray")
plt.title("Threshold Segmentation")
plt.axis("off")
plt.show()
