"""Created on Jul 23 23:41:18 2024"""

from typing import List, Tuple

import matplotlib.pyplot as plt
import numpy as np


def two_column_file(file_name: str, data_label: str, x_label: str, y_label: str, delimiter: str = ',',
                    fig_size: Tuple[int, int] = (12, 5), **kwargs) -> None:
    """
    Plots data from a simple two-column file.

    Parameters
    ----------
    file_name : str
        The name of the file to be plotted.
    data_label : str
        The label to be assigned to the plotted data.
    x_label : str
        The label to be assigned to the x-axis.
    y_label : str
        The label to be assigned to the y-axis.
    delimiter : str, optional
        The delimiter to be used with the CSV file (default is ',').
    fig_size : tuple of int, optional
        The figure size to be used by the plot (default is (12, 5)).
    kwargs : dict
        Additional keyword arguments to customize the plot (e.g., line style).

    Returns
    -------
    None
        The function does not return any value. It displays the plot.
    """
    # Load the data from the CSV file
    csv_ = np.genfromtxt(file_name, delimiter=delimiter)

    # Transpose the data to separate x and y
    x, y = csv_.transpose()

    # Get the line style from kwargs if provided, else default to '-'
    line_style = kwargs.get('ls', '-')

    # Create the figure and plot the data
    plt.figure(figsize=fig_size)
    plt.plot(x, y, label=data_label, ls=line_style)

    # Set the labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(data_label)

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    # Display the plot
    plt.show()


def plot_xy(x_data: List[float], y_data: List[float], data_label: str = '', x_label: str = '', y_label: str = '',
            plot_title: str = '', fig_size: Tuple[int, int] = (12, 5), auto_label: bool = False) -> None:
    """
    Plots x_data against y_data with various customization options.

    Parameters
    ----------
    x_data : list of float
        The data for the x-axis.
    y_data : list of float
        The data for the y-axis.
    data_label : str, optional
        The label for the data (default is '').
    x_label : str, optional
        The label for the x-axis (default is '').
    y_label : str, optional
        The label for the y-axis (default is '').
    plot_title : str, optional
        The title of the plot (default is '').
    fig_size : tuple of int, optional
        The size of the figure (default is (12, 5)).
    auto_label : bool, optional
        If True, automatically set the labels and title (default is False).

    Returns
    -------
    None
        The function does not return any value. It displays the plot.

    Notes
    -----
    If `auto_label` is True, it will override `x_label`, `y_label`, `data_label`, and `plot_title` with default values.
    """

    # Automatically set labels and title if auto_label is True
    if auto_label:
        x_label = 'X'
        y_label = 'Y'
        data_label = 'data'
        plot_title = 'Plot between X and Y data'

    # Create the figure and plot the data
    plt.figure(figsize=fig_size)
    plt.plot(x_data, y_data, label=data_label)

    # Set the labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)

    # Add legend and improve layout
    plt.legend(loc='best')
    plt.tight_layout()

    # Display the plot
    plt.show()
