"""Created on Aug 17 15:43:42 2022."""

from mpyez import list_

# a = {1: 2, 3: 4, 2: 3, 6: 7}
#
# print(dict_.pretty_print(a))
# print(dict_.get_key_index(a, 3))

a = [1, 2, 3, 4, 5, 6, [1, 5]]
print(list_.index_(a, [1, 5], True))
