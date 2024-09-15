"""Created on Jul 23 17:17:17 2022."""


class EzFileErrs(Exception):
    """Base class for exceptions in EzFile."""
    pass


class LineNumberOutOfBounds(EzFileErrs):
    """Exception raised when a line number is out of bounds."""
    pass
