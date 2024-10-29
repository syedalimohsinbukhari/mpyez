"""Created on Oct 21 00:12:02 2024"""

__all__ = ['LinePlot', 'ScatterPlot', 'SubPlots']

from matplotlib import rcParams

from .uPlotting import _PlotParams

rc_color = rcParams['axes.prop_cycle'].by_key()['color'] * 10


class LinePlot(_PlotParams):
    """
    Class for double-line plot parameters.

    Parameters
    ----------
    All parameters are inherited from `_PlotParams`.
    """

    def __init__(self,
                 line_style=None, line_width=None,
                 color=None, alpha=None,
                 marker=None, marker_size=None,
                 marker_edge_color=None, marker_face_color=None, marker_edge_width=None, _fixed: int = 0):
        super().__init__(line_style=line_style, line_width=line_width, color=color, alpha=alpha, marker=marker, marker_size=marker_size,
                         marker_edge_color=marker_edge_color, marker_face_color=marker_face_color, marker_edge_width=marker_edge_width)

        if self.color is None:
            self.color = rc_color

    def _all_parameters(self):
        return [self.line_style, self.line_width,
                self.color, self.alpha,
                self.marker, self.marker_size,
                self.marker_edge_color, self.marker_face_color, self.marker_edge_width]

    def _all_labels(self):
        return ['ls', 'lw', 'color', 'alpha', 'marker', 'ms', 'mec', 'mfc', 'mew']


class ScatterPlot(_PlotParams):
    """
    Class for double-scatter plot parameters.

    Parameters
    ----------
    All parameters are inherited from `_PlotParams`.
    """

    def __init__(self, size=None, color=None, marker=None, cmap=None, alpha=None, face_color=None):
        super().__init__(color=color, alpha=alpha, marker=marker, size=size, cmap=cmap, face_color=face_color)

        if self.color is None:
            self.color = rc_color

    def _all_parameters(self):
        return [self.size, self.color, self.marker, self.cmap, self.alpha, self.face_color]

    def _all_labels(self):
        return ['s', 'c', 'marker', 'cmap', 'alpha', 'fc']


class SubPlots(_PlotParams):

    def __init__(self, share_x=None, share_y=None, fig_size=None):
        super().__init__(share_x=share_x, share_y=share_y, subplot_fig_size=fig_size)

    def _all_labels(self):
        return ['sharex', 'sharey', 'figsize']

    def _all_parameters(self):
        return [self.share_x, self.share_y, self.fig_size]
