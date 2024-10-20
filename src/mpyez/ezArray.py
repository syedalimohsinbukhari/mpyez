"""Created on Jun 12 13:49:07 2024"""

import numpy as np


def transpose1d(array: np.ndarray) -> np.ndarray:
    """
    Transposes a given array.

    Parameters
    ----------
    array:
        Given numpy array.

    Returns
    -------
    np.ndarray
        Transposed numpy array
    """
    return np.array([array]).transpose() if len(array.shape) == 1 else array.transpose()


def reshape_with_padding(array: np.ndarray, new_shape: tuple, pad_value: int = 0) -> np.ndarray:
    """
    Reshape an array to a new shape with padding if necessary.

    Parameters
    ----------
    array : np.ndarray
        The input array to be reshaped.
    new_shape : tuple of int
        The desired shape for the output array.
    pad_value : scalar, optional
        The value to use for padding if the new shape requires more elements
        than the original array contains. The default is 0.

    Returns
    -------
    np.ndarray
        The reshaped array with padding applied if necessary.
    """
    new_array = np.full(new_shape, pad_value)
    new_array.flat[:len(array)] = array

    return new_array


def moving_average(array: np.ndarray, window_size: int) -> np.ndarray:
    """
    Compute the moving average of a given 1D array.

    Parameters
    ----------
    array : np.ndarray
        The 1-D array for which the moving average is to be computed.
    window_size : int
        The size of the moving window.

    Returns
    -------
    np.ndarray
        An array containing the moving averages. The length of this array will be `len(array) - window_size + 1`.
    """
    return np.convolve(array, np.ones(window_size), 'valid') / window_size
