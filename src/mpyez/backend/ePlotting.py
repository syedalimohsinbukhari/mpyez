"""Created on Oct 21 00:12:02 2024"""

from matplotlib import pyplot as plt

# Access the default color cycle
rc_color = plt.rcParams['axes.prop_cycle'].by_key()['color']


class PlotParams:
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
                 size=None, cmap=None, face_color=None):

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


class DoubleLinePlot(PlotParams):
    """
    Class for double-line plot parameters.

    Parameters
    ----------
    All parameters are inherited from `PlotParams`.
    """

    def __init__(self,
                 line_style=None, line_width=None,
                 color=None, alpha=None,
                 marker=None, marker_size=None,
                 marker_edge_color=None, marker_face_color=None, marker_edge_width=None):
        super().__init__(line_style, line_width, color, alpha, marker, marker_size,
                         marker_edge_color, marker_face_color, marker_edge_width)

        if self.color is None:
            self.color = rc_color

    def _all_parameters(self):
        return [self.line_style, self.line_width,
                self.color, self.alpha,
                self.marker, self.marker_size,
                self.marker_edge_color, self.marker_face_color, self.marker_edge_width]

    def _all_labels(self):
        return ['ls', 'lw', 'color', 'alpha',
                'marker', 'ms', 'mec', 'mfc', 'mew']


class DoubleScatterPlot(PlotParams):
    """
    Class for double-scatter plot parameters.

    Parameters
    ----------
    All parameters are inherited from `PlotParams`.
    """

    def __init__(self, size=None, color=None, marker=None, cmap=None, alpha=None, face_color=None):
        super().__init__(color=color, alpha=alpha, marker=marker, size=size, cmap=cmap, face_color=face_color)

        if self.color is None:
            self.color = rc_color

    def _all_parameters(self):
        return [self.size, self.color, self.marker, self.cmap, self.alpha, self.face_color]

    def _all_labels(self):
        return ['s', 'c', 'marker', 'cmap', 'alpha', 'fc']
