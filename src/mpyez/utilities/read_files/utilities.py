"""Created on Jul 23 18:38:52 2022."""

from . import errors as _errors


def check_for_errors(open_file, lines_to_read):
    if all([x >= 0 for x in lines_to_read]):
        if max(lines_to_read) > len(open_file) - 1:
            err = True
        else:
            err = False
    elif any([x < 0 for x in lines_to_read]):
        if abs(min(lines_to_read)) > len(open_file):
            err = True
        else:
            err = False
            for x in [x < 0 for x in lines_to_read]:
                if x:
                    lines_to_read[x] += len(open_file)
    else:
        err = False
    if err:
        raise _errors.LineNumberOutOfBounds('The line number specified is outside the line numbers '
                                            'of the file.')
