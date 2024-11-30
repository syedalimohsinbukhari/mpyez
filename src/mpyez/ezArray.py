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


def evaluate_with_broadcast(func, constant_array, **param_arrays):
    """
    Evaluate a function with a constant array and multiple parameter arrays using broadcasting.

    Parameters
    ----------
    func : callable
        The function to evaluate. It must support broadcasting of inputs. The function signature should match `func(constant_array, **param_arrays)`.
    constant_array : ndarray
        The constant array to evaluate the function over.
    **param_arrays : dict
        Keyword arguments representing parameter arrays. Each array should be compatible with broadcasting.

    Returns
    -------
    ndarray
        The result of the function evaluation. The shape of the result is `(len(constant_array), ...)`,
        where the additional dimensions correspond to the shapes of the parameter arrays.

    Examples
    --------
    Evaluate a sine wave function over time with varying frequencies and amplitudes:

    >>> import numpy as np
    >>> def sine_wave(t, f, a):
    ...     return a * np.sin(2 * np.pi * f * t)
    >>> time = np.linspace(0, 1, 100)
    >>> frequencies = np.array([1, 2, 3])
    >>> amplitudes = np.array([0.5, 1.0, 1.5])
    >>> result = evaluate_with_broadcast(sine_wave, time, f=frequencies, a=amplitudes)
    >>> result.shape
    (100, 3)
    """
    # Expand constant_array to add a broadcastable dimension
    expanded_constant = constant_array[:, np.newaxis]

    # Expand all parameter arrays
    broadcasted_params = {key: value[np.newaxis, :] for key, value in param_arrays.items()}

    # Evaluate the function using broadcasting
    return func(expanded_constant, **broadcasted_params)
