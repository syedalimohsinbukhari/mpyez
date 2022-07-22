"""Created on Jul 20 11:54:27 2022."""

from copy import deepcopy
from itertools import chain, compress
from re import search
from typing import Any, List, Union

try:
    from .utilities.ez_list import errors, misc
except ImportError:
    from utilities.ez_list import errors, misc


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


def numeric_list_to_string(num_list: List[int]) -> List[str]:
    """
    Convert all elements of a numeric lists to string.

    Parameters
    ----------
    num_list : List[int]
        A list containing numeric values.

    Returns
    -------
    List[str]
        A list containing strings equivalent to the numbers in the input list.

    Examples
    --------
    Let's say we have

    >>> a = [1, 2, 3, 4, 5]

    and we want to convert each element in thist list to string,

    >>> numeric_list_to_string(a)
    >>> ['1', '2', '3', '4', '5']
    """
    return list(map(str, num_list))


def string_list_to_numeric(str_list: list) -> list:
    """
    Convert all elements of a string lists to numeric.

    Parameters
    ----------
    str_list : list
        A list containing string elements.

    Raises
    ------
    errors.AlphabetFound
        This error is raised when the string is alphabetical in nature and not numerical.

    Returns
    -------
    list
        A list containing numeric elements.
    """
    mask_ = [is_alphabet(element) for element in str_list]

    if any(mask_):
        raise errors.AlphabetFound(f'An alphabet found in the list passed, {", ".join(compress(str_list, mask_))} '
                                   f'cannot be processed.')

    return list(map(str, str_list))


def nested_list_to_list(nested_list: List[list]) -> list:
    """
    Convert nested list to a single list.

    Parameters
    ----------
    nested_list : List[list]
        An even/uneven nested list.

    Returns
    -------
    list
        A 1D list.

    Examples
    --------
    To convert

    >>> a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    to a simple 1D list,

    >>> nested_list_to_list(a)
    >>> [1, 2, 3, 4, 5, 6, 7, 8, 9]

    Uneven lists can also be converted to 1D lists,

    >>> a = [[1, 2, 3], [4, 5], [6]]
    >>> nested_list_to_list(a)
    >>> [1, 2, 3, 4, 5, 6]
    """
    return list(chain.from_iterable(nested_list))


def list_to_nested_list(input_list: list, n_elements: int) -> List[list]:
    """
    Convert a single list to nested list.

    Parameters
    ----------
    input_list : list
        A simple, single list.
    n_elements : int
        Number of elements in each list.

    Returns
    -------
    List[list]
        A nested list with the n_elements per inner list.

    Notes
    -----
    For lists with,

    >>> len(list) % n_elements > 0

    the number of elements in the last inner list will not match the rest.

    Examples
    --------
    To convert,

    >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    into a nested list with 3 elements per list,

    >>> list_to_nested_list(a, 3)
    >>> [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    Similarly, for the nested list to have four elements per inner list,

    >>> list_to_nested_list(a, 4)
    >>> [[1, 2, 3, 4], [5, 6, 7, 8], [9]]
    """

    return [input_list[i:i + n_elements] for i in range(0, len(input_list), n_elements)]


def join_lists(input_lists: List[Any], get_unique: bool = False, sort: bool = False,
               tuples_as_lists: bool = False) -> List[Any]:
    """
    Joins two or more lists.

    Parameters
    ----------
    input_lists : List[Any]
        A nested list with lists, tuples, ints, or floats in it.
    get_unique: bool
        Whether the output should contain unique values or not. The default if False.
    sort : bool
        Whether the output should be sorted or not. The default is False.
    tuples_as_lists : bool
        Whether the tuples in output should be converted to list or not. The default is False.

    Returns
    -------
    List[Any]
        A merger of all the input lists.
    """
    # taken from https://www.geeksforgeeks.org/extending-list-python-5-different-ways/
    out_list = list(chain([], *input_lists))

    # get indices of all list elements with type == list
    mask1 = [i for i, v in enumerate(out_list) if type(v) == list]

    # change the values at mask1 indices from lists to tuples
    if mask1:
        for value in mask1:
            out_list[value] = tuple(out_list[value])

    # taken from https://stackoverflow.com/a/58666031/3212945
    if get_unique:
        unique = set()
        out_list = [value for value in out_list if not (value in unique or unique.add(value))]

    if sort:
        try:
            out_list = sorted(out_list)
        except TypeError:
            n_types = list(set([type(element) for element in out_list]))
            mask2 = [[index for index, value in enumerate(out_list) if isinstance(value, types)] for types in n_types]

            out_list = [sorted(element) for element in [[out_list[value] for value in index] for index in mask2]]
            out_list = nested_list_to_list(out_list)

    if tuples_as_lists:
        for index, _ in enumerate(out_list):
            try:
                out_list[index] = list(out_list[index])
            except TypeError:
                break

    return out_list


class Replace:

    def __init__(self, input_list: list, work_on: Union[list, int], replace_with: Union[list, int], by: str = 'index',
                 new_list: list = False):
        if new_list:
            self.input_list = deepcopy(input_list)
        else:
            self.input_list = input_list
        self.work_on = work_on
        self.replace_with = replace_with
        self.by = by

    def __convert_inputs_to_lists(self):
        if not isinstance(self.work_on, list):
            self.work_on = [self.work_on]

        if not isinstance(self.replace_with, list):
            self.replace_with = [self.replace_with]

        return self.work_on, self.replace_with

    def __equalizing_list_length(self) -> list:
        if self.by == 'index':
            names = ['index', 'value']
        else:
            names = ['old_elements', 'new_elements']

        if len(self.replace_with) > len(self.work_on):
            raise errors.UnequalElements(f'The number of elements in the {names[0]} list is '
                                         f'greater than that of {names[1]}. Cannot perform '
                                         f'replacement in this case.')
        elif len(self.replace_with) < len(self.work_on):
            diff = len(self.work_on) - len(self.replace_with)
            self.replace_with = self.replace_with * (diff + 1)
        else:
            self.replace_with = self.replace_with

        return self.replace_with

    def __replace_values(self, primary_list=None) -> None:
        primary_list = self.work_on if primary_list is None else primary_list

        for index_, value_ in zip(primary_list, self.replace_with):
            self.input_list[index_] = value_

    def at_index(self) -> list:
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [_index > len(self.input_list) - 1 for _index in self.work_on]

        if True in bool_mask:
            join_ = ", ".join(compress(numeric_list_to_string(self.replace_with), bool_mask))
            raise errors.IndexOutOfList(f'Index {join_} is out of bound for a list of length '
                                        f'{len(self.input_list)}.')

        self.__replace_values()

        return self.input_list

    def at_value(self) -> list:
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [element not in self.input_list for element in self.work_on]

        if True in bool_mask:
            join_ = ", ".join(compress(numeric_list_to_string(self.work_on), bool_mask))
            raise errors.GotAnUnknownValue(f'The value {join_} given in old_element does not exist '
                                           f'in the input_list.')

        index = [self.input_list.index(element) for element in self.work_on]

        self.__replace_values(primary_list=index)

        return self.input_list


def is_contained(child_list: list, parent_list: list) -> bool:
    return True if all([child in parent_list for child in child_list]) else False
