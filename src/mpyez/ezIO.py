"""Created on Jul 23 16:56:48 2022."""

from .backend.uIO import check_for_errors


def read_txt_file(file_to_read: str) -> list:
    """
    Reads a text file and returns its contents as a list of stripped lines.

    This function reads the specified text file line by line, strips any newline characters,
    and returns a list of those lines.

    Parameters
    ----------
    file_to_read : str
        The path to the text file to be read.

    Returns
    -------
    list of str
        A list containing each line from the file, with newline characters removed.

    Raises
    ------
    FileNotFoundError
        If the file specified by `file_to_read` does not exist or cannot be accessed.
    IOError
        If there is an issue reading the file.
    """
    with open(file_to_read, 'r') as file:
        return [line.strip() for line in file]


def get_lines_from_txt_file(file_to_read: str, lines_to_read: list) -> list:
    """
    Retrieves specific lines from a text file.

    This function reads a file and returns only the specified lines from the file.
    If `lines_to_read` is a single integer, it is converted to a list. The function
    uses zero-based indexing for line numbers.

    Parameters
    ----------
    file_to_read : str
        The path to the text file to be read.
    lines_to_read : list of int or int
        The line numbers (zero-based) to retrieve from the file. If a single integer is provided,
        it will be treated as a list with one element.

    Returns
    -------
    list of str
        A list of the lines from the file that correspond to the provided line numbers.

    Raises
    ------
    ValueError
        If any of the requested line numbers exceed the total number of lines in the file.
    TypeError
        If `lines_to_read` is not an integer or a list of integers.
    """
    out = read_txt_file(file_to_read)

    if not isinstance(lines_to_read, list):
        lines_to_read = [lines_to_read]

    if not all(isinstance(line, int) for line in lines_to_read):
        raise TypeError("lines_to_read must be an integer or a list of integers.")

    check_for_errors(open_file=out, lines_to_read=lines_to_read)

    # taken from https://stackoverflow.com/a/2082131/3212945
    return [value for index, value in enumerate(out) if index in set(lines_to_read)]
