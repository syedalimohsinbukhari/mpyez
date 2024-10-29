"""Created on Oct 21 00:12:02 2024"""


class PlotError(Exception):
    """Basic PlotError class"""
    pass


class NoXYLabels(PlotError):
    """Custom class for missing x or y labels"""
    pass


class OrientationError(PlotError):
    """Custom class for wrong orientation"""
    pass
