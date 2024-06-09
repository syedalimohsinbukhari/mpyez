"""Created on Jul 20 21:45:16 2022."""

from . import errors as _errors


def equalizing_list_length(primary_list, secondary_list, names):
    primary_len = len(primary_list)
    secondary_len = len(secondary_list)

    if secondary_len > primary_len:
        raise _errors.UnequalElements(f'The number of elements in the {names[0]} list is greater than that of '
                                      f'{names[1]}. Cannot perform replacement in this case.')
    elif secondary_len < primary_len:
        secondary_list += secondary_list[:primary_len - secondary_len]

    return secondary_list


def replace_at_index(input_list, index, value, new_list=False):
    index, value = map(lambda x: [x] if not isinstance(x, list) else x, (index, value))
    value += value[:len(index) - len(value)]

    for i, v in zip(index, value):
        if i > len(input_list) - 1:
            raise _errors.IndexOutOfList(f'Index {i} is out of bound for a list of length {len(input_list)}.')

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
            raise _errors.GotAnUnknownValue(f'The value {old} given in old_element does not exist in the input_list.')
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
