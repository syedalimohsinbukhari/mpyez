"""Created on Jul 23 18:38:52 2022."""

from .eIO import LineNumberOutOfBounds


def check_for_errors(open_file: list, lines_to_read: list):
    """
    Checks if the requested lines to read are within the valid range for the file.

    Parameters
    ----------
    open_file : list
        A list of file content lines.
    lines_to_read : list
        A list of line numbers requested to be read.

    Raises
    ------
    LineNumberOutOfBounds
        If any line number is out of the bounds of the file.
    """

    file_length = len(open_file)
    err = False

    # Check if all line numbers are non-negative
    if all(line >= 0 for line in lines_to_read):
        if max(lines_to_read) >= file_length:
            err = True

    # Check if any negative line numbers are present
    elif any(line < 0 for line in lines_to_read):
        if abs(min(lines_to_read)) > file_length:
            err = True
        else:
            # Adjust negative indices to correspond to positive ones (from the end)
            for idx, line in enumerate(lines_to_read):
                if line < 0:
                    lines_to_read[idx] += file_length

    if err:
        raise LineNumberOutOfBounds("The line number specified is outside the line numbers of the file.")
