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


class PrettyPrint:
    def __init__(self, input_dictionary: dict):
        self.inp_dict = input_dictionary

    def __get_max_width(self):
        value_widths = [len(str(value)) for value in self.inp_dict.values()]
        max_width = max(value_widths)
        return max(max_width + 1, 71) if max_width % 2 == 0 else max(max_width, 71)

    def __str__(self):
        max_width = self.__get_max_width()

        width = (max_width - 1) // 2 - 1
        pline = '-' * max_width + '\n'

        out = pline
        out += f"|{'dict_key'.center(width)}|{'dict_value'.center(width)}|\n"
        out += pline
        out += '\n'.join([f"|{k.center(width)}|{v.center(width)}|" for k, v in self.inp_dict.items()]) + '\n'
        out += pline

        return out
