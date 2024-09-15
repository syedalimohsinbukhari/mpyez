"""Created on Jul 23 23:41:18 2024"""

__all__ = ['plot_two_column_file', 'plot_xy', 'plot_with_dual_axes']

from typing import Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np


# TODO:
#   See what more plotting keywords can be added here
#   See if the kwargs are working or not with the new `set_labels_and_title`
#   Check if the `plt` objects returned are compatible with both axes in their respective functions.


def plot_two_column_file(file_name: str, delimiter: str = ',', skip_header: bool = False, auto_label: bool = False,
                         fig_size: Tuple[int, int] = (12, 5), is_scatter: bool = False, axis=None) -> plt:
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
        If True, skips the first row in the given data file, otherwise does nothing (defaults to False).
    auto_label : bool, optional
        If True, automatically sets the x-axis label, y-axis label, and plot title (default is False).
    fig_size : tuple of int, optional
        The size of the plot figure, only used if a new plot is created (default is (12, 5)).
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot (default is False).
    axis : matplotlib axis, optional
        A specific matplotlib axis object to plot on. If None, a new plot is created (default is None).

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    data = np.genfromtxt(file_name, delimiter=delimiter, skip_header=skip_header)

    if data.shape[1] != 2:
        raise ValueError("The file must contain exactly two columns of data.")

    x_data, y_data = data.T

    return plot_xy(x_data, y_data, auto_label, fig_size, is_scatter, axis)


def plot_xy(x_data: np.ndarray, y_data: np.ndarray, auto_label: bool = False, fig_size: Tuple[int, int] = (12, 5),
            is_scatter: bool = False, axis=None) -> plt:
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
        If True, automatically sets x and y-axis labels and the plot title (default is False).
    fig_size : tuple of int, optional
        The size of the plot figure (default is (12, 5)).
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot (default is False).
    axis : matplotlib axis, optional
        A specific matplotlib axis object to plot on. If None, a new plot is created (default is None).

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    plotter = axis if axis else plt
    if not axis:
        plotter.figure(figsize=fig_size)

    if is_scatter:
        plot_function = plotter.scatter
    else:
        plot_function = plotter.plot

    plot_function(x_data, y_data)

    if auto_label:
        label_functions = {'x_label': plotter.set_xlabel if axis else plotter.xlabel,
                           'y_label': plotter.set_ylabel if axis else plotter.ylabel,
                           'title': plotter.set_title if axis else plotter.title}

        label_functions['x_label']('X-axis')
        label_functions['y_label']('Y-axis')
        label_functions['title']('X vs Y Plot')
        plotter.legend(loc='best')
        plotter.tight_layout()

    return plotter


def plot_with_dual_axes(x1_data: np.ndarray, y1_data: np.ndarray,
                        x2_data: Optional[np.ndarray] = None, y2_data: Optional[np.ndarray] = None,
                        x1y1_label: str = 'X1 vs Y1', x1y2_label: str = 'X1 vs Y2', x2y1_label: str = 'X2 vs Y1',
                        is_dual_y: bool = False, auto_label: bool = False, fig_size: Tuple[int, int] = (12, 5),
                        is_scatter: bool = False, color_y2: str = 'red', legend_loc: str = 'best') -> plt:
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
    is_dual_y : bool, optional
        If True, creates dual y-axis plot. If False, creates dual x-axis plot. Default is False.
    auto_label : bool, optional
        If True, automatically labels the axes and plot title. Default is False.
    fig_size : Tuple[int, int], optional
        Figure size for the plot. Default is (12, 5).
    is_scatter : bool, optional
        If True, creates scatter plot; otherwise, line plot. Default is False.
    color_y2 : str, optional
        Color for the secondary y-axis or X2 axis plot (default is 'red').
    legend_loc : str, optional
        Location of the legend (default is 'best').

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    [fig, (ax1, ax2)] or [fig, ax1] depending on the presence of dual axes.
    """
    if is_dual_y and y2_data is None:
        raise ValueError("Dual Y-axis plot requested but 'y2_data' is None.")
    if not is_dual_y and x2_data is None:
        raise ValueError("Dual X-axis plot requested but 'x2_data' is None.")
    if len(x1_data) == 0 or len(y1_data) == 0:
        raise ValueError("Primary x or y data is empty. Please provide valid data.")

    fig, ax1 = plt.subplots(figsize=fig_size)

    def _plot_or_scatter(ax, scatter):
        return ax.scatter if scatter else ax.plot

    _plot_or_scatter(ax1, is_scatter)(x1_data, y1_data, label=x1y1_label)

    if auto_label:
        ax1.set_xlabel('X1')
        ax1.set_ylabel('Y1')
        ax1.set_title('Plot')

    if is_dual_y:
        ax2 = ax1.twinx()
        _plot_or_scatter(ax2, is_scatter)(x1_data, y2_data, label=x1y2_label, color=color_y2)
        if auto_label:
            ax2.set_ylabel('Y2')
    else:
        ax2 = ax1.twiny()
        _plot_or_scatter(ax2, is_scatter)(x2_data, y1_data, label=x2y1_label, color=color_y2)
        if auto_label:
            ax2.set_xlabel('X2')

    handles, labels = ax1.get_legend_handles_labels()
    if ax2:
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles += handles2
        labels += labels2

    ax1.legend(handles, labels, loc=legend_loc)

    plt.tight_layout()

    return [fig, (ax1, ax2)] if ax2 else [fig, ax1]
