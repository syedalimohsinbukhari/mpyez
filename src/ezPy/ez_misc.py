"""Created on Jul 24 14:55:53 2022."""

from re import search
from typing import Any


def is_alphabet(input_: Any) -> bool:
    """
    Check if the given input is an alphabet or not.

    Parameters
    ----------
    input_ : Any
        The input string to be checked

    Returns
    -------
    bool
        ``True`` if the input_ is string, else ``False``.

    Examples
    --------
    Let's say we have

    >>> a = 'A'

    as an input, and we want to check whether it is alphabet or not,

    >>> is_alphabet(a)
    >>> True

    However, if

    >>> a = 1

    >>> is_alphabet(a)
    >>> False
    """
    if not isinstance(input_, str):
        input_ = str(input_)

    return True if search(r'[A-Za-z]', input_) is not None else False


def is_numeric(input_: Any) -> bool:
    """
    Check whether the input is numeric or not.

    Parameters
    ----------
    input_ : Any
        Input to be checked.

    Returns
    -------
    bool
        ``True`` of ``False`` depending upon the input being numeric or not.

    Examples
    --------
    Let's say we have

    >>> a = 1

    and we want to check whether the varaible is numeric or not,

    >>> is_numeric(a)
    >>> True
    """
    return True if isinstance(input_, int or float) else False
