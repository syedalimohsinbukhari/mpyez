"""
Created on Jul 18 23:26:48 2022
"""

import itertools
import os


class ListOfFilesFromExtensions:
    """
    Class for getting the list of files from a folder.
    """

    def __init__(self, file_type: str or list, directory: str = os.curdir):
        """
        Initialization method for ListOfFiles class.

        Parameters
        ----------
        file_type : str or list
            The type of file to be picked from the working_directory.
        directory : str
            The directory from where the files are to be picked.

        Examples
        ----------
        Suppose we want to pick all `.py` files from the current folder,

        >>> list_of_files = ListOfFilesFromExtensions(file_type='.py')

        To see the selected files,

        >>> list_of_files.list_

        To select multiple types of files, just pass in a list

        >>> list_of_files = ListOfFilesFromExtensions(file_type=['.py', '.txt'])

        Now, let's say we want to remove a `remove_me.py` from the `list_of_files`

        >>> list_of_files.exclude(exclude_file='remove_me.py')


        """
        self.file_type = file_type
        self.w_dir = directory
        self.lof = None

        self.__initialize_lof()

    def __initialize_lof(self):
        if isinstance(self.file_type, str):
            self.file_type = (self.file_type,)

        lof_ = ((f for f in os.listdir(self.w_dir) if f.endswith(x)) for x in
                self.file_type)

        # taken from https://stackoverflow.com/a/953097/3212945
        self.lof = list(itertools.chain.from_iterable(lof_))

    def exclude(self, exclude_file):
        if isinstance(exclude_file, str):
            exclude_file = (exclude_file,)

        tuple(self.lof.remove(x) for x in exclude_file)

    def sort(self, reverse=False):
        self.lof.sort(reverse=reverse)

    @property
    def list_(self):
        return self.lof
