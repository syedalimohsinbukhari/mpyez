"""Created on Jul 23 23:41:18 2024"""

from typing import Dict, Optional, Tuple

import matplotlib.pyplot as plt
import numpy as np


# TODO:
#   See what more plotting keywords can be added here


def set_labels_and_title(auto_label: bool, default_labels: Dict[str, str], **kwargs) -> Dict[str, str]:
    """
    Helper function to set labels and title for the plots.

    Parameters
    ----------
    auto_label : bool
        If True, automatically set the labels and title with default values.
    default_labels : dict
        A dictionary containing default labels and title.
    kwargs : dict
        The keyword arguments provided to the plotting function.

    Returns
    -------
    labels : dict
        A dictionary with the final labels and title.
    """
    labels = {key: kwargs.get(key, default_labels[key]) for key in default_labels}
    if auto_label:
        labels.update(default_labels)
    return labels


def two_column_file(file_name: str, delimiter: str = ',', fig_size: Tuple[int, int] = (12, 5), auto_label: bool = False,
                    **plt_kwargs: Dict[str, Optional[str]]) -> plt:
    """
    Plots data from a simple two-column file.

    Parameters
    ----------
    file_name : str
        The name of the file to be plotted.
    delimiter : str, optional
        The delimiter to be used with the CSV file (default is ',').
    fig_size : tuple of int, optional
        The figure size to be used by the plot (default is (12, 5)).
    auto_label : bool, optional
        If True, automatically set the labels and title (default is False).
    plt_kwargs : dict, optional
        Additional keyword arguments to customize the plot (e.g., line style).

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the plot.
    """
    # Default labels and title
    default_labels = {
        'x_label': 'X',
        'y_label': 'Y',
        'data_label': 'data',
        'plot_title': 'Plot between X and Y data'
    }

    # Set the labels and title
    labels = set_labels_and_title(auto_label, default_labels, **plt_kwargs)

    # Load the data from the CSV file
    data = np.genfromtxt(file_name, delimiter=delimiter)
    x, y = data.T

    # Create the figure and plot the data
    plt.figure(figsize=fig_size)
    plt.plot(x, y, label=labels['data_label'], ls=plt_kwargs.get('ls', '-'), lw=plt_kwargs.get('lw', 1))

    # Set the labels and title
    plt.xlabel(labels['x_label'])
    plt.ylabel(labels['y_label'])
    plt.title(labels['plot_title'])

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    return plt


def plot_xy(x_data: np.ndarray, y_data: np.ndarray, fig_size: Tuple[int, int] = (12, 5), auto_label: bool = False,
            **plt_kwargs: Dict[str, Optional[str]]) -> plt:
    """
    Plots x_data against y_data with various customization options.

    Parameters
    ----------
    x_data : list of float
        The data for the x-axis.
    y_data : list of float
        The data for the y-axis.
    fig_size : tuple of int, optional
        The size of the figure (default is (12, 5)).
    auto_label : bool, optional
        If True, automatically set the labels and title (default is False).
    plt_kwargs : dict, optional
        Additional keyword arguments to customize the plot (e.g., labels, title).

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the plot.
    """
    # Default labels and title
    default_labels = {
        'x_label': 'X',
        'y_label': 'Y',
        'data_label': 'data',
        'plot_title': 'Plot between X and Y data'
    }

    # Set the labels and title
    labels = set_labels_and_title(auto_label, default_labels, **plt_kwargs)

    # Create the figure and plot the data
    plt.figure(figsize=fig_size)
    plt.plot(x_data, y_data, label=labels['data_label'])

    # Set the labels and title
    plt.xlabel(labels['x_label'])
    plt.ylabel(labels['y_label'])
    plt.title(labels['plot_title'])

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    return plt


def plot_xyy(x_data: np.ndarray, y1_data: np.ndarray, y2_data: np.ndarray, fig_size: Tuple[int, int] = (12, 5),
             auto_label: bool = False, **plt_kwargs: Dict[str, Optional[str]]) -> plt:
    """
    Plots a dual y-axis plot with two different y-axis data sets.

    Parameters
    ----------
    x_data : np.ndarray
        The data for the x-axis.
    y1_data : np.ndarray
        The data for the first y-axis.
    y2_data : np.ndarray
        The data for the second y-axis.
    fig_size : tuple of int, optional
        The size of the figure (default is (12, 5)).
    auto_label : bool, optional
        If True, automatically set the labels and title (default is False).
    plt_kwargs : dict, optional
        Additional keyword arguments to customize the plot (e.g., labels, title).

    Returns
    -------
    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the plot.
    """
    # Default labels and title
    default_labels = {
        'x_label': 'X',
        'y1_label': 'Y1',
        'y2_label': 'Y2',
        'data1_label': 'data1',
        'data2_label': 'data2',
        'plot_title': 'TwinX plot between X, Y1, and Y2'
    }

    # Set the labels and title
    labels = set_labels_and_title(auto_label, default_labels, **plt_kwargs)

    # Create the figure
    plt.figure(figsize=fig_size)

    # Plot the first y-axis data
    plt.plot(x_data, y1_data, label=labels['data1_label'])
    plt.xlabel(labels['x_label'])
    plt.ylabel(labels['y1_label'])
    plt.title(labels['plot_title'])

    # Create the second y-axis and plot the data
    plt.twinx()
    plt.plot(x_data, y2_data, label=labels['data2_label'])
    plt.ylabel(labels['y2_label'])

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    return plt


def plot_xxy(y_data: np.ndarray, x1_data: np.ndarray, x2_data: np.ndarray, fig_size: Tuple[int, int] = (12, 5),
             auto_label: bool = False, **plt_kwargs: Dict[str, Optional[str]]) -> plt:
    """
    Plots a dual x-axis plot with two different x-axis data sets.

    Parameters
    ----------
    y_data : np.ndarray
        The data for the y-axis.
    x1_data : np.ndarray
        The data for the first x-axis.
    x2_data : np.ndarray
        The data for the second x-axis.
    fig_size : tuple of int, optional
        The size of the figure (default is (12, 5)).
    auto_label : bool, optional
        If True, automatically set the labels and title (default is False).
    plt_kwargs : dict, optional
        Additional keyword arguments to customize the plot (e.g., labels, title).

    Returns
    -------
    plt : matplotlib.pyplot
        The matplotlib.pyplot object for the plot.
    """
    # Default labels and title
    default_labels = {
        'y_label': 'Y',
        'x1_label': 'X1',
        'x2_label': 'X2',
        'data1_label': 'data1',
        'data2_label': 'data2',
        'plot_title': 'TwinX plot between X1, X2, and Y'
    }

    # Set the labels and title
    labels = set_labels_and_title(auto_label, default_labels, **plt_kwargs)

    # Create the figure
    plt.figure(figsize=fig_size)

    # Plot the first x-axis data
    plt.plot(x1_data, y_data, label=labels['data1_label'])
    plt.xlabel(labels['x1_label'])
    plt.ylabel(labels['y_label'])
    plt.title(labels['plot_title'])

    # Create the second x-axis and plot the data
    ax2 = plt.twiny()
    ax2.plot(x2_data, y_data, label=labels['data2_label'], color='orange')
    ax2.set_xlabel(labels['x2_label'])

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    return plt
