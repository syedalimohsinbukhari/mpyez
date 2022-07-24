"""
Created on Jul 18 23:26:06 2022
"""

try:
    from . import ez_dict, ez_list, ez_misc, ez_os, ez_read_files
except ImportError:
    import ez_dict
    import ez_list
    import ez_misc
    import ez_os
    import ez_read_files
