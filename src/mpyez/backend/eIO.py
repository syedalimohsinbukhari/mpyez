"""Created on Jul 23 17:17:17 2022."""


class EzFileErrs(Exception):
    """
    Base class for exceptions in EzFile.

    Notes
    -----
    This serves as the base class for all exceptions related to file operations
    in the EzFile module. Specific exceptions should inherit from this class.
    """
    pass


class LineNumberOutOfBounds(EzFileErrs):
    """
    Raised when a specified line number is out of the bounds of the file.

    Notes
    -----
    This error occurs when an operation attempts to access a line number
    that exceeds the number of lines in the file or is less than 1.
    """
    pass
