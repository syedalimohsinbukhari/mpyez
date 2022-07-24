"""Created on Jul 18 23:26:48 2022."""

import os
from typing import Union

try:
    from utilities.ez_os.get_files import GetFiles as _GetFiles
except ImportError:
    from .utilities.ez_os.get_files import GetFiles as _GetFiles


class ListOfFilesFromExtensions(_GetFiles):
    """
    Class for getting the list of files from a folder.
    """

    def __init__(self, extension: Union[str, list], directory: str = os.curdir):
        """
        Initialization method for ListOfFiles class.

        Parameters
        ----------
        extension : Union[str, list]
            The type of file to be picked from the working_directory.
        directory : str
            The directory from where the files are to be picked.

        Examples
        ----------
        Suppose we want to pick all `.py` files from the current folder,

        >>> list_of_files = ListOfFilesFromExtensions(extension='.py')

        To see the selected files,

        >>> list_of_files.list_

        To select multiple types of files, just pass in a list

        >>> list_of_files = ListOfFilesFromExtensions(extension=['.py', '.txt'])

        Now, let's say we want to remove a `remove_me.py` from the `list_of_files`

        >>> list_of_files.exclude(exclude_file='remove_me.py')
        """

        super(ListOfFilesFromExtensions, self).__init__(input_variable=extension, var_type='ext',
                                                        working_directory=directory)


class ListOfFilesFromName(_GetFiles):

    def __init__(self, file_name: Union[str, list], directory: str = os.curdir):
        """
        Initialization method for ListOfFiles class.

        Parameters
        ----------
        file_name : Union[str, list]
            The name of file to be picked from the working_directory. The file is picked with
            `in` keyword.
        directory : str
            The directory from where the files are to be picked.

        Examples
        ----------
        Suppose we want to pick all files from the current folder with contianing `main` in their
        names,

        >>> list_of_files = ListOfFilesFromName(file_name='main')

        To see the selected files,

        >>> list_of_files.list_

        To select multiple files with different names,

        >>> list_of_files = ListOfFilesFromName(file_name=['main', 'test'])

        Now, let's say we want to remove a `remove_me.py` from the `list_of_files`

        >>> list_of_files.exclude(exclude_file='remove_me.py')
        """

        super(ListOfFilesFromName, self).__init__(input_variable=file_name, var_type='name',
                                                  working_directory=directory)
