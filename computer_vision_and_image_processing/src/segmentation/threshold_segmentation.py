import cv2
import numpy as np
from src.enhancement.grayscale import to_grayscale

def threshold_segment(image, threshold=None, invert=False):
    """
    Binary threshold segmentation.

    If threshold is None, Otsu's method is used.
    Returns: binary image, threshold used.
    """
    gray = to_grayscale(image)
    mode = cv2.THRESH_BINARY_INV if invert else cv2.THRESH_BINARY

    if threshold is None:
        value, binary = cv2.threshold(gray, 0, 255, mode | cv2.THRESH_OTSU)
    else:
        value, binary = cv2.threshold(gray, float(threshold), 255, mode)

    return binary.astype(np.uint8), float(value)
