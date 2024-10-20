"""Created on Jul 20 11:54:27 2022."""

import copy
from collections import Counter
from itertools import chain, compress
from typing import Any, List, Union

from .backend import eList as eL
from .backend.uList import CountObjectsInList, Replace


def equal_lists(lists: list) -> bool:
    """
    Check if all lists within a list have the same length.

    Parameters
    ----------
    lists : list of lists
        A list containing sublists to be checked.

    Returns
    -------
    bool
        True if all sublists have the same length, False otherwise.

    Examples
    --------
    >>> equal_lists([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    True
    >>> equal_lists([[1, 2, 3], [4, 5], [7, 8, 9]])
    False
    """
    return len(set(map(len, lists))) == 1


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
        raise eL.AlphabetFound(f'An alphabet found in the list passed, '
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
        obj_ = CountObjectsInList(counts)
        count_obj = obj_[:] if top_n == -1 else obj_ if top_n == 0 else obj_[0: top_n]
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
    list :
        A list with the position of elements changed.

    """
    temp_ = input_list if not get_new_list else copy.deepcopy(input_list)

    temp_.insert(new_position, temp_.pop(old_position))

    return temp_


def replace_at_index(input_list: list, work_on: Union[list, int], replace_with: Union[list, int], new_list: bool = False):
    """
    Replace elements in `input_list` at specific indices.

    Parameters
    ----------
    input_list : list
        The original list to modify.
    work_on : Union[list, int]
        A single index or a list of indices where elements will be replaced.
    replace_with : Union[list, int]
        A single value or list of values that will replace the existing elements at the specified indices.
    new_list : bool, optional
        If True, returns a new list with the replacements. Otherwise, modifies the original list in place. Default is False.

    Returns
    -------
    list
        The modified list with replaced values.
    """
    return Replace(input_list, work_on, replace_with, new_list).at_index()


def replace_with_value(input_list: list, work_on: Union[list, int], replace_with: Union[list, int], new_list: bool = False):
    """
    Replace specific values in `input_list` with new values.

    Parameters
    ----------
    input_list : list
        The original list to modify.
    work_on : Union[list, int]
        A single value or list of values that will be replaced in the list.
    replace_with : Union[list, int]
        A single value or list of values that will replace the specified values.
    new_list : bool, optional
        If True, returns a new list with the replacements. Otherwise, modifies the original list in place. Default is False.

    Returns
    -------
    list
        The modified list with replaced values.
    """
    return Replace(input_list, work_on, replace_with, new_list, 'value').at_value()


def difference_between_lists(input_list1: list, input_list2: list):
    """
    Find the differences between two lists.

    Parameters
    ----------
    input_list1 : list
        The first list to compare.
    input_list2 : list
        The second list to compare.

    Returns
    -------
    tuple of lists
        Two lists representing the differences:
        - First list contains elements in `input_list1` not in `input_list2`.
        - Second list contains elements in `input_list2` not in `input_list1`.
    """
    diff1 = [element for element in input_list1 if element not in input_list2]
    diff2 = [element for element in input_list2 if element not in input_list1]
    return diff1, diff2


def index_(input_list: list, iterator: Union[list, int]):
    """
    Get the index or indices of specific values in `input_list`.

    Parameters
    ----------
    input_list : list
        The list to search for values.
    iterator : Union[list, int]
        A single value or list of values for which indices will be returned.

    Returns
    -------
    Union[int, list of int]
        The index of the value if `iterator` is a single value, or a list of indices if `iterator` is a list.
    """
    if isinstance(iterator, int):
        return input_list.index(iterator)
    else:
        return [input_list.index(elem) for elem in iterator]
