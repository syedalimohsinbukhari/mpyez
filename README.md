# `mpyez`

Common use utilities for python done easy.

![GitHub](https://img.shields.io/github/license/syedalimohsinbukhari/mpyez?color=blue&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/syedalimohsinbukhari/mpyez?color=green&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/syedalimohsinbukhari/mpyez?style=for-the-badge)

## What is `mpyez`

`mpyez` is a library made specifically to make the daily mundane tasks as easily doable as possible.

* Want to get a list of all python files in your folder? Use `ListOfFilesFromExtensions` class.
* Want to convert a nested list to a 1D list? Use `nested_list_to_list()`.
* Want to convert a simple list to nested list? Use `list_to_nested_list()`.

This library is intended to lower complexity of daily recurring tasks.

## How to install

Use pip: `pip install mpyez`

## Examples

Let's say, you want to convert a nested list

`>>> my_nested_list = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10]]`

to a 1D list, with `mpyez` you can do it using `nested_list_to_list` function in `ez_list` module (see, Current implementations for details).

`>>> nested_list_to_list(my_nested_list)`

`>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

## Modules

### Current implementations

1. `ez_misc`
    1. `is_alphabet` : To check if the input is alphabet or not.
    2. `is_numeric` : To check if the input is numeric or not.
2. `ez_os`
    1. `ListOfFilesFromExtensions` : To pick files of specific extensions
    2. `ListOfFilesFromNames`: To pick files matching a specific name pattern.
3. `ez_list`
    1. `numeric_list_to_string` : To convert a list of numeric values to string.
    2. `string_list_to_numeric` : To convert a list of string number values to numeric.
    3. `nested_list_to_list` : To convert a nested list to 1D list.
    4. `list_to_nested_list` : To convert a simple 1D list to a nested list.
    5. `join_lists` : To join multiple lists into a single one
    6. `Replace` : To replace values in a list, either by given value or by the index.
    7. `is_contained` : To check if a given list is contained within another list.
    8. `get_object_count`: To get an object count from the list. Has an added capability of returning sorted list of objects or top N objects.
    9. `sort_`: To sort a list. Can also return the sort indices.
    10. `remove_`: To remove a value from a given list. Can also remove `tuple`, `str`, or a nested `list`.
    11. `move_element_in_list`: To move a given element present in the list to a new location within the list.
4. `ez_read_files`
    1. `read_text_file_in_a_list`: Reads an entire `txt` file.
    2. `read_specific_lines_from_a_file`: Reads specific lines (index based) from a given `txt` file.

### Future implementations

1. `ez_read_files`
    1. Whole files using generator to reduce memory issues,
    2. Implementation of reading other files, especially `.csv`.
2. `ez_dict`
    1. For handling dictionary manipulations methods easily. For example,
        1. updating dictionaries,
        2. index retrieval, and/or
        3. dictionary comparisons.
3. And more

### Documentation: IN PROGRESS
