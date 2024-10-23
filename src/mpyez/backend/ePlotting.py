"""Created on Oct 21 00:12:02 2024"""

__all__ = ['LinePlot', 'ScatterPlot', 'SubPlots']

default1 = '#1f77b4'
default2 = '#ff7f0e'


class _PlotParams:
    """
    Base class for handling common plot parameters.

    Parameters
    ----------
    line_style : list(str), optional
        Line style for the plot. Default is None.
    line_width : list(float), optional
        Width of the lines. Default is None.
    color : list(str), optional
        List or tuple containing two colors. Defaults to first two colors in matplotlib color cycle.
    alpha : list(float), optional
        Opacity of the plot elements. Default is None.
    marker : list(str), optional
        Marker style for the plot. Default is None.
    marker_size : list(float), optional
        Size of the markers. Default is None.
    marker_edge_color : list(str), optional
        Color of the marker edges. Default is None.
    marker_face_color : list(str), optional
        Color of the marker faces. Default is None.
    marker_edge_width : list(float), optional
        Width of the marker edges. Default is None.
    size : list(float), optional
        Size of the markers for scatter plots. Must be a list or tuple with exactly two elements. Default is None.
    cmap : list(Colormap), optional
        Colormap used for scatter plots. Default is None.
    face_color : list(str), optional
        Color of the marker faces in scatter plots. Default is None.
    """

    def __init__(self,
                 line_style=None, line_width=None,
                 color=None, alpha=None,
                 marker=None, marker_size=None,
                 marker_edge_color=None, marker_face_color=None, marker_edge_width=None,
                 size=None, cmap=None, face_color=None,
                 share_x=None, share_y=None, subplot_fig_size=None):

        self.line_style = line_style
        self.line_width = line_width
        self.color = color
        self.alpha = alpha
        self.marker = marker
        self.marker_size = marker_size
        self.marker_edge_color = marker_edge_color
        self.marker_face_color = marker_face_color
        self.marker_edge_width = marker_edge_width

        # Additional keywords for scatter plot
        self.size = size
        self.cmap = cmap
        self.face_color = face_color

        # Additional keywords for subplots
        self.share_x = share_x
        self.share_y = share_y
        self.fig_size = subplot_fig_size

    def get(self):
        """
        Get the dictionary of plot parameters, excluding None values.

        Returns
        -------
        dict
            Dictionary containing non-None parameters for the plot.
        """
        param_dict = {}

        for param, label in zip(self._all_parameters(), self._all_labels()):
            if param is not None:
                param_dict[f'{label}'] = param

        return param_dict

    def _all_parameters(self):
        raise NotImplementedError("This method should be implemented by subclasses.")

    def _all_labels(self):
        raise NotImplementedError("This method should be implemented by subclasses.")


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
                 marker_edge_color=None, marker_face_color=None, marker_edge_width=None):
        super().__init__(line_style=line_style, line_width=line_width, color=color, alpha=alpha, marker=marker, marker_size=marker_size,
                         marker_edge_color=marker_edge_color, marker_face_color=marker_face_color, marker_edge_width=marker_edge_width)

        if self.color is None:
            self.color = [default1, default2]

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
            self.color = [default1, default2]

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