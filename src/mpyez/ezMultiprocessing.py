"""Created on Jun 12 13:48:59 2024"""

from multiprocessing import Pool
from typing import Callable, Dict, List

import numpy as np


class MultiProcessor:
    """Generalized multiprocessing functionality for processing dictionary inputs."""

    def __init__(self, func: Callable, args: Dict[str, List], n_processors: int = 3):
        """
        Initialize the `MultiProcessor` class.

        Parameters
        ----------
        func: Callable
            Function to be processed. The function should take arguments corresponding to the keys in the dictionary.
        args: Dict[str, List]
            A dictionary where keys are argument names, and values are lists of values for those arguments.
        n_processors: int, optional
            The number of processors to use for multiprocessing. Default is 3.
        """
        if n_processors < 1:
            raise ValueError("`n_processors` must be at least 1.")

        self.func = func
        self.args = args
        self.n_proc = n_processors

        lengths = [len(v) for v in args.values()]
        if len(set(lengths)) != 1:
            raise ValueError("All argument lists must have the same length.")

        self.arg_tuples = list(zip(*self.args.values()))

    def run(self) -> np.ndarray:
        """Run the multiprocessing task."""
        with Pool(self.n_proc) as pool:
            try:
                results = pool.starmap(self.func, self.arg_tuples)
            except Exception as e:
                raise RuntimeError(f"Error occurred during parallel execution: {e}")

        return np.array(results)
