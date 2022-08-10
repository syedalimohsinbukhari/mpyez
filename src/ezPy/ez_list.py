"""Created on Jul 20 11:54:27 2022."""

import copy
from collections import Counter
from copy import deepcopy
from itertools import chain, compress
from typing import Any, List, Union

try:
    from .ez_misc import is_alphabet as _is_alphabet
    from .utilities.ez_list import errors as _errors
    from .utilities.ez_list.utilities import CountObjectsInList
except ImportError:
    from ez_misc import is_alphabet as _is_alphabet
    from utilities.ez_list import errors as _errors
    from utilities.ez_list.utilities import CountObjectsInList


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
    mask_ = [_is_alphabet(element) for element in str_list]

    if any(mask_):
        raise _errors.AlphabetFound(f'An alphabet found in the list passed, '
                                    f'{", ".join(compress(str_list, mask_))} cannot be processed.')

    return list(map(int, str_list))


def nested_list_to_list(nested_list: List[Any]) -> list:
    """
    Convert nested list to a single list.

    Parameters
    ----------
    nested_list : List[Any]
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
    if mask1 is not None:
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
            mask2 = [[index for index, value in enumerate(out_list) if isinstance(value, types)] for
                     types in n_types]

            out_list = [sorted(element) for element in
                        [[out_list[value] for value in index] for index in mask2]]
            out_list = nested_list_to_list(out_list)

    if tuples_as_lists:
        for index, _ in enumerate(out_list):
            try:
                out_list[index] = list(out_list[index])
            except TypeError:
                break

    return out_list


class Replace:

    def __init__(self, input_list: list, work_on: Union[list, int], replace_with: Union[list, int],
                 by: str = 'index', new_list: list = False):
        self.input_list = deepcopy(input_list) if new_list else input_list
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
        elif self.by == 'value':
            names = ['old_elements', 'new_elements']
        else:
            raise _errors.InvalidInputParameter('The input parameter required is, \'index\', '
                                                'or \'value\'.')

        if len(self.replace_with) != len(self.work_on):
            raise _errors.UnequalElements(f'The number of elements in the {names[0]} list is '
                                          f'not equal to that of {names[1]}. Cannot perform '
                                          f'replacement in this case.')

        return self.replace_with

    def __replace_values(self, primary_list=None) -> None:
        primary_list = self.work_on if primary_list is None else primary_list

        for index, value in zip(primary_list, self.replace_with):
            self.input_list[index] = value

    def at_index(self) -> list:
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [_index > len(self.input_list) - 1 for _index in self.work_on]

        if any(bool_mask):
            join_ = ", ".join(compress(numeric_list_to_string(self.replace_with), bool_mask))
            raise _errors.IndexOutOfList(f'Index {join_} is out of bound for a list of length '
                                         f'{len(self.input_list)}.')

        self.__replace_values()

        return self.input_list

    def at_value(self) -> list:
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [element not in self.input_list for element in self.work_on]

        if any(bool_mask):
            join_ = ", ".join(compress(numeric_list_to_string(self.work_on), bool_mask))
            raise _errors.GotAnUnknownValue(f'The value {join_} given in old_element does not '
                                            f'exist in the input_list.')

        index = [self.input_list.index(element) for element in self.work_on]

        self.__replace_values(primary_list=index)

        return self.input_list


def is_contained(child_list: list, parent_list: list) -> bool:
    """
    Check if the child_list is contained within the parent_list.

    Parameters
    ----------
    child_list : list
        The list to be checked for containment in parent list.
    parent_list : list
        The list to be checked for containment of child list.

    Returns
    -------
    bool
        Whether the child list is contained within parent list or not

    Examples
    --------
    To check whether,

    >>> a = [1, '2', 3, 'A']

    is contained within

    >>> b = [1, '2', 3, 4, 5, 'A']

    the is_contained method can be used

    >>> is_contained(a, b)
    >>> True
    """
    return True if all([child in parent_list for child in child_list]) else False


def get_object_count(input_list, top_n: float = -1):
    obj_ = CountObjectsInList(dict(Counter(input_list)))

    return obj_[:] if top_n == -1 else obj_ if top_n == 0 else obj_[0: top_n]


def sort_(input_list, reverse=False, get_sorting_indices=False):
    if get_sorting_indices:
        ind = range(len(input_list))
        out = [list(i) for i in zip(*sorted(zip(input_list, ind)))]

        return [i[::-1] for i in out] if reverse else out
    else:
        return sorted(input_list, reverse=reverse)


def remove_(input_list, value_to_remove):
    if isinstance(value_to_remove, (tuple, str, list)):
        ind_ = input_list.index(value_to_remove)
        del input_list[ind_]
    else:
        input_list.pop(value_to_remove)

    return input_list


def move_element_in_list(input_list, old_position, new_position, get_new_list=False):
    inp_ = input_list if not get_new_list else copy.deepcopy(input_list)

    inp_.insert(new_position, inp_.pop(old_position))

    return inp_
