"""Created on Jul 24 14:55:53 2022."""

import itertools
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
    return input_.isalpha()


def is_numeric(input_: Any, bool_check=True, get_mask=False, get_numeric=False):
    """
    Check whether the input is numeric or not.

    Parameters
    ----------
    input_ : Any
        Input to be checked. Can be a single value or a list.
    bool_check : bool
        Check if all the elements of input list are numeric or not. The default is True.
    get_mask : bool
        Get the numeric mask for the input_array. The default is False.
    get_numeric: bool
        Get the numeric values from a mixed list.

    Returns
    -------


    Examples
    --------
    Let's say we have

    >>> a = 1

    and we want to check whether the varaible is numeric or not,

    >>> is_numeric(a)
    >>> True
    """
    if not isinstance(input_, list):
        input_ = [input_]

    num_mask = [isinstance(value, int) for value in input_]

    out = []

    if get_mask:
        out.append(num_mask)
    if bool_check:
        out.append(all(num_mask))
    if get_numeric:
        out.append(list(itertools.compress(input_, num_mask)))

    return out
