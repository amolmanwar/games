"""An unit testing module to test snake and ladder game """

import warnings


def warn(*args, **kwargs):
    """Supressing warnings """
    _ = args
    _ = kwargs

warnings.warn = warn
