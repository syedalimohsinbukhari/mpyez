"""Created on Jul 20 21:45:16 2022."""

from copy import deepcopy
from itertools import compress
from typing import List, Union

from . import eList as eL
from .eList import GotAnUnknownValue, IndexOutOfList, UnequalElements


def equalizing_list_length(primary_list, secondary_list, names):
    primary_len = len(primary_list)
    secondary_len = len(secondary_list)

    if secondary_len > primary_len:
        raise UnequalElements(f'The number of elements in the {names[0]} list is greater than that of {names[1]}. '
                              f'Cannot perform replacement in this case.')
    elif secondary_len < primary_len:
        secondary_list += secondary_list[:primary_len - secondary_len]

    return secondary_list


def replace_at_index(input_list, index, value, new_list=False):
    index, value = map(lambda x: [x] if not isinstance(x, list) else x, (index, value))
    value += value[:len(index) - len(value)]

    for i, v in zip(index, value):
        if i > len(input_list) - 1:
            raise IndexOutOfList(f'Index {i} is out of bound for a list of length {len(input_list)}.')

    if new_list:
        input_list = input_list[:]

    for i, v in zip(index, value):
        input_list[i] = v

    return input_list


def replace_element(input_list, old_element, new_element, new_list=False):
    old_element, new_element = map(lambda x: [x] if not isinstance(x, list) else x, (old_element, new_element))
    new_element += new_element[:len(old_element) - len(new_element)]

    index = []
    for i, old in enumerate(old_element):
        if old not in input_list:
            raise GotAnUnknownValue(f'The value {old} given in old_element does not exist in the input_list.')
        index.append(input_list.index(old))

    if new_list:
        input_list = input_list[:]

    for i, new in zip(index, new_element):
        input_list[i] = new

    return input_list


class CountObjectsInList:

    def __init__(self, counter_dict):
        self.counter_dict = counter_dict
        self.__counter_dict = sorted(self.counter_dict.items(), key=lambda x: x[1], reverse=True)

        self.counter = 0

    def __str__(self):
        out = '-' * 50 + '\n'
        out += f'|{"items":^30}|{"counts":^17}|\n'
        out += '-' * 50 + '\n'
        out += '\n'.join([f'|{key:^30}|{value:^17}|'
                          if not isinstance(key, str)
                          else f"|\'{key}\':^30|{value:^17}|"
                          for key, value in self.counter_dict.items()]) + '\n'
        out += '-' * 50 + '\n'
        return out

    def __getitem__(self, item):
        _get = self.__counter_dict[item]
        try:
            return CountObjectsInList({element[0]: element[1] for element in _get})
        except TypeError:
            return CountObjectsInList({_get[0]: _get[1]})


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
