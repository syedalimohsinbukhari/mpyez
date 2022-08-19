"""Created on Aug 17 23:51:58 2022."""


def change_value_to_list(input_dictionary):
    for key, value in input_dictionary.items():
        if not isinstance(value, list):
            input_dictionary[key] = [input_dictionary[key]]

    return input_dictionary


def change_list_to_values(input_dictionary):
    for key, value in input_dictionary.items():
        if len(input_dictionary[key]) == 1:
            input_dictionary[key] = input_dictionary[key][0]

    return input_dictionary
