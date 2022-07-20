"""
Created on Jul 20 11:54:27 2022
"""

import itertools

try:
    from .utilities.ez_list import errors as errors_
except ImportError:
    import utilities.ez_list.errors as errors_


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
        raise errors_.AlphabetFound(f'Alphabet found in the list passed, '
                                    f'{", ".join(itertools.compress(str_list, mask_))} cannot '
                                    f'be processed.')

    return ret_


def nested_list_to_list(nested_list):
    return list(itertools.chain.from_iterable(nested_list))


def list_to_nested_list(input_list, n_elements):
    return [input_list[i:i + n_elements] for i in range(0, len(input_list), n_elements)]


def join_lists(lists, get_unique=False, sort=False):
    _temp = []

    for _list in lists:
        _temp.extend(_list)

    # taken from https://stackoverflow.com/a/58666031/3212945
    if get_unique:
        unique_ = set()
        _temp = [x for x in _temp if not (x in unique_ or unique_.add(x))]

    if sort:
        _temp = sorted(_temp)

    return _temp
