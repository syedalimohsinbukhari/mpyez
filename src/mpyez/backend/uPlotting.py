"""Created on Oct 29 09:33:06 2024"""

__all__ = ['LinePlot', 'ScatterPlot', 'SubPlots', 'label_handler', 'plot_or_scatter', 'plot_dictionary_handler']

import warnings
from typing import List, Optional, Tuple, Union

from matplotlib import pyplot as plt, rcParams

from .ePlotting import NoXYLabels

rc_color = rcParams['axes.prop_cycle'].by_key()['color'] * 10


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


def label_handler(x_labels: Optional[List[str]], y_labels: Optional[List[str]],
                  n_rows: int, n_cols: int,
                  auto_label: bool) -> Tuple[List[str], List[str]]:
    """
    Handles the generation or validation of x and y labels for a subplot configuration.

    Parameters
    ----------
    x_labels : list of str or None
        The labels for the x-axis. If `None`, labels may be auto-generated based on `auto_label`.
    y_labels : list of str or None
        The labels for the y-axis. If `None`, labels may be auto-generated based on `auto_label`.
    n_rows : int
        Number of rows in the subplot grid.
    n_cols : int
        Number of columns in the subplot grid.
    auto_label : bool
        If `True`, generates x and y labels automatically when not provided.

    Returns
    -------
    Tuple[List[str], List[str]]
        The x and y labels for the subplot grid.

    Raises
    ------
    NoXYLabels
        If both `x_labels` and `y_labels` are `None` and `auto_label` is `False`.

    Warnings
    --------
    UserWarning
        If one of `x_labels` or `y_labels` is missing when `auto_label` is enabled, or if
        there is a mismatch in the number of provided labels.

    """
    if not auto_label and (x_labels is None or y_labels is None):
        raise NoXYLabels("Both x_labels and y_labels are required without the auto_label parameter.")

    elif auto_label and (x_labels is None or y_labels is None):
        if x_labels is None and y_labels is None:
            pass
        else:
            if x_labels is None:
                warnings.warn("y_labels given but x_labels is missing, applying auto-labeling...", UserWarning)
            if y_labels is None:
                warnings.warn("x_labels given but y_labels is missing, applying auto-labeling...", UserWarning)

    if auto_label:
        if x_labels and y_labels:
            start = "auto_label selected with x_labels and y_labels provided"
            if len(x_labels) != n_rows * n_cols or len(y_labels) != n_rows * n_cols:
                warnings.warn(f"{start}, mismatch found, using auto-generated labels...", UserWarning)
                x_labels = [fr'X$_{i + 1}$' for i in range(n_cols * n_rows)]
                y_labels = [fr'Y$_{i + 1}$' for i in range(n_cols * n_rows)]
            else:
                print(f"{start}, using user-provided labels...")
        else:
            x_labels = [fr'X$_{i + 1}$' for i in range(n_cols * n_rows)]
            y_labels = [fr'Y$_{i + 1}$' for i in range(n_cols * n_rows)]

    return x_labels, y_labels


def plot_or_scatter(axes: plt.axis, scatter: bool):
    """
    Returns the plot or scatter method based on the specified plot type.

    Parameters
    ----------
    axes : plt.axis
        The matplotlib axis on which to apply the plot or scatter method.
    scatter : bool
        If True, returns the scatter method; otherwise, returns the plot method.

    Returns
    -------
    function
        The matplotlib plotting method (`axes.scatter` if scatter is True, otherwise `axes.plot`).
    """
    return axes.scatter if scatter else axes.plot


def plot_dictionary_handler(plot_dictionary: Union[LinePlot, ScatterPlot]):
    """
    Handles plot dictionary configuration, retrieving items from the specified plot dictionary.

    If no dictionary is provided, returns items from a default LinePlot instance.

    Parameters
    ----------
    plot_dictionary : Union[LinePlot, ScatterPlot]
        The plot dictionary to retrieve items from. If None, defaults to a LinePlot instance.

    Returns
    -------
    Iterable
        An iterable of items (key-value pairs) from the specified or default plot dictionary.
    """
    return plot_dictionary.get().items() if plot_dictionary else LinePlot().get().items()
