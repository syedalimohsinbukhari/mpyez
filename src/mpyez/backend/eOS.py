"""Created on Jul 20 12:22:44 2022."""


class EzOsErrs(Exception):
    """
    Base class for custom exceptions related to EzOs operations.
    All specific errors inherit from this class.
    """
    pass


class FileNotPresent(EzOsErrs):
    """
    Raised when a specified file is not found in the expected location.

    Notes
    -----
    This error is typically raised when a file operation (e.g., reading or writing)
    is attempted on a file that does not exist.
    """
    pass
