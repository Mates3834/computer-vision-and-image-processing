import cv2
import numpy as np

def to_grayscale(image):
    """Convert a BGR/RGB-like image to uint8 grayscale."""
    if image is None:
        raise ValueError("Input image is None.")
    if image.ndim == 2:
        return image.astype(np.uint8)
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def histogram(gray):
    """Return the 256-bin grayscale histogram."""
    gray = to_grayscale(gray)
    return cv2.calcHist([gray], [0], None, [256], [0, 256]).ravel()
