"""
Created on Jul 18 23:26:06 2022
"""

try:
    from . import ez_dict
    from . import ez_list
    from . import ez_misc
    from . import ez_os
    from . import ez_read_files
except ImportError:
    import ez_dict
    import ez_list
    import ez_misc
    import ez_os
    import ez_read_files
