"""Created on Jul 20 12:21:33 2022."""


class EzListErrs(Exception):
    """
    Base class for custom exceptions related to EzList operations.
    All specific errors inherit from this class.
    """
    pass


class AlphabetFound(EzListErrs):
    """
    Raised when an unexpected alphabet character is found in the list.

    Notes
    -----
    This error is typically raised when numeric operations are attempted
    on a list that contains alphabetic strings.
    """
    pass


class IndexOutOfList(EzListErrs):
    """
    Raised when an index is out of the valid range of the list.

    Notes
    -----
    This error occurs when an attempt is made to access or modify a list
    using an index that exceeds the bounds of the list.
    """
    pass


class UnequalElements(EzListErrs):
    """
    Raised when lists have unequal elements where equality is expected.

    Notes
    -----
    This error may be raised when operations requiring equal-length lists
    or matching elements are attempted but the lists differ in size or content.
    """
    pass


class GotAnUnknownValue(EzListErrs):
    """
    Raised when an unknown or unexpected value is encountered.

    Notes
    -----
    This error is raised when a list contains a value that does not conform
    to the expected data type or range.
    """
    pass


class ChildListLengthError(EzListErrs):
    """
    Raised when a child list has an invalid length.

    Notes
    -----
    This error is raised in scenarios where nested or child lists are
    expected to meet specific length constraints but fail to do so.
    """
    pass


class StringNotPassed(EzListErrs):
    """
    Raised when a string input is expected but not provided.

    Notes
    -----
    This error is raised when a function or operation requires a string
    input but receives a non-string value instead.
    """
    pass


class InvalidInputParameter(EzListErrs):
    """
    Raised when an invalid parameter is passed to a function or method.

    Notes
    -----
    This error indicates that one or more input arguments to a function
    do not meet the expected type, range, or format.
    """
    pass
