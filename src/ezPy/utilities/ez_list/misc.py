"""
Created on Jul 20 21:45:16 2022
"""
import copy
from itertools import compress

from src.ezPy.utilities.ez_list import errors


def convert_inputs_to_lists(input1, input2):
    if not isinstance(input1, list):
        input1 = [input1]

    if not isinstance(input2, list):
        input2 = [input2]

    return input1, input2


def equalizing_list_length(primary_list, secondary_list, names):
    if len(secondary_list) > len(primary_list):
        raise errors.UnequalElements(f'The number of elements in the {names[0]} list is greater '
                                     f'than that of {names[1]}. Cannot perform replacement in '
                                     f'this case.')
    elif len(secondary_list) < len(primary_list):
        diff = len(primary_list) - len(secondary_list)
        secondary_list = secondary_list * (diff + 1)
    else:
        secondary_list = secondary_list

    return secondary_list


def replace_at_index(input_list, index, value, new_list=False):
    index, value = convert_inputs_to_lists(index, value)

    value = equalizing_list_length(primary_list=index,
                                   secondary_list=value,
                                   names=['index', 'value'])

    bool_mask = [_index > len(input_list) - 1 for _index in index]

    if True in bool_mask:
        join_ = ", ".join(compress(map(str, index), bool_mask))
        raise errors.IndexOutOfList(f'Index {join_} is out of bound for a list of length '
                                    f'{len(input_list)}.')

    if new_list:
        input_list = copy.deepcopy(input_list)

    for index_, value_ in zip(index, value):
        input_list[index_] = value_

    return input_list


def replace_element(input_list, old_element, new_element, new_list=False):
    old_element, new_element = convert_inputs_to_lists(old_element, new_element)

    bool_mask = [x not in input_list for x in old_element]

    if True in bool_mask:
        join_ = ", ".join(compress(map(str, old_element), bool_mask))
        raise errors.GotAnUnknownValue(f'The value {join_} given in old_element does not exist in '
                                       f'the input_list.')

    new_element = equalizing_list_length(primary_list=old_element,
                                         secondary_list=new_element,
                                         names=['old_elements', 'new_elements'])

    if new_list:
        input_list = copy.deepcopy(input_list)

    index = [input_list.index(element) for element in old_element]

    return replace_at_index(input_list, index, new_element)
