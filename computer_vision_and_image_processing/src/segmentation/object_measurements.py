import cv2
import numpy as np

def measure_largest_object(binary):
    """
    Measure the largest external binary object.

    Returns area, centroid, bounding box and orientation.
    Orientation is estimated from second-order central moments.
    """
    binary = np.asarray(binary, dtype=np.uint8)
    contours, _ = cv2.findContours(
        binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE
    )
    if not contours:
        return None

    contour = max(contours, key=cv2.contourArea)
    area = float(cv2.contourArea(contour))
    x, y, w, h = cv2.boundingRect(contour)

    m = cv2.moments(contour)
    if abs(m["m00"]) > 1e-12:
        cx = m["m10"] / m["m00"]
        cy = m["m01"] / m["m00"]
    else:
        cx, cy = x + w / 2.0, y + h / 2.0

    denom = m["mu20"] - m["mu02"]
    theta = 0.5 * np.arctan2(2.0 * m["mu11"], denom)

    return {
        "area": area,
        "centroid": (float(cx), float(cy)),
        "bounding_box": (int(x), int(y), int(w), int(h)),
        "orientation_deg": float(np.degrees(theta)),
        "contour": contour,
    }
