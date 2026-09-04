import numpy as np

def rle_encode(array):
    """
    Run-Length Encode a NumPy array.

    Returns:
        values, counts, original_shape
    """
    arr = np.asarray(array)
    flat = arr.ravel()
    if flat.size == 0:
        return np.array([]), np.array([], dtype=int), arr.shape

    changes = np.r_[True, flat[1:] != flat[:-1]]
    starts = np.flatnonzero(changes)
    values = flat[starts]
    ends = np.r_[starts[1:], flat.size]
    counts = ends - starts
    return values, counts.astype(int), arr.shape

def rle_decode(values, counts, shape):
    """Reconstruct an array from RLE values and counts."""
    decoded = np.repeat(values, counts)
    return decoded.reshape(shape)
