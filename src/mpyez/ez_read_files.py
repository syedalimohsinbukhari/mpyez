"""Created on Jul 23 16:56:48 2022."""

try:
    from .utilities.ez_read_files import errors, misc
except ImportError:
    from utilities.ez_read_files import errors, misc


def read_text_file_in_a_list(file_to_read):
    open_file = [value.readlines() for _, value in enumerate(open(file=file_to_read, mode='r'))]

    return [line.split('\n')[0] for line in open_file[0]]


def read_specific_lines_from_a_text_file(file_to_read, lines_to_read):
    out = read_text_file_in_a_list(file_to_read=file_to_read)

    if not isinstance(lines_to_read, list):
        lines_to_read = [lines_to_read]

    misc.check_for_errors(open_file=out, lines_to_read=lines_to_read)

    # taken from https://stackoverflow.com/a/2082131/3212945
    return [value.split('\n')[0] for index, value in enumerate(open(file=file_to_read, mode='r')) if
            index in set(lines_to_read)]
