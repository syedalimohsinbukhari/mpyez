# `ezPy`

Common use utilities for python done easy.

![GitHub](https://img.shields.io/github/license/syedalimohsinbukhari/ezPy?color=blue&style=for-the-badge)
![GitHub top language](https://img.shields.io/github/languages/top/syedalimohsinbukhari/ezPy?color=green&style=for-the-badge)
![Lines of code](https://img.shields.io/tokei/lines/github/syedalimohsinbukhari/ezPy?style=for-the-badge)
![GitHub repo size](https://img.shields.io/github/repo-size/syedalimohsinbukhari/ezPy?style=for-the-badge)
![GitHub contributors](https://img.shields.io/github/contributors/syedalimohsinbukhari/ezPy?style=for-the-badge)

## What is `ezPy`

`ezPy` is a library made specifically to make the daily mundane tasks as easily doable as possible.

* Want to get a list of all python files in your folder? Use `ListOfFilesFromExtensions` class.
* Want to convert a nested list to a 1D list? Use `nested_list_to_list()`.
* Want to convert a simple list to nested list? Use `list_to_nested_list()`.

This library is intended to lower complexity of daily recurring tasks.

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
   6. `is_contained` : To check if a given list is contained within another list.
   7. `Replace` : To replace values in a list, either by given value or by the index.

### Future implementations

1. `ez_file_handling`
   1. For reading text files in python,
      1. whole files,
      2. lazy loading, or
      3. chunks of files only.
   2. Implementation of reading other files will also be included
2. `ez_dict`
   1. For handling dictionary manipulations methods easily. For example,
      1. updating dictionaries,
      2. index retrieval, and/or
      3. dictionary comparisons.
3. And more
