"""Created on Jul 20 12:21:33 2022."""


class EzListErrs(Exception):
    pass


class AlphabetFound(EzListErrs):
    pass


class IndexOutOfList(EzListErrs):
    pass


class UnequalElements(EzListErrs):
    pass


class GotAnUnknownValue(EzListErrs):
    pass


class ChildListLengthError(EzListErrs):
    pass


class StringNotPassed(EzListErrs):
    pass


class InvalidInputParameter(EzListErrs):
    pass
