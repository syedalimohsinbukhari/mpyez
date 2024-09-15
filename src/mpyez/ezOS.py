"""Created on Jul 18 23:26:48 2022."""

import os
import shutil
from typing import Union

from .backend.uOS import GetFiles


class ListOfFilesFromExtensions(GetFiles):
    """Class for getting the list of files from a folder."""

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
        super(ListOfFilesFromExtensions, self).__init__(input_variable=extension,
                                                        var_type='ext',
                                                        working_directory=directory)


class ListOfFilesFromName(GetFiles):
    """Class for getting the list of files from a folder."""

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
        super(ListOfFilesFromName, self).__init__(input_variable=file_name,
                                                  var_type='name',
                                                  working_directory=directory)


def move_directory_contents(old_path: str, new_path: str):
    """
    Moves the contents from `old_path` to `new_path`.

    Parameters
    ----------
    old_path:
        The old directory from which the files are to be moved.
    new_path:
        The new directory to which the files are to be moved.
    """
    if not os.path.exists(old_path):
        raise Exception(f"The source directory '{old_path}' does not exist.")

    if not os.path.exists(new_path):
        os.makedirs(new_path)

    for item in os.listdir(old_path):
        old_item_path = os.path.join(old_path, item)
        new_item_path = os.path.join(new_path, item)
        shutil.move(old_item_path, new_item_path)

    # Optionally, remove the old directory if it's empty
    if not os.listdir(old_path):
        os.rmdir(old_path)
    else:
        print(f"Warning: '{old_path}' is not empty after move.")
