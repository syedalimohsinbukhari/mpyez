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

    def __init__(self, input_dictionary):
        self.inp_dict = input_dictionary

    def __get_max_width(self):
        _width = max([len(str_)
                      for str_ in [str(value)
                                   for value in self.inp_dict.values()]])

        if _width > 71:
            return _width + 1 if _width % 2 == 0 else +_width
        else:
            return 71

    def __str__(self):
        max_ = self.__get_max_width()

        width = max_ - 1
        width /= 2
        width -= 1
        width = int(width)

        pline = '-' * max_ + '\n'

        out = pline
        out += '|' + 'dict_key'.center(width) + '|' + 'dict_value'.center(width) + '|\n'
        out += pline
        out += '\n'.join(['|' + f'{k}'.center(width) + '|' + f'{v}'.center(width) + '|'
                          for k, v in self.inp_dict.items()]) + '\n'
        out += pline

        return out
