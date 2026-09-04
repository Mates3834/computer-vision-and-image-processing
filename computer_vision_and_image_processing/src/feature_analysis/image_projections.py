import numpy as np

def vertical_projection(binary):
    """Sum foreground pixels along image rows."""
    mask = np.asarray(binary) > 0
    return mask.sum(axis=0)

def horizontal_projection(binary):
    """Sum foreground pixels along image columns."""
    mask = np.asarray(binary) > 0
    return mask.sum(axis=1)
