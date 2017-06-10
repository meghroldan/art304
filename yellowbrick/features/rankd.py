# yellowbrick.features.rankd
# Implements 1D (histograms) and 2D (joint plot) feature rankings.
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Fri Oct 07 15:14:01 2016 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: rankd.py [ee754dc] benjamin@bengfort.com $

"""
Implements 1D (histograms) and 2D (joint plot) feature rankings.
"""

##########################################################################
## Imports
##########################################################################

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import shapiro

from yellowbrick.utils import is_dataframe
from yellowbrick.features.base import FeatureVisualizer
from yellowbrick.exceptions import YellowbrickValueError
from yellowbrick.style.colors import resolve_colors, get_color_cycle


##########################################################################
## Quick Methods
##########################################################################

def rank1d(X, y=None, ax=None, algorithm='shapiro', features=None,
           colormap='RdBu_r', **kwargs):
    """Scores each feature with the algorithm and ranks them in a bar plot.

    This helper function is a quick wrapper to utilize the Rank1D Visualizer
    (Transformer) for one-off analysis.

    Parameters
    ----------
    X : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features

    y : ndarray or Series of length n
        An array or series of target or class values

    ax : matplotlib axes
        the axis to plot the figure on.

    algorithm : one of {'shapiro', }, default: 'shapiro'
        The ranking algorithm to use, default is 'Shapiro-Wilk.

    features : list
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    colormap : string or cmap
        optional string or matplotlib cmap to colorize lines
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    Returns
    -------
    ax : matplotlib axes
        Returns the axes that the parallel coordinates were drawn on.

    """
    # Instantiate the visualizer
    visualizer = Rank1D(ax, algorithm, features, colormap, **kwargs)

    # Fit and transform the visualizer (calls draw)
    visualizer.fit(X, y, **kwargs)
    visualizer.transform(X)

    # Return the axes object on the visualizer
    return visualizer.ax

def rank2d(X, y=None, ax=None, algorithm='pearson', features=None,
           colormap='RdBu_r', **kwargs):
    """Displays pairwise comparisons of features with the algorithm and ranks
    them in a lower-left triangle heatmap plot.

    This helper function is a quick wrapper to utilize the Rank2D Visualizer
    (Transformer) for one-off analysis.

    Parameters
    ----------
    X : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features

    y : ndarray or Series of length n
        An array or series of target or class values

    ax : matplotlib axes
        the axis to plot the figure on.

    algorithm : one of {pearson, covariance}
        the ranking algorithm to use, default is Pearson correlation.

    features : list
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    colormap : string or cmap
        optional string or matplotlib cmap to colorize lines
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    Returns
    -------
    ax : matplotlib axes
        Returns the axes that the parallel coordinates were drawn on.

    """
    # Instantiate the visualizer
    visualizer = Rank2D(ax, algorithm, features, colormap, **kwargs)

    # Fit and transform the visualizer (calls draw)
    visualizer.fit(X, y, **kwargs)
    visualizer.transform(X)

    # Return the axes object on the visualizer
    return visualizer.ax


##########################################################################
## Base Feature Visualizer
##########################################################################

class RankDBase(FeatureVisualizer):
    """
    Base visualizer for Rank1D and Rank2D

    Parameters
    ----------
    ax : matplotlib Axes, default: None
        The axis to plot the figure on. If None is passed in the current axes
        will be used (or generated if required).

    algorithm : string
        The ranking algorithm to use; options and defaults vary by subclass

    features : list
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    colormap : string or cmap, default: 'RdBu_r'
        optional string or matplotlib cmap to colorize lines
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    kwargs : dict
        Keyword arguments that are passed to the base class and may influence
        the visualization as defined in other Visualizers.

    Examples
    --------

    >>> visualizer = Rank2D()
    >>> visualizer.fit(X, y)
    >>> visualizer.transform(X)
    >>> visualizer.poof()

    Notes
    -----
    These parameters can be influenced later on in the visualization
    process, but can and should be set as early as possible.
    """

    def __init__(self, ax=None, algorithm='shapiro', features=None,
                 colormap='RdBu_r', **kwargs):
        """
        Initialize the class with the options required to rank and
        order features as well as visualize the result.
        """
        super(RankDBase, self).__init__(ax=ax, **kwargs)

        # Data Parameters
        self.ranking_  = algorithm
        self.features_ = features

        # Visual Parameters
        self.colormap = colormap

    def fit(self, X, y=None, **kwargs):
        """
        The fit method gathers information about the state of the visualizer.

        Parameters
        ----------
        X : ndarray or DataFrame of shape n x m
            A matrix of n instances with m features

        y : ndarray or Series of length n
            An array or series of target or class values

        kwargs : dict
            Pass generic arguments to the drawing method

        Returns
        -------
        self : instance
            Returns the instance of the transformer/visualizer
        """
        # Get the shape of the data
        nrows, ncols = X.shape

        # Handle the feature names if they're None.
        if self.features_ is None:

            # If X is a data frame, get the columns off it.
            if is_dataframe(X):
                self.features_ = X.columns

            # Otherwise create numeric labels for each column.
            else:
                self.features_ = [
                    str(cdx) for cdx in range(ncols)
                ]

        # Fit always returns self.
        return self

    def transform(self, X, **kwargs):
        """
        The transform method is the primary drawing hook for ranking classes.

        Parameters
        ----------
        X : ndarray or DataFrame of shape n x m
            A matrix of n instances with m features

        kwargs : dict
            Pass generic arguments to the drawing method

        Returns
        -------
        X' : ndarray
            The transformed matrix, X'
        """
        # Rank and draw the input matrix
        R = self.rank(X)
        self.draw(R, **kwargs)

        # Return the X matrix, unchanged
        return X

    def rank(self, X, algorithm=None):
        """
        Returns the ranking of each pair of columns as an m by m matrix.

        Parameters
        ----------
        X : ndarray or DataFrame of shape n x m
            A matrix of n instances with m features

        algorithm : str or None
            The ranking mechanism to use, or None for the default

        Returns
        -------
        R : ndarray
            The mxm ranking matrix of the variables
        """
        algorithm = algorithm or self.ranking_
        algorithm = algorithm.lower()

        if algorithm not in self.ranking_methods:
            raise YellowbrickValueError(
                "'{}' is unrecognized ranking method".format(algorithm)
            )

        # Extract matrix from dataframe if necessary
        if is_dataframe(X):
            X = X.as_matrix()

        return self.ranking_methods[algorithm](X)

    def finalize(self, **kwargs):
        """
        Finalize executes any subclass-specific axes finalization steps.
        The user calls poof and poof calls finalize.

        Parameters
        ----------
        kwargs: dict
            generic keyword arguments

        """
        # Set the title
        self.set_title(
            "{} Ranking of {} Features".format(
                self.ranking_.title(), len(self.features_)
            )
        )


##########################################################################
## Rank 1D Feature Visualizer
##########################################################################

class Rank1D(RankDBase):
    """
    Rank1D computes a score for each feature in the data set with
    a specific metric or algorithm (e.g. takes the shapiro) then returns
    them ranked as a bar plot.

    Parameters
    ----------
    ax : matplotlib Axes, default: None
        The axis to plot the figure on. If None is passed in the current axes
        will be used (or generated if required).

    algorithm : one of {'shapiro', }, default: 'shapiro'
        The ranking algorithm to use, default is 'Shapiro-Wilk.

    features : list
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    colormap : string or cmap, default: 'RdBu_r'
        optional string or matplotlib cmap to colorize lines
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    kwargs : dict
        Keyword arguments that are passed to the base class and may influence
        the visualization as defined in other Visualizers.

    Examples
    --------

    >>> visualizer = Rank2D()
    >>> visualizer.fit(X, y)
    >>> visualizer.transform(X)
    >>> visualizer.poof()
    """
    ranking_methods = {
        'shapiro': lambda X: np.array([shapiro(x)[0] for x in X.T]),
    }

    def __init__(self, ax=None, algorithm='shapiro', features=None,
                 colormap='RdBu_r', **kwargs):
        """
        Initialize the class with the options required to rank and
        order features as well as visualize the result.
        """
        super(Rank1D, self).__init__(ax=None, algorithm=algorithm, features=features,
                         colormap=colormap, **kwargs)

    def draw(self, R, **kwargs):
        """
        Draws the heatmap of the ranking matrix of variables.
        """
        self.ax.bar(np.arange(len(R)), R, color=self.colormap[0])
        self.ax.set_xticks(np.arange(len(R)))
        self.ax.xaxis.grid(False)
        self.ax.set_xticklabels(self.features_, rotation=90, ha='left')


##########################################################################
## Rank 2D Feature Visualizer
##########################################################################

class Rank2D(RankDBase):
    """
    Rank2D performs pairwise comparisons of each feature in the data set with
    a specific metric or algorithm (e.g. Pearson correlation) then returns
    them ranked as a lower left triangle diagram.

    Parameters
    ----------
    ax : matplotlib Axes, default: None
        The axis to plot the figure on. If None is passed in the current axes
        will be used (or generated if required).

    algorithm : one of {'pearson', 'covariance'}, default: 'pearson'
        The ranking algorithm to use, default is Pearson correlation.

    features : list
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    colormap : string or cmap, default: 'RdBu_r'
        optional string or matplotlib cmap to colorize lines
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    kwargs : dict
        Keyword arguments that are passed to the base class and may influence
        the visualization as defined in other Visualizers.

    Examples
    --------

    >>> visualizer = Rank2D()
    >>> visualizer.fit(X, y)
    >>> visualizer.transform(X)
    >>> visualizer.poof()

    Notes
    -----
    These parameters can be influenced later on in the visualization
    process, but can and should be set as early as possible.
    """

    ranking_methods = {
        'pearson': lambda X: np.corrcoef(X.transpose()),
        'covariance': lambda X: np.cov(X.transpose()),
    }

    def __init__(self, ax=None, algorithm='pearson', features=None,
                 colormap='RdBu_r', **kwargs):
        """
        Initialize the class with the options required to rank and
        order features as well as visualize the result.
        """
        super(Rank2D, self).__init__(ax=None, algorithm=algorithm, features=features,
                         colormap=colormap, **kwargs)

    def draw(self, R, **kwargs):
        """
        Draws the heatmap of the ranking matrix of variables.
        """
        # Set the axes aspect to be equal
        self.ax.set_aspect("equal")
        self.ax.set_xticks(np.arange(len(R)))
        self.ax.set_yticks(np.arange(len(R)))

        # Generate a mask for the upper triangle
        mask = np.zeros_like(R, dtype=np.bool)
        mask[np.triu_indices_from(mask)] = True

        # Draw the heatmap
        # TODO: Move mesh to a property so the colorbar can be finalized
        data = np.ma.masked_where(mask, R)
        mesh = self.ax.pcolormesh(data, cmap=self.colormap, vmin=   -1, vmax=1)

        # Set the Axis limits
        self.ax.set(
            xlim=(0, data.shape[1]), ylim=(0, data.shape[0])
        )

        # Add the colorbar
        cb = self.ax.figure.colorbar(mesh, None, self.ax)
        cb.outline.set_linewidth(0)

        # Reverse the rows to get the lower left triangle
        self.ax.invert_yaxis()

        self.ax.set_xticklabels(self.features_, rotation=90, ha='left')
        self.ax.set_yticklabels(self.features_, va='top')
