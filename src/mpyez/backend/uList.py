"""Created on Jul 20 21:45:16 2022."""

from copy import deepcopy
from itertools import compress
from typing import Any, Dict, List, Union

from . import eList as eL


def equalizing_list_length(primary_list: List, secondary_list: List) -> List:
    """
    Adjusts the length of the secondary list to match the length of the primary list.

    If the secondary list is shorter, it is extended by repeating its elements cyclically.
    If the secondary list is longer, an error is raised.

    Parameters
    ----------
    primary_list : list
        The reference list whose length needs to be matched.
    secondary_list : list
        The list to be adjusted to the length of the primary list.

    Returns
    -------
    list
        The adjusted secondary list, with a length equal to the primary list.

    Raises
    ------
    UnequalElements
        If the secondary list has more elements than the primary list.
    """
    primary_length = len(primary_list)
    secondary_length = len(secondary_list)

    if secondary_length > primary_length:
        raise eL.UnequalElements(f"The secondary list ({secondary_length} elements) is longer than the primary list ({primary_length} elements).")
    elif secondary_length < primary_length:
        # Extend secondary_list cyclically to match the length of primary_list
        secondary_list += secondary_list[:primary_length - secondary_length]

    return secondary_list


def replace_at_index(input_list: List, index: Union[int, List[int]], value: Union[Any, List[Any]], new_list: bool = False) -> List:
    """
    Replaces elements in a list at specified indices with new values.

    Parameters
    ----------
    input_list : list
        The original list whose elements need to be replaced.
    index : int or list of int
        The index or indices of the elements to replace.
    value : any or list of any
        The new value(s) to insert at the specified index/indices.
    new_list : bool, optional
        If True, returns a modified copy of the original list. If False, modifies
        the list in place (default is False).

    Returns
    -------
    list
        The modified list with replaced values.

    Raises
    ------
    IndexOutOfList
        If any index in `index` is out of bounds for the input list.
    ValueError
        If the number of indices does not match the number of values.

    Examples
    --------
    >>> input_ = [1, 2, 3, 4]
    >>> replace_at_index(input_, [1, 3], [9, 10])
    [1, 9, 3, 10]

    >>> replace_at_index([1, 2, 3, 4], 2, 99)
    [1, 2, 99, 4]
    """
    # Ensure index and value are lists for uniform processing
    index = [index] if not isinstance(index, list) else index
    value = [value] if not isinstance(value, list) else value

    # Check if the number of indices matches the number of values
    if len(index) != len(value):
        raise ValueError(f"The number of indices ({len(index)}) must match the number of values ({len(value)}).")

    # Validate indices are within bounds
    for i in index:
        if i >= len(input_list) or i < 0:
            raise eL.IndexOutOfList(f"Index {i} is out of bounds for a list of length {len(input_list)}.")

    # Create a new list if requested
    if new_list:
        input_list = deepcopy(input_list)

    # Replace elements at the specified indices
    for i, v in zip(index, value):
        input_list[i] = v

    return input_list


def replace_element(input_list: List[Union[int, float, str]],
                    old_elements: Union[List[Union[int, float, str]], Union[int, float, str]],
                    new_elements: Union[List[Union[int, float, str]], Union[int, float, str]],
                    new_list: bool = False) -> List[Union[int, float, str]]:
    """
    Replaces elements in a list with new values at corresponding indices.

    Parameters
    ----------
    input_list : list of int, float, or str
        The original list in which elements will be replaced.
    old_elements : int, float, str, or list of int, float, str
        The element(s) to be replaced in the input_list.
    new_elements : int, float, str, or list of int, float, str
        The new value(s) to replace the old_elements.
    new_list : bool, optional
        If True, returns a modified copy of the original list. If False, modifies
        the list in place (default is False).

    Returns
    -------
    list of int, float, or str
        The modified list with the replaced elements.

    Raises
    ------
    GotAnUnknownValue
        If any value in old_elements does not exist in the input_list.
    UnequalElements
        If old_elements and new_elements lists have different lengths.

    Notes
    -----
    - The lengths of old_elements and new_elements must match if they are provided as lists.
    - If a single element is provided in old_elements or new_elements, it will be applied to all occurrences of old_elements in input_list.
    """
    if not isinstance(old_elements, list):
        old_elements = [old_elements]
    if not isinstance(new_elements, list):
        new_elements = [new_elements]

    if len(old_elements) != len(new_elements):
        raise eL.UnequalElements(f'The number of elements in old_elements ({len(old_elements)}) does not match '
                                 f'the number of elements in new_elements ({len(new_elements)}).')

    indices = []
    for old in old_elements:
        if old not in input_list:
            raise eL.GotAnUnknownValue(f'The value {old} given in old_elements does not exist in the input_list.')
        indices.append(input_list.index(old))

    if new_list:
        input_list = input_list[:]

    for i, new in zip(indices, new_elements):
        input_list[i] = new

    return input_list


class CountObjectsInList:
    """Class to count objects in the given list."""

    def __init__(self, counter_dict: Dict[Union[str, int], int]):
        """
        Initialize the CountObjectsInList with a dictionary containing items and their counts.

        Parameters
        ----------
        counter_dict : dict
            A dictionary where keys are items (could be strings or other types),
            and values are their corresponding counts.
        """
        self.counter_dict = counter_dict
        self.__counter_dict = sorted(self.counter_dict.items(), key=lambda x: x[1], reverse=True)

    def __str__(self) -> str:
        """Return a formatted string representing the counts of the objects in the list. The items and their counts are displayed in a table format.

        Returns
        -------
        str
            A string representation of the object with formatted counts.
        """
        out = '-' * 50 + '\n'
        out += f'|{"items":^30}|{"counts":^17}|\n'
        out += '-' * 50 + '\n'

        for key, value in self.counter_dict.items():
            if isinstance(key, str):
                out += f"|\'{key}\':^30|{value:^17}|\n"
            else:
                out += f"|{key:^30}|{value:^17}|\n"
        out += '-' * 50 + '\n'
        return out

    def __getitem__(self, item: int) -> 'CountObjectsInList':
        """
        Retrieve a specific item from the sorted counter list and return a new CountObjectsInList instance.

        Parameters
        ----------
        item : int
            The index of the item in the sorted counter list.

        Returns
        -------
        CountObjectsInList
            A new CountObjectsInList instance with the corresponding item and its count.
        """
        if item < 0 or item >= len(self.__counter_dict):
            raise IndexError("Index out of bounds.")

        selected_item = self.__counter_dict[item]

        return CountObjectsInList({selected_item[0]: selected_item[1]})


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


class Replace:
    """Class to replace stuff inside a given list."""

    def __init__(self, input_list: list, work_on: Union[list, int], replace_with: Union[list, int],
                 new_list: bool = False, by: str = 'index'):
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
            raise eL.InvalidInputParameter('The input parameter required is, \'index\', or \'value\'.')

        if len(self.replace_with) != len(self.work_on):
            raise eL.UnequalElements(f'The number of elements in {names[0]} list is not equal to that of {names[1]}.'
                                     f' Cannot perform replacement in this case.')

        return self.replace_with

    def __replace_values(self, primary_list=None) -> None:
        primary_list = self.work_on if primary_list is None else primary_list

        for index, value in zip(primary_list, self.replace_with):
            self.input_list[index] = value

    def at_index(self) -> list:
        """
        Replaces the elements on the specified indices.

        Returns
        -------
        list:
            A list with replaced values.
        """
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [_index > len(self.input_list) - 1 for _index in self.work_on]

        if any(bool_mask):
            join_ = ", ".join(compress(numeric_list_to_string(self.replace_with), bool_mask))
            raise eL.IndexOutOfList(f'Index {join_} is out of bound for a list of length {len(self.input_list)}.')

        self.__replace_values()

        return self.input_list

    def at_value(self) -> list:
        """
        Replaces the specified values in the given input list.

        Returns
        -------
        list:
            A list with replaced values.
        """
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [element not in self.input_list for element in self.work_on]

        if any(bool_mask):
            join_ = ", ".join(compress(numeric_list_to_string(self.work_on), bool_mask))
            raise eL.GotAnUnknownValue(f'The value {join_} given in old_element does not exist in the input_list.')

        index = [self.input_list.index(element) for element in self.work_on]

        self.__replace_values(primary_list=index)

        return self.input_list
