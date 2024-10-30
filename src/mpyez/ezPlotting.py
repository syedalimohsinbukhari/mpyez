"""Created on Jul 23 23:41:18 2024"""

__all__ = ['plot_two_column_file', 'plot_xy', 'plot_with_dual_axes', 'two_subplots', 'n_plotter']

from typing import List, Optional, Tuple, Union

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams

from .backend.ePlotting import OrientationError
from .backend.uPlotting import label_handler, LinePlot, plot_dictionary_handler, plot_or_scatter, ScatterPlot, SubPlots

# safeguard
line_plot = "LinePlot"
scatter_plot = "ScatterPlot"
plot_dictionary_type = Optional[Union[LinePlot, ScatterPlot]]
axis_return = Union[List[plt.axis], plt.axis]


def plot_two_column_file(file_name: str,
                         delimiter: str = ',',
                         skip_header: bool = False,
                         auto_label: bool = False,
                         is_scatter: bool = False,
                         fig_size: Optional[Tuple[int, int]] = None,
                         plot_dictionary: Optional[plot_dictionary_type] = None,
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
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot. Default is False.
    fig_size : tuple of int, optional
        The size of the plot figure, only used if a new plot is created. If None, default matplotlib size will be used.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.
    axis: Optional[plt.axis]
        The axis object to draw the plots on. If not passed, a new axis object will be created internally.

    Returns
    -------
    list:
        Either a single or double axis list.
    """
    data = np.genfromtxt(file_name, delimiter=delimiter, skip_header=skip_header)

    if data.shape[1] != 2:
        raise ValueError("The file must contain exactly two columns of data.")

    x_data, y_data = data.T

    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, auto_label=auto_label, is_scatter=is_scatter, fig_size=fig_size,
                               plot_dictionary=plot_dictionary, axis=axis)


def plot_xy(x_data: np.ndarray, y_data: np.ndarray,
            data_label: str = 'X1 vs Y1',
            auto_label: bool = False,
            is_scatter: bool = False,
            fig_size: Optional[Tuple[int, int]] = None,
            plot_dictionary: Optional[plot_dictionary_type] = None,
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
    data_label: str
        Data label for the plot to put in the legend. Defaults to 'X1 vs Y1'.
    auto_label : bool, optional
        If True, automatically sets x and y-axis labels and the plot title. Default is False.
    is_scatter : bool, optional
        If True, creates a scatter plot. Otherwise, creates a line plot. Default is False.
    fig_size : tuple of int, optional
        The size of the plot figure. If None, default matplotlib size will be used.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.
    axis: Optional[plt.axis]
        The axis object to draw the plots on. If not passed, a new axis object will be created internally.

    Returns
    -------
    list:
        Either a single or double axis list.
    """
    return plot_with_dual_axes(x1_data=x_data, y1_data=y_data, x1y1_label=data_label, auto_label=auto_label, is_scatter=is_scatter, fig_size=fig_size,
                               plot_dictionary=plot_dictionary, axis=axis)


def plot_with_dual_axes(x1_data: np.ndarray, y1_data: np.ndarray,
                        x2_data: np.ndarray = None, y2_data: np.ndarray = None,
                        x1y1_label: str = 'X1 vs Y1',
                        x1y2_label: str = 'X1 vs Y2',
                        x2y1_label: str = 'X2 vs Y1',
                        use_twin_x: bool = False,
                        auto_label: bool = False,
                        is_scatter: bool = False,
                        fig_size: Optional[Tuple[int, int]] = None,
                        plot_dictionary: Optional[plot_dictionary_type] = None,
                        axis: Optional[plt.axis] = None) -> axis_return:
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
    is_scatter : bool, optional
        If True, creates scatter plot; otherwise, line plot. Default is False.
    fig_size : Tuple[int, int], optional
        Figure size for the plot. If None, default matplotlib size will be used.
    plot_dictionary: Union[LinePlot, ScatterPlot], optional
        An object representing the plot data, either a `LinePlot` or `ScatterPlot`,  to be passed to the matplotlib plotting library.
         If None, a default plot type will be used.
    axis: Optional[plt.axis]
        The axis object to draw the plots on. If not passed, a new axis object will be created internally.

    Returns
    -------
    list:
        Either a single or double axis list.
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

    plot_items = plot_dictionary_handler(plot_dictionary=plot_dictionary)

    dict1 = {key: (value[0] if isinstance(value, list) else value) for key, value in plot_items}
    use_secondary_values = x2_data is not None or y2_data is not None or use_twin_x
    dict2 = {key: (value[1] if use_secondary_values else None) for key, value in plot_items}

    plot_or_scatter(axes=ax1, scatter=is_scatter)(x1_data, y1_data, label=x1y1_label, **dict1)

    ax2 = None

    if auto_label:
        ax1.set_xlabel('X1')
        ax1.set_ylabel('Y1')
        ax1.set_title('Plot')

    if use_twin_x:
        ax2 = ax1.twinx()
        plot_or_scatter(axes=ax2, scatter=is_scatter)(x1_data, y2_data, label=x1y2_label, **dict2)
        if auto_label:
            ax2.set_ylabel('Y2')

    elif x2_data is not None:
        ax2 = ax1.twiny()
        plot_or_scatter(axes=ax2, scatter=is_scatter)(x2_data, y1_data, label=x2y1_label, **dict2)
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


def two_subplots(x_data: List[np.ndarray], y_data: List[np.ndarray],
                 x_labels: List[str], y_labels: List[str], data_labels: List[str],
                 orientation: str = 'h',
                 auto_label: bool = False,
                 is_scatter: bool = False,
                 subplot_dictionary: Optional[SubPlots] = None,
                 plot_dictionary: Optional[Union[LinePlot, ScatterPlot]] = None) -> None:
    """
    Creates two subplots arranged horizontally or vertically, with optional customization.

    This function internally calls `n_plotter` to handle the plotting of each subplot.
    `n_plotter` arranges the subplots and applies relevant plot and subplot dictionaries.

    Parameters
    ----------
    x_data : list of np.ndarray
        List containing x-axis data arrays for each subplot.
    y_data : list of np.ndarray
        List containing y-axis data arrays for each subplot.
    x_labels : list of str
        List of labels for the x-axes in each subplot.
    y_labels : list of str
        List of labels for the y-axes in each subplot.
    data_labels : list of str
        List of labels for the data series in each subplot.
    orientation : str, optional, default='h'
        Orientation of the subplots, either 'h' for horizontal or 'v' for vertical.
    auto_label : bool, default False
        Automatically assigns labels to subplots if `True`.
    is_scatter : bool, default False
        If `True`, plots data as scatter plots; otherwise, plots as line plots.
    subplot_dictionary : dict, optional
        Dictionary of parameters for subplot configuration.
    plot_dictionary : LinePlot or ScatterPlot, optional
        Object containing plot styling parameters. Defaults to `LinePlot`.
    """
    # CHANGELIST:
    #   Can take two x arguments and two y arguments
    #   added capability for SubPlots dictionary, have to test LinePlot/ScatterPlot dictionaries
    #   X and Y data can be now passed in as lists
    #   for two_subplots, it provides horizontal or vertical orientation because there'll only be two subplots.
    #   Handles not providing a subplot dictionary
    #   Handles not providing a plot dictionary
    #   includes is_scatter option for scatter plotting
    #   can now handle plot dictionary with various parameters, the first parameter is used in both dictionaries if second parameter is not provided.
    #   returns axes object
    #   adapts to `n_plotter` for plotting
    #   Removed the axes variable
    if orientation == 'h':
        n_rows, n_cols = 1, 2
    elif orientation == 'v':
        n_rows, n_cols = 2, 1
    else:
        raise OrientationError("The orientation must be either \'h\' or \'v\'.")

    return n_plotter(x_data=x_data, y_data=y_data,
                     n_rows=n_rows, n_cols=n_cols,
                     x_labels=x_labels, y_labels=y_labels, data_labels=data_labels,
                     auto_label=auto_label, is_scatter=is_scatter,
                     subplot_dictionary=subplot_dictionary, plot_dictionary=plot_dictionary)


def n_plotter(x_data: List[np.ndarray], y_data: List[np.ndarray],
              n_rows: int, n_cols: int,
              x_labels: Optional[List[str]] = None, y_labels: Optional[List[str]] = None, data_labels: Optional[List[str]] = None,
              auto_label: bool = False,
              is_scatter: bool = False,
              subplot_dictionary: Optional[SubPlots] = None,
              plot_dictionary: Optional[Union[LinePlot, ScatterPlot]] = None) -> Union[plt.figure, plt.axis]:
    """
    Plots multiple subplots in a grid with optional customization for each subplot.

    Parameters
    ----------
    x_data : list of np.ndarray
        List of x-axis data arrays for each subplot.
    y_data : list of np.ndarray
        List of y-axis data arrays for each subplot.
    n_rows : int
        Number of rows in the subplot grid.
    n_cols : int
        Number of columns in the subplot grid.
    x_labels : list of str, optional
        List of labels for the x-axes of each subplot.
    y_labels : list of str, optional
        List of labels for the y-axes of each subplot.
    data_labels : list of str, optional
        List of labels for the data series in each subplot.
    auto_label : bool, default False
        Automatically assigns labels to subplots if `True`.
    is_scatter : bool, default False
        If `True`, plots data as scatter plots; otherwise, plots as line plots.
    subplot_dictionary : dict, optional
        Dictionary of parameters for subplot configuration.
    plot_dictionary : LinePlot or ScatterPlot, optional
        Object containing plot styling parameters. Defaults to `LinePlot`.
    """
    # CHANGELIST:
    #   Can plot basic n_rows x n_cols data,where n_cols > n_rows
    #   Handles data labels, and uses `plot_xy` instead of `plot_on_dual_axes`
    #   Handles all dictionaries good -> for n_rows = 1
    #   logic of x_label, y_label and legend is simplified
    #   Doesn't show other y axes if share_y = True
    #   Works with axes passed as well,
    #   Removed the axes variable
    #   Handles multi-row and multi-column subplots as well
    #   Slight modification in multi-row and multi-column subplot decorations
    sp_dict = subplot_dictionary.get() if subplot_dictionary else SubPlots().get()

    fig, axs = plt.subplots(n_rows, n_cols, **sp_dict)
    axs = axs.flatten()

    plot_items = plot_dictionary_handler(plot_dictionary=plot_dictionary)

    main_dict = [{key: value[c] for key, value in plot_items} for c in range(n_cols * n_rows)]

    x_labels, y_labels = label_handler(x_labels=x_labels, y_labels=y_labels, n_rows=n_rows, n_cols=n_cols, auto_label=auto_label)

    shared_y = sp_dict.get('sharey')
    shared_x1 = sp_dict.get('sharex')
    shared_x2 = len(axs) - int(len(axs) / n_rows if n_rows > n_cols else n_cols)
    for index, ax, j, k in zip(range(n_cols * n_rows), axs, x_labels, y_labels):
        label = f'{x_labels[index]} vs {y_labels[index]}' if data_labels is None else data_labels[index]
        plot_or_scatter(axes=ax, scatter=is_scatter)(x_data[index], y_data[index], label=label, **main_dict[index])
        if shared_x1:
            if not index < shared_x2:
                ax.set_xlabel(j)
        else:
            ax.set_xlabel(j)
        if not (shared_y and index % n_cols != 0):
            ax.set_ylabel(k)
        ax.legend(loc='best')

    plt.tight_layout()

    return fig, axs
