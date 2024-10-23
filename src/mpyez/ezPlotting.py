"""Created on Jul 23 23:41:18 2024"""

__all__ = ['plot_two_column_file', 'plot_xy', 'plot_with_dual_axes', 'two_subplots']

from typing import List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

from .backend.ePlotting import LinePlot, ScatterPlot, SubPlots

# safeguard
line_plot = "LinePlot"
scatter_plot = "ScatterPlot"
plot_dictionary_type = Optional[Union[LinePlot, ScatterPlot]]
axis_return = Union[List[plt.axis], plt.axis]


# TODO:
#   Can `two_subplots` work  with `plot_with_dual_axes`
#   Have to add axes individual functionality in `plot_with_dual_axes`
#   See if two plots can work with a single specifier of kwargs in plots
#   Get rid of fig_size default values in the functions

def plot_two_column_file(file_name: str, delimiter: str = ',', skip_header: bool = False, auto_label: bool = False,
                         fig_size: Tuple[int, int] = None, is_scatter: bool = False, plot_dictionary: plot_dictionary_type = None,
                         axis: Optional[plt.axis] = None) -> axis_return:
    """
    Reads a two-column file (x, y) and plots the data.

    This function reads a file containing two columns (e.g., x and y values) and plots them
    using either a line plot or scatter plot based on the user's preference.

    Parameters
    ----------
    file_name : str
        The path to the file to be plotted. The file should contain two columns (x and y data).
    delimiter : str, optional
        The delimiter used in the file (default is ',').
    skip_header: bool, optional
        If True, skips the first row in the given data file, otherwise does nothing. Default is False.
    auto_label : bool, optional
        If True, automatically sets the x-axis label, y-axis label, and plot title. Default is False.
    fig_size : tuple of int, optional
        The size of the plot figure, only used if a new plot is created. If None, default matplotlib size will be used.
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot. Default is False.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    data = np.genfromtxt(file_name, delimiter=delimiter, skip_header=skip_header)

    if data.shape[1] != 2:
        raise ValueError("The file must contain exactly two columns of data.")

    x_data, y_data = data.T

    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, auto_label=auto_label, fig_size=fig_size, is_scatter=is_scatter,
                               plot_dictionary=plot_dictionary, axis=axis)


def plot_xy(x_data: np.ndarray, y_data: np.ndarray, auto_label: bool = False, fig_size: Tuple[int, int] = None,
            is_scatter: bool = False, plot_dictionary: plot_dictionary_type = None,
            axis: Optional[plt.axis] = None) -> axis_return:
    """
    Plots x_data against y_data with customizable options.

    This function accepts two arrays of data (x and y) and plots them using either
    a line plot or scatter plot, with options for labels and figure size.

    Parameters
    ----------
    x_data : np.ndarray
        The data for the x-axis.
    y_data : np.ndarray
        The data for the y-axis.
    auto_label : bool, optional
        If True, automatically sets x and y-axis labels and the plot title. Default is False.
    fig_size : tuple of int, optional
        The size of the plot figure. If None, default matplotlib size will be used.
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot. Default is False.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, auto_label=auto_label, fig_size=fig_size, is_scatter=is_scatter,
                               plot_dictionary=plot_dictionary, axis=axis)


def plot_with_dual_axes(x1_data: np.ndarray, y1_data: np.ndarray,
                        x2_data: Optional[np.ndarray] = None, y2_data: Optional[np.ndarray] = None,
                        x1y1_label: str = 'X1 vs Y1', x1y2_label: str = 'X1 vs Y2', x2y1_label: str = 'X2 vs Y1',
                        use_twin_x: bool = False, auto_label: bool = False, fig_size: Tuple[int, int] = None,
                        is_scatter: bool = False, plot_dictionary: plot_dictionary_type = None, axis: Optional[plt.axis] = None) -> axis_return:
    """
    Plots data with options for dual axes (x or y) or single axis.

    Parameters
    ----------
    x1_data : np.ndarray
        Data for the primary x-axis.
    y1_data : np.ndarray
        Data for the primary y-axis.
    x2_data : np.ndarray, optional
        Data for the secondary x-axis (used for dual x-axis plots).
    y2_data : np.ndarray, optional
        Data for the secondary y-axis (used for dual y-axis plots).
    x1y1_label : str, optional
        Label for the plot of X1 vs Y1. Default is 'X1 vs Y1'.
    x1y2_label : str, optional
        Label for the plot of X1 vs Y2 (when using dual Y-axes). Default is 'X1 vs Y2'.
    x2y1_label : str, optional
        Label for the plot of X2 vs Y1 (when using dual X-axes). Default is 'X2 vs Y1'.
    use_twin_x : bool, optional
        If True, creates dual y-axis plot. If False, creates dual x-axis plot. Default is False.
    auto_label : bool, optional
        If True, automatically labels the axes and plot title. Default is False.
    fig_size : Tuple[int, int], optional
        Figure size for the plot. If None, default matplotlib size will be used.
    is_scatter : bool, optional
        If True, creates scatter plot; otherwise, line plot. Default is False.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    [fig, (ax1, ax2)] or [fig, ax1] depending on the presence of dual axes.
    """
    # CHANGELIST:
    #   Works with axis
    #   Works with default fig_size if no figure size is specified
    if use_twin_x and x2_data is not None:
        raise ValueError("Dual Y-axis plot requested but 'x2_data' given.")
    if not use_twin_x and y2_data is not None:
        raise ValueError("Dual X-axis plot requested but 'y2_data' given.")
    if len(x1_data) == 0 or len(y1_data) == 0:
        raise ValueError("Primary x or y data is empty. Please provide valid data.")

    if axis:
        ax1 = axis
    else:
        _, ax1 = plt.subplots(figsize=fig_size if fig_size else rcParams["figure.figsize"])

    def _plot_or_scatter(axes, scatter):
        return axes.scatter if scatter else axes.plot

    plot_items = _plot_dictionary_handler(is_scatter=is_scatter, plot_dictionary=plot_dictionary)

    dict1 = {key: (value[0] if isinstance(value, list) else value) for key, value in plot_items}

    # Check the condition once before creating dict2
    use_secondary_values = x2_data is not None or y2_data is not None or use_twin_x
    dict2 = {key: (value[1] if use_secondary_values else None) for key, value in plot_items}

    _plot_or_scatter(axes=ax1, scatter=is_scatter)(x1_data, y1_data, label=x1y1_label, **dict1)

    ax2 = None

    if auto_label:
        ax1.set_xlabel('X1')
        ax1.set_ylabel('Y1')
        ax1.set_title('Plot')

    if use_twin_x:
        ax2 = ax1.twinx()
        _plot_or_scatter(axes=ax2, scatter=is_scatter)(x1_data, y2_data, label=x1y2_label, **dict2)
        if auto_label:
            ax2.set_ylabel('Y2')

    elif x2_data is not None:
        ax2 = ax1.twiny()
        _plot_or_scatter(axes=ax2, scatter=is_scatter)(x2_data, y1_data, label=x2y1_label, **dict2)
        if auto_label:
            ax2.set_xlabel('X2')

    handles, labels = ax1.get_legend_handles_labels()
    if ax2:
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles += handles2
        labels += labels2

    ax1.legend(handles, labels, loc='best')

    plt.tight_layout()

    return (ax1, ax2) if ax2 else ax1


def _plot_dictionary_handler(is_scatter, plot_dictionary):
    if plot_dictionary:
        plot_items = plot_dictionary.get().items()
    elif is_scatter:
        plot_items = ScatterPlot().get().items()
    else:
        plot_items = LinePlot().get().items()
    return plot_items


def two_subplots(x_data, y_data, x_labels, y_labels, orientation='h', subplot_dictionary=None, plot_dictionary=None, is_scatter: bool = False):
    # CHANGELIST:
    #   Can take two x arguments and two y arguments
    #   added capability for SubPlots dictionary, have to test LinePlot/ScatterPlot dictionaries
    #   X and Y data can be now passed in as lists
    #   for two_subplots, it provides horizontal or vertical orientation because there'll only be two subplots.
    #   Handles not providing a subplot dictionary
    #   Handles not providing a plot dictionary
    #   includes is_scatter option for scatter plotting
    #   can now handle plot dictionary with various parameters, the first parameter is used in both dictionaries if second parameter is not provided.

    if orientation == 'h':
        n_rows, n_cols = 1, 2
    elif orientation == 'v':
        n_rows, n_cols = 2, 1
    else:
        raise ValueError("The orientation must be either \'h\' or \'v\'.")

    fig, axs = plt.subplots(n_rows, n_cols,
                            **subplot_dictionary if subplot_dictionary else SubPlots().get())
    axs = axs.flatten()

    plot_items = _plot_dictionary_handler(is_scatter=is_scatter, plot_dictionary=plot_dictionary)

    dict1 = {key: value[0] if isinstance(value, list) else value for key, value in plot_items}
    dict2 = {key: value[1] if isinstance(value, list) else value for key, value in plot_items}

    axs[0].plot(x_data[0], y_data[0], **dict1)
    axs[0].set_xlabel(x_labels[0])
    axs[0].set_ylabel(y_labels[0])

    axs[1].plot(x_data[1], y_data[1], **dict2)
    axs[1].set_xlabel(x_labels[1])
    axs[1].set_ylabel(y_labels[1])
    plt.tight_layout()
    plt.show()
