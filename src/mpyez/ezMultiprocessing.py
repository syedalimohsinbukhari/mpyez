"""Created on Jun 12 13:48:59 2024"""

from collections import defaultdict
from multiprocessing import Pool
from typing import Any, Callable, Dict, List

import numpy as np


def _reshape(lst: List[Any], n: int) -> List[List[Any]]:
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


class MultiProcessor:
    """Generalized multiprocessing functionality."""

    def __init__(self, func: Callable[..., Dict], args: List[List[Any]], n_processors: int = 3, result_handler: Callable = None):
        """
        Initialize the `MultiProcessor` class.

        Parameters
        ----------
        func: Callable
            Function to be processed.
        args: list of lists
            A list of arguments to be passed onto the given function.
        n_processors: int, optional
            The number of processors to use for multiprocessing. Default is 3.
        result_handler: Callable, optional
            A function to handle results after processing. Defaults to `defaultdict(list)`.

        Raises
        ------
        ValueError
            If `n_processors` is less than 1, or if `args` is malformed.
        """
        if n_processors < 1:
            raise ValueError("`n_processors` must be at least 1.")
        if not all(isinstance(arg, list) for arg in args):
            raise ValueError("Each element of `args` must be a list.")

        self.func = func
        self.args = args
        self.n_proc = n_processors
        self.n_values = len(self.args[0])
        self.result_handler = result_handler or (lambda results: defaultdict(list))

    def run(self) -> Dict:
        # Reshape the arguments to split the work across processors
        reshaped_args = np.array([list(_reshape(i, self.n_proc)) for i in self.args])
        reshaped_args = reshaped_args.transpose()
        flattened_args = [list(chunk) for chunk in reshaped_args]

        with Pool(self.n_proc) as pool:
            try:
                # Use starmap to correctly pass the arguments to the function
                results = pool.starmap(self.func, flattened_args)
            except Exception as e:
                raise RuntimeError(f"Error occurred during parallel execution: {e}")

        new_dict = self.result_handler(results)
        return new_dict


def sine_wave(t_low, t_high, f, a, phi):
    """Generate a sine wave.

    Parameters
    ----------
    t_low:
        The start time for the wave.
    t_high:
        The end time for the wave.
    f:
        The frequency for the wave.
    a:
        The amplitude of the wave.
    phi:
        The phase of the wave.

    Returns
    -------
    dict
        A dictionary with sine wave values for each time `t`.
    """
    t = np.linspace(t_low, t_high, 1000)
    return {f"wave_{i}": a * np.sin(2 * np.pi * f * t[i] + phi) for i in range(len(t))}


# Time and other parameters for the waves
f_ = np.linspace(0, 1, 16).tolist()  # Frequencies for the waves (in Hz)
a_ = np.linspace(0, 1, 16).tolist()  # Amplitudes for each wave
phi_ = np.linspace(-2 * np.pi, 2 * np.pi, 16).tolist()  # Phases for the waves
t_l = np.repeat(0, len(f_)).tolist()  # Start time for each sine wave
t_h = np.repeat(1, len(f_)).tolist()  # End time for each sine wave

# Arguments to be passed to the function
arguments = [t_l, t_h, f_, a_, phi_]

# Create the MultiProcessor instance and run it
processor = MultiProcessor(func=sine_wave, args=arguments, n_processors=4)
result = processor.run()

# Print the results
print(result)
