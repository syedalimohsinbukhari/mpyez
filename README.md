# `mpyez`

Common use utilities for python done easy.

![GitHub-licence](https://img.shields.io/github/license/syedalimohsinbukhari/mpyez?style=for-the-badge&color=blue)
![GitHub top language](https://img.shields.io/github/languages/top/syedalimohsinbukhari/mpyez?color=green&style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/syedalimohsinbukhari/mpyez?style=for-the-badge)
![Github Issues](https://img.shields.io/github/issues/syedalimohsinbukhari/mpyez?color=red&style=for-the-badge)
![GitHub PRs](https://img.shields.io/github/issues-pr/syedalimohsinbukhari/mpyez?color=maroon&style=for-the-badge)

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

to a 1D list, with `mpyez` you can do it using `nested_list_to_list` function in `ez_list` module (see, Current
implementations for details).

`>>> nested_list_to_list(my_nested_list)`

`>>> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]`

## Modules

### Current Implementations

---

1. `os_`
   1. `ListOfFilesFromExtensions`: To pick files of specific extensions.
   2. `ListOfFilesFromNames`: To pick files matching a specific name pattern.
   3. `move_directory_contents`: To move directory contents to a new location.

2. `list_`
   1. `difference_between_lists`: To get the difference between two lists.
   2. `equal_lists`: To check if two lists are equal.
   3. `get_object_count`: To get an object count from the list.
   4. `index`: To get the index of an element in the list.
   5. `is_contained`: To check if a list is contained within another list.
   6. `join_lists`: To join multiple lists into a single one.
   7. `list_to_nested_list`: To convert a list to a nested list.
   8. `move_element_in_list`: To move a list element to a new position.
   9. `nested_list_to_list`: To convert a nested list to a flat list.
   10. `remove_`: To remove a value from a list.
   11. `replace_at_index`: To replace values at a specific index in the list.
   12. `replace_with_value`: To replace values with a given value in the list.
   13. `sort_`: To sort a list.
   14. `string_list_to_numeric`: To convert string values in a list to numeric.

3. `read_files`
   1. `read_txt_file`: To read an entire text file.
   2. `get_lines_from_txt_file`: To read specific lines from a text file.

4. `dict_`
   1. `get_key_index`: To get the index of a key in a dictionary.
   2. `merge_dictionaries`: To merge dictionaries.
   3. `pretty_print`: To print a dictionary in a readable format.
   4. `sort_dictionary`: To sort a dictionary.

5. `array_`
   1. `moving_average`: To calculate the moving average for an array.
   2. `reshape_with_padding`: To reshape an array with padding.
   3. `transpose1d`: To transpose a 1D array.

6. `plotting_`
   1. `plot_two_column_file`: To plot data from a two-column file.
   2. `plot_xy`: To plot x vs. y data.
   3. `plot_with_dual_axes`: To plot with dual axes for two datasets.

---

### Future Implementations

1. `read_files`
   1. Implementation of reading other file formats, especially `.csv`.
   2. Whole file reading using generators to reduce memory issues.

2. `dict_`
   1. Additional dictionary manipulation methods such as updating, retrieval, and comparisons.