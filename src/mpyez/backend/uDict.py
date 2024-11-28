"""Created on Aug 17 23:51:58 2022."""

from typing import Any, Dict, List, Union


def change_value_to_list(input_dictionary: Dict[Any, Any]) -> Dict[Any, List[Any]]:
    """
    Converts all non-list values in a dictionary to lists.

    Parameters
    ----------
    input_dictionary : dict
        The dictionary whose values need to be converted to lists.

    Returns
    -------
    dict
        A dictionary where all values are guaranteed to be lists.
    """
    for key, value in input_dictionary.items():
        if not isinstance(value, list):
            input_dictionary[key] = [value]
    return input_dictionary


def change_list_to_values(input_dictionary: Dict[Any, List[Any]]) -> Dict[Any, Union[Any, List[Any]]]:
    """
    Converts single-element lists in a dictionary back to their single values.

    Parameters
    ----------
    input_dictionary : dict
        The dictionary whose single-element list values need to be simplified.

    Returns
    -------
    dict
        A dictionary where single-element lists are replaced by their sole values.
    """
    for key, value in input_dictionary.items():
        if len(value) == 1:
            input_dictionary[key] = value[0]
    return input_dictionary


class PrettyPrint:
    """
    A class for displaying dictionaries in a tabular format.

    Parameters
    ----------
    input_dictionary : dict
        The dictionary to be formatted and displayed.
    column_width : int, optional
        Custom width for table columns (default is dynamically calculated).
    alignment : str, optional
        Alignment for table cells: 'left', 'center', or 'right' (default is 'center').

    Attributes
    ----------
    inp_dict : dict
        The input dictionary stored for formatting and display.
    column_width : int
        Width of each column in the table.
    alignment : str
        Alignment configuration for table cells.
    """

    def __init__(self, input_dictionary: Dict[Any, Any], column_width: int = None, alignment: str = "center"):
        self.inp_dict = input_dictionary
        self.column_width = column_width
        self.alignment = alignment

    def __get_max_width(self) -> int:
        """
        Computes the maximum column width for formatting if not provided.

        Returns
        -------
        int
            The maximum width for the table columns.
        """
        if self.column_width:
            return self.column_width

        value_widths = [len(str(value)) for value in self.inp_dict.values()]
        max_width = max(value_widths)
        return max(max_width + 1, 71) if max_width % 2 == 0 else max(max_width, 71)

    def __align_text(self, text: str, width: int) -> str:
        """
        Aligns text within a given width based on the alignment setting.

        Parameters
        ----------
        text : str
            The text to align.
        width : int
            The width of the column.

        Returns
        -------
        str
            The aligned text.
        """
        if self.alignment == "left":
            return text.ljust(width)
        elif self.alignment == "right":
            return text.rjust(width)
        else:  # Default to center
            return text.center(width)

    def __str__(self) -> str:
        """
        Returns the formatted string representation of the dictionary.

        Returns
        -------
        str
            A tabular representation of the dictionary with enhanced aesthetics.
        """
        max_width = self.__get_max_width()
        column_width = (max_width - 1) // 2 - 1
        separator_line = "+" + "-" * column_width + "+" + "-" * column_width + "+\n"

        header = f"|{self.__align_text('dict_key', column_width)}|{self.__align_text('dict_value', column_width)}|\n"
        rows = '\n'.join([f"|{self.__align_text(str(key), column_width)}|"
                          f"{self.__align_text(str(value), column_width)}|"
                          for key, value in self.inp_dict.items()])

        return separator_line + header + separator_line + rows + '\n' + separator_line
