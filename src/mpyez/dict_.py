"""Created on Jul 23 04:26:54 2022."""

from typing import Any, Dict

from .utilities.dict_ import utilities


def sort_dictionary(input_dictionary, sort_by='values', sort_reverse=False):
    def get_key(x):
        return x[1] if sort_by == 'values' else x[0]

    return dict(sorted(input_dictionary.items(), key=get_key, reverse=sort_reverse))


def merge_dictionaries(*dicts: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merge multiple dictionaries into a single dictionary.

    Parameters
    ----------
    dicts : Dict[str, Any]
        The dictionaries to be merged.

    Returns
    -------
    Dict[str, Any]
        The merged dictionary.
    """
    merged_dict = {}

    for dict_ in dicts:
        for key, value in dict_.items():
            if key in merged_dict:
                if isinstance(merged_dict[key], list) and isinstance(value, list):
                    merged_dict[key].extend(value)
                else:
                    merged_dict[key] = [merged_dict[key], value]
            else:
                merged_dict[key] = value

    return merged_dict


def pretty_print(input_dictionary):
    return utilities.PrettyPrint(input_dictionary)


def get_key_index(input_dictionary: dict, key: object) -> int:
    """
    Find the index of a key in a dictionary.

    Parameters
    ----------
    input_dictionary : dict
        The dictionary to search.
    key : object
        The key to find.

    Returns
    -------
    int
        The index of the key in the dictionary.

    Examples
    --------
    >>> inp_dictionary = {'a': 1, 'b': 2, 'c': 3}
    >>> key_to_find = 'b'
    >>> get_key_index(inp_dictionary, key_to_find)
    1
    """
    keys = list(input_dictionary.keys())
    return keys.index(key)
