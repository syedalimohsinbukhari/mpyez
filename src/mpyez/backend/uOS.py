"""Created on Jul 20 00:17:54 2022."""

import itertools
import os
from typing import Union

from .eOS import FileNotPresent


class GetFiles:

    def __init__(self, input_variable, var_type, working_directory=os.curdir):
        self.input_variable = input_variable
        self.w_dir = working_directory
        self.var_type = var_type

        self.lof = None

        self.__initialize_lof()

    def __initialize_lof(self):
        """Get the list of files from the input folder with the given extension(s)."""
        if isinstance(self.input_variable, str):
            self.input_variable = (self.input_variable,)

        if self.var_type == 'ext':
            lof_ = ((f for f in os.listdir(self.w_dir) if f.endswith(x) and not os.path.isdir(f))
                    for x in self.input_variable)
        else:
            lof_ = ((f for f in os.listdir(self.w_dir) if x in f and not os.path.isdir(f)) for x in
                    self.input_variable)

        # taken from https://stackoverflow.com/a/953097/3212945
        self.lof = list(itertools.chain.from_iterable(lof_))

    def exclude(self, exclude_file: Union[str, list]):
        """
        Exclude specific files from the obtained list of files.

        Parameters
        ----------
        exclude_file : Union[str, list]
            File name or list of files to exclude from the obtained list of files.
        """
        if isinstance(exclude_file, str):
            exclude_file = (exclude_file,)

        mask_ = [x not in self.lof for x in exclude_file]

        if True in mask_:
            raise FileNotPresent(f'The file(s) named '
                                 f'{", ".join(itertools.compress(exclude_file, mask_))} '
                                 f'do not exist in the list of files.')
        else:
            tuple(self.lof.remove(x) for x in exclude_file)

    def sort(self, reverse: bool = False):
        """
        Sort the list of files obtained.

        Parameters
        ----------
        reverse : bool, optional
            Whether to reverse the sorting order of the list of files or not. The default is False.
        """
        self.lof.sort(reverse=reverse)

    @property
    def list_(self) -> list:
        """
        Show the list of files obtained.

        Returns
        -------
        list
            List of files matching the input extension.
        """
        return self.lof
