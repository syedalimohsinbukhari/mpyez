"""Created on Jul 20 11:54:27 2022."""

import copy
from collections import Counter
from copy import deepcopy
from itertools import chain, compress
from typing import Any, List, Union

from .utilities.list_ import errors, utilities


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
    mask_ = [element.isalpha() for element in str_list]

    if any(mask_):
        raise errors.AlphabetFound(f'An alphabet found in the list passed, '
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
    For lists with, `len(list) % n_elements > 0`, the number of elements in the last inner list
    will not match the rest.

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


def join_lists(input_lists: List[Any], get_unique: bool = False, sort: bool = False) -> List[Any]:
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
    mask1 = [i for i, v in enumerate(out_list) if isinstance(v, list)]

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

    return out_list


class Replace:

    def __init__(self, input_list: list, work_on: Union[list, int], replace_with: Union[list, int], by: str = 'index',
                 new_list: list = False):
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
            raise errors.InvalidInputParameter('The input parameter required is, \'index\', or \'value\'.')

        if len(self.replace_with) != len(self.work_on):
            raise errors.UnequalElements(f'The number of elements in the {names[0]} list is not '
                                         f'equal to that of {names[1]}. Cannot perform '
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
            raise errors.IndexOutOfList(f'Index {join_} is out of bound for a list of length '
                                        f'{len(self.input_list)}.')

        self.__replace_values()

        return self.input_list

    def at_value(self) -> list:
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [element not in self.input_list for element in self.work_on]

        if any(bool_mask):
            join_ = ", ".join(compress(numeric_list_to_string(self.work_on), bool_mask))
            raise errors.GotAnUnknownValue(f'The value {join_} given in old_element does not exist '
                                           f'in the input_list.')

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

    return all(child in parent_list for child in child_list)


def get_object_count(input_list: list, top_n: float = -1, get_tabular_form: bool = False):
    """
    Get the count of objects in a given list.

    Parameters
    ----------
    input_list : list
        The given list to get the element count from.
    top_n : float, optional
        Whether to show top `N` elements or all of them from the list. The default is -1.
    get_tabular_form : bool, optional
        DESCRIPTION. The default is False.

    Returns
    -------
    count_obj
        Either a dictionary or a CountObjectsInList object representing the counts of objects in a
        given list.

    """
    counts = dict(Counter(input_list))

    if get_tabular_form:
        obj_ = utilities.CountObjectsInList(counts)
        count_obj = obj_[:] if top_n == -1 else obj_ if top_n == 0 else obj_[0: top_n]
        print(type(count_obj))
    else:
        count_obj = counts

    return count_obj


def sort_(input_list: list, ascending_order: bool = True, get_sorting_indices: bool = True) -> list:
    """
    Sort the given list.

    Parameters
    ----------
    input_list : list
        The list to be sorted.
    ascending_order : bool, optional
        Whether to sort the list in ascending or descending order. The default is False.
    get_sorting_indices : bool, optional
        Get the order of sort in the original list. The default is True.

    Returns
    -------
        Sorted list. Sort list indices, optional.

    """
    sort_order = False if ascending_order else True

    if get_sorting_indices:
        sorted_list = (list(i) for i in zip(*sorted(zip(input_list, range(len(input_list))))))

        return [element[::-1] for element in sorted_list] if sort_order else list(sorted_list)
    else:
        return sorted(input_list, reverse=sort_order)


def remove_(input_list: list, value_to_remove: Union[list, tuple, str, int],
            get_new_list: bool = False) -> list:
    """
    Remove a certain value from the input list.    

    Parameters
    ----------
    input_list : list
        The list from which the value is to be removed.
    value_to_remove : Union[list, tuple, str, int]
        The value to remove. The value can either be an int, str, tuple or even a nested list.
    get_new_list : bool, optional
        Whether the original list should be preserved or not. The default is False.

    Returns
    -------
    modified_list : list
        Modified list with the value removed from it.

    """
    modified_list = input_list if not get_new_list else copy.deepcopy(input_list)

    if isinstance(value_to_remove, (tuple, str, list)):
        ind_ = modified_list.index(value_to_remove)
        del modified_list[ind_]
    else:
        modified_list.pop(value_to_remove)

    return modified_list


def move_element_in_list(input_list: list, old_position: Union[list, int], new_position: Union[list, int],
                         get_new_list: bool = False) -> list:
    """
    Moves an element from `old_position` in the given list to `new_position`.

    Parameters
    ----------
    input_list : list
        The list in which the element/elements are to be moved.
    old_position : Union[list, int]
        The index (or list of index) on which the element to be moved is currently present.
    new_position : Union[list, int]
        The index (or list of index) to which the element is to be moved.
    get_new_list : bool, optional
        Whether the original list should be preserved or not. The default is False.

    Returns
    -------
    list_ :
        A list with the position of elements changed.

    """
    list_ = input_list if not get_new_list else copy.deepcopy(input_list)

    list_.insert(new_position, list_.pop(old_position))

    return list_


def difference_between_lists(input_list1, input_list2):
    diff1 = [element for element in input_list1 if element not in input_list2]
    diff2 = [element for element in input_list2 if element not in input_list1]
    return diff1, diff2


def index_(input_list, iterator):
    if isinstance(iterator, int):
        return input_list.index(iterator)
    else:
        return [input_list.index(elem) for elem in iterator]
