"""Created on Jul 23 04:26:54 2022."""


class Sort_:

    def __init__(self, input_dictionary, sort_by='values'):
        self.inp_dict = input_dictionary
        self.sort_ = sort_by

    def __sorter(self, ind, reverse):
        # taken from https://stackoverflow.com/a/613218/3212945
        return dict(sorted(self.inp_dict.items(), key=lambda x: x[ind], reverse=reverse))

    def get(self, reverse=False):
        return self.__sorter(1 if self.sort_ == 'values' else 0, reverse=reverse)
