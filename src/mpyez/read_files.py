"""Created on Jul 23 16:56:48 2022."""

from src.mpyez.utilities.read_files.utilities import check_for_errors


def read_txt_file(file_to_read) -> list:
    open_file = [value for _, value in enumerate(open(file=file_to_read, mode='r'))]

    return [line.strip('\n') for line in open_file]


def get_lines_from_txt_file(file_to_read, lines_to_read) -> list:
    out = read_txt_file(file_to_read=file_to_read)

    if not isinstance(lines_to_read, list):
        lines_to_read = [lines_to_read]

    check_for_errors(open_file=out, lines_to_read=lines_to_read)

    # taken from https://stackoverflow.com/a/2082131/3212945
    return [value for index, value in enumerate(out) if index in set(lines_to_read)]
