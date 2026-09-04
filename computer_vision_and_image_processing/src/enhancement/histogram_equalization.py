import cv2
from src.enhancement.grayscale import to_grayscale

def equalize_grayscale(image):
    """Apply global histogram equalization to a grayscale image."""
    gray = to_grayscale(image)
    return cv2.equalizeHist(gray)
