"""Created on Jul 23 04:26:54 2022."""

import copy

from .list_ import index_
from .utilities.dict_ import utilities


def sort_dictionary(input_dictionary, sort_by='values', sort_reverse=False):
    def __sorter(index, reverse):
        # taken from https://stackoverflow.com/a/613218/3212945
        return dict(sorted(input_dictionary.items(), key=lambda x: x[index], reverse=reverse))

    return __sorter(index=1 if sort_by == 'values' else 0, reverse=sort_reverse)


def merge_dictionaries(input_dictionaries, keep_original_dictionaries=True):
    inp_dict = [copy.deepcopy(dict_)
                if keep_original_dictionaries else input_dictionaries
                for dict_ in input_dictionaries]

    [utilities.change_value_to_list(dict_) for dict_ in inp_dict]

    merged_ = {}

    for dict_ in inp_dict:
        for key, value in dict_.items():
            if key not in merged_.keys():
                merged_.update({key: value})
            else:
                merged_[key].extend(value)

    utilities.change_list_to_values(merged_)

    return merged_


def pretty_print(input_dictionary):
    return utilities.PrettyPrint(input_dictionary)


def get_key_index(input_dictionary, key, is_iterator=True):
    return index_(input_list=list(input_dictionary.keys()), iterator=key, is_iterator=is_iterator)
