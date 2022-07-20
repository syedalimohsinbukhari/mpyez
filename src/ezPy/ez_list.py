"""
Created on Jul 20 11:54:27 2022
"""

import copy
from itertools import chain, compress

try:
    from .utilities.ez_list import errors, misc
except ImportError:
    from utilities.ez_list import errors, misc


def is_alphabet(input_):
    try:
        if int(input_):
            return False
    except ValueError:
        return True


def is_numeric(input_):
    if isinstance(input_, int or float):
        return True
    else:
        return False


def numeric_list_to_string(num_list):
    return list(map(str, num_list))


def string_list_to_numeric(str_list):
    mask_ = [is_alphabet(x) for x in str_list]

    if False not in mask_:
        ret_ = list(map(str, str_list))
    else:
        raise errors.AlphabetFound(f'Alphabet found in the list passed, '
                                   f'{", ".join(compress(str_list, mask_))} cannot be processed.')

    return ret_


def nested_list_to_list(nested_list):
    return list(chain.from_iterable(nested_list))


def list_to_nested_list(input_list, n_elements):
    return [input_list[i:i + n_elements] for i in range(0, len(input_list), n_elements)]


def join_lists(lists, get_unique=False, sort=False):
    _temp = []

    for _list in lists:
        _temp.extend(_list)

    mask1 = [i for i, v in enumerate(_temp) if type(v) == list]

    if mask1:
        for x in mask1:
            _temp[x] = tuple(_temp[x])

    # taken from https://stackoverflow.com/a/58666031/3212945
    if get_unique:
        unique_ = set()
        _temp = [x for x in _temp if not (x in unique_ or unique_.add(x))]

    if sort:
        try:
            _temp = sorted(_temp)
        except TypeError:
            n_types = list(set([type(x) for x in _temp]))
            mask2 = [[index for index, value in enumerate(_temp) if type(value) == types_] for
                     types_ in n_types]

            _temp = [sorted(x) for x in [[_temp[y] for y in z] for z in mask2]]
            _temp = nested_list_to_list(_temp)

    return _temp


class Replace:

    def __init__(self, input_list, work_on, replace_with, by='index', new_list=False):
        if new_list:
            self.input_list = copy.deepcopy(input_list)
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

    def __equalizing_list_length(self):
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

    def __replace_values(self, primary_list=None):
        primary_list = self.work_on if primary_list is None else primary_list

        for index_, value_ in zip(primary_list, self.replace_with):
            self.input_list[index_] = value_

    def at_index(self):
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [_index > len(self.input_list) - 1 for _index in self.work_on]

        if True in bool_mask:
            join_ = ", ".join(compress(numeric_list_to_string(self.replace_with), bool_mask))
            raise errors.IndexOutOfList(f'Index {join_} is out of bound for a list of length '
                                        f'{len(self.input_list)}.')

        self.__replace_values()

        return self.input_list

    def at_value(self):
        self.work_on, self.replace_with = self.__convert_inputs_to_lists()
        self.replace_with = self.__equalizing_list_length()

        bool_mask = [x not in self.input_list for x in self.work_on]

        if True in bool_mask:
            join_ = ", ".join(compress(numeric_list_to_string(self.work_on), bool_mask))
            raise errors.GotAnUnknownValue(f'The value {join_} given in old_element does not exist '
                                           f'in the input_list.')

        index = [self.input_list.index(element) for element in self.work_on]

        self.__replace_values(primary_list=index)

        return self.input_list
