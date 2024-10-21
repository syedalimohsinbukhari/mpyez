"""Created on Jul 23 23:41:18 2024"""

__all__ = ['plot_two_column_file', 'plot_xy', 'plot_with_dual_axes']

from typing import Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np

from .backend.ePlotting import DoubleLinePlot, DoubleScatterPlot, rc_color

# safeguard
double_scatter_plot = "DoubleScatterPlot"
double_line_plot = "DoubleLinePlot"


# TODO:
#   See what more plotting keywords can be added here
#   See if the kwargs are working or not with the new `set_labels_and_title`
#   Check if the `plt` objects returned are compatible with both axes in their respective functions.


def plot_two_column_file(file_name: str, delimiter: str = ',', skip_header: bool = False, auto_label: bool = False,
                         fig_size: Tuple[int, int] = (12, 5), is_scatter: bool = False) -> plt:
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

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    data = np.genfromtxt(file_name, delimiter=delimiter, skip_header=skip_header)

    if data.shape[1] != 2:
        raise ValueError("The file must contain exactly two columns of data.")

    x_data, y_data = data.T

    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, auto_label=auto_label, fig_size=fig_size, is_scatter=is_scatter)


def plot_xy(x_data: np.ndarray, y_data: np.ndarray, auto_label: bool = False, fig_size: Tuple[int, int] = (12, 5),
            is_scatter: bool = False) -> plt:
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

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    """
    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, auto_label=auto_label, fig_size=fig_size, is_scatter=is_scatter)


def plot_with_dual_axes(x1_data: np.ndarray, y1_data: np.ndarray,
                        x2_data: Optional[np.ndarray] = None, y2_data: Optional[np.ndarray] = None,
                        x1y1_label: str = 'X1 vs Y1', x1y2_label: str = 'X1 vs Y2', x2y1_label: str = 'X2 vs Y1',
                        use_twin_x: bool = False, auto_label: bool = False, fig_size: Tuple[int, int] = (12, 5),
                        is_scatter: bool = False, plot_dictionary: Union[DoubleLinePlot, DoubleScatterPlot] = None) -> plt:
    """
    Plots data with options for dual axes (x or y) or single axis.

    Parameters
    ----------
    plot_dictionary
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
        Figure size for the plot. Default is (12, 5).
    is_scatter : bool, optional
        If True, creates scatter plot; otherwise, line plot. Default is False.

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the generated plot.
    [fig, (ax1, ax2)] or [fig, ax1] depending on the presence of dual axes.
    """
    if use_twin_x and x2_data is not None:
        raise ValueError("Dual Y-axis plot requested but 'x2_data' given.")
    if not use_twin_x and y2_data is not None:
        raise ValueError("Dual X-axis plot requested but 'y2_data' given.")
    if len(x1_data) == 0 or len(y1_data) == 0:
        raise ValueError("Primary x or y data is empty. Please provide valid data.")

    fig, ax1 = plt.subplots(figsize=fig_size)

    def _plot_or_scatter(ax, scatter):
        return ax.scatter if scatter else ax.plot

    if plot_dictionary.__class__.__name__ in [double_line_plot, double_scatter_plot]:
        dict1 = {key: value[0] for key, value in plot_dictionary.get().items()}

        dict2 = {key: value[1] for key, value in plot_dictionary.get().items()}
    else:
        dict1, dict2 = {'c': rc_color[0]}, {'c': rc_color[1]}

    _plot_or_scatter(ax1, is_scatter)(x1_data, y1_data, label=x1y1_label, **dict1)

    ax2 = None

    if auto_label:
        ax1.set_xlabel('X1')
        ax1.set_ylabel('Y1')
        ax1.set_title('Plot')

    if use_twin_x:
        ax2 = ax1.twinx()
        _plot_or_scatter(ax2, is_scatter)(x1_data, y2_data, label=x1y2_label, **dict2)
        if auto_label:
            ax2.set_ylabel('Y2')

    elif x2_data is not None:
        ax2 = ax1.twiny()
        _plot_or_scatter(ax2, is_scatter)(x2_data, y1_data, label=x2y1_label, **dict2)
        if auto_label:
            ax2.set_xlabel('X2')

    handles, labels = ax1.get_legend_handles_labels()
    if ax2:
        handles2, labels2 = ax2.get_legend_handles_labels()
        handles += handles2
        labels += labels2

    ax1.legend(handles, labels, loc='best')

    plt.tight_layout()

    return [fig, (ax1, ax2)] if ax2 else [fig, ax1]
