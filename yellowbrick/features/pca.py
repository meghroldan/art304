# -*- coding: utf-8 -*-
# yellowbrick.features.pca
# Decomposition based feature visualization with PCA.
#
# Author:   Carlo Morales <@cjmorale>
# Author:   Raúl Peralta Lozada <@RaulPL>
# Author:   Benjamin Bengfort <@bbengfort>
# Created:  Tue May 23 18:34:27 2017 -0400
#
# ID: pca.py [] cmorales@pacificmetrics.com $

"""
Decomposition based feature visualization with PCA.
"""

##########################################################################
## Imports
##########################################################################

# NOTE: must import mplot3d to load the 3D projection
import mpl_toolkits.mplot3d # noqa
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.pyplot as plt
import numpy as np
from yellowbrick.features.base import MultiFeatureVisualizer
from yellowbrick.style import palettes
from yellowbrick.exceptions import YellowbrickValueError

from sklearn.pipeline import Pipeline
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler


##########################################################################
##2D and #3D PCA Visualizer
##########################################################################

class PCADecomposition(MultiFeatureVisualizer):
    """
    Produce a two or three dimensional principal component plot of a data array
    projected onto it's largest sequential principal components. It is common
    practice to scale the data array ``X`` before applying a PC decomposition.
    Variable scaling can be controlled using the ``scale`` argument.

    Parameters
    ----------
    ax : matplotlib Axes, default: None
        The axes to plot the figure on. If None is passed in the current axes.
        will be used (or generated if required).

    features: list, default: None
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    scale : bool, default: True
        Boolean that indicates if user wants to scale data.

    proj_dim : int, default: 2
        Dimension of the PCA visualizer.

    proj_features : bool, default: False
        Boolean that indicates if the user wants to project the features
        in the projected space. If True the plot will be similar to a biplot.

    color : list or tuple of colors, default: None
        Specify the colors for each individual class.

    colormap : string or cmap, default: None
        Optional string or matplotlib cmap to colorize lines.
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    random_state : int, RandomState instance or None, optional (default None)
        If input data is larger than 500x500 and the number of components to
        extract is lower than 80% of the smallest dimension of the data, then
        the more efficient `randomized` solver is enabled, this parameter sets
        the random state on this solver.

    kwargs : dict
        Keyword arguments that are passed to the base class and may influence
        the visualization as defined in other Visualizers.

    Examples
    --------
    >>> from sklearn import datasets
    >>> iris = datasets.load_iris()
    >>> X = iris.data
    >>> y = iris.target
    >>> visualizer = PCADecomposition()
    >>> visualizer.fit_transform(X)
    >>> visualizer.poof()

    """
    def __init__(self,
                 ax=None,
                 features=None,
                 scale=True,
                 proj_dim=2,
                 proj_features=False,
                 colorbar = False,
                 heatmap = False,
                 color=None,
                 colormap=palettes.DEFAULT_SEQUENCE,
                 random_state=None,
                 **kwargs):
        super(PCADecomposition, self).__init__(ax=ax,
                                               features=features,
                                               **kwargs)

        if proj_dim not in (2, 3):
            raise YellowbrickValueError("proj_dim object is not 2 or 3.")

        # Data Parameters
        self.scale = scale
        self.proj_dim = proj_dim
        self.proj_features = proj_features
        self.colorbar = colorbar 
        self.heatmap = heatmap

        # Create the PCA transformer
        self.pca_transformer = Pipeline(
            [('scale', StandardScaler(with_std=self.scale)),
             ('pca', PCA(self.proj_dim, random_state=random_state))]
        )

        # Visual Parameters
        self.color = color
        self.colormap = colormap

    def fit(self, X, y=None, **kwargs):
        """
        Fits the PCA transformer, transforms the data in X, then draws the
        decomposition in either 2D or 3D space as a scatter plot.

        Parameters
        ----------
        X : ndarray or DataFrame of shape n x m
            A matrix of n instances with m features.

        y : ndarray or Series of length n
            An array or series of target or class values.

        Returns
        -------
        self : visualizer
            Returns self for use in Pipelines
        """
        super(PCADecomposition, self).fit(X=X, y=y, **kwargs)
        self.pca_transformer.fit(X)
        self.pca_components_ = self.pca_transformer.named_steps['pca'].components_
        return self

    def transform(self, X, y=None, **kwargs):
        self.orig_X = X
        self.pca_features_ = self.pca_transformer.transform(X)
        self.draw()
        return self.pca_features_

    def draw(self, **kwargs):
        X = self.pca_features_
        if self.proj_dim == 2:
            self.fig = plt.figure()
            if(self.heatmap):
                self.ax = self.fig.add_subplot(2,1,1)
            else:
                self.ax = self.fig.add_subplot(1,1,1)
            im = self.ax.scatter(X[:,0], X[:,1], c=self.color, cmap=self.colormap, edgecolors='black',
                             vmin= self.pca_components_.min(), vmax = self.pca_components_.max())
            if self.colorbar:
                divider = make_axes_locatable(self.ax)
                cax = divider.append_axes("bottom", size="10%", pad=0.63)
                plt.colorbar(im, cax = cax, orientation='horizontal',ticks=[self.pca_components_.min(), 0,self.pca_components_.max()])
            if self.heatmap:
                self.ax1 = self.fig.add_subplot(2,1,2)
                self.ax1.imshow(self.pca_components_, interpolation = 'none', cmap = self.colormap)
            
            if self.proj_features:
                x_vector = self.pca_components_[0]
                y_vector = self.pca_components_[1]
                max_x = max(X[:, 0])
                max_y = max(X[:, 1])
                for i in range(self.pca_components_.shape[1]):
                    self.ax.arrow(
                        x=0, y=0,
                        dx=x_vector[i] * max_x,
                        dy=y_vector[i] * max_y,
                        color='r', head_width=0.05,
                        width=0.005,
                    )
                    self.ax.text(
                        x_vector[i] * max_x * 1.05,
                        y_vector[i] * max_y * 1.05,
                        self.features_[i], color='r'
                    )
        if self.proj_dim == 3:
            self.fig = plt.figure()
            if(self.heatmap):
                self.ax = self.fig.add_subplot(211, projection='3d')
            else:
                self.ax = self.fig.add_subplot(111, projection='3d')
            
            im = self.ax.scatter(X[:,0], X[:,1], X[:, 2], c=self.color, cmap=self.colormap, alpha=0.4, edgecolors='black',
                             vmin= self.pca_components_.min(), vmax = self.pca_components_.max())
            if self.colorbar:
                plt.colorbar(im, orientation='horizontal', ticks=[self.pca_components_.min(), 0,self.pca_components_.max()])
            if self.heatmap:
                self.ax1 = self.fig.add_subplot(2,1,2)
                self.ax1.imshow(self.pca_components_, interpolation = 'none', cmap = self.colormap)
            if self.proj_features:
                x_vector = self.pca_components_[0]
                y_vector = self.pca_components_[1]
                z_vector = self.pca_components_[2]
                print(self.pca_components)
                max_x = max(X[:, 0])
                max_y = max(X[:, 1])
                max_z = max(X[:, 1])
                for i in range(self.pca_components_.shape[1]):
                    self.ax.plot(
                        [0, x_vector[i] * max_x],
                        [0, y_vector[i] * max_y],
                        [0, z_vector[i] * max_z],
                        color='y'
                    )
                    self.ax.text(
                        x_vector[i] * max_x * 1.05,
                        y_vector[i] * max_y * 1.05,
                        z_vector[i] * max_z * 1.05,
                        self.features_[i], color='y'
                    )
        return self.ax

    def finalize(self, **kwargs):
        # Set the title
        orig_X = self.orig_X
        self.ax.set_title('Principal Component Plot')
        self.ax.set_xlabel('\nPrincipal Component 1',linespacing=1.2)
        self.ax.set_ylabel('\nPrincipal Component 2',linespacing=1.2)
        if self.heatmap == True:
            feature_names = list(orig_X.columns)
            plt.gca().set_xticks(np.arange(-.5, len(feature_names)))
            plt.gca().set_xticklabels(feature_names, rotation=90, ha='left', fontsize=12)
            if self.proj_dim == 2:
                plt.gca().set_yticks(np.arange(0.5, 2))
                plt.gca().set_yticklabels(['First PC', 'Second PC'], va='bottom', fontsize=12)
            if self.proj_dim == 3:
                plt.gca().set_yticks(np.arange(0.5, 3))
                plt.gca().set_yticklabels(['First PC', 'Second PC', 'Third PC'], va='bottom', fontsize=12)
        if self.proj_dim == 3:
            self.ax.set_zlabel('Principal Component 3',linespacing=1.2)


##########################################################################
## Quick Method
##########################################################################

def pca_decomposition(X, y=None, ax=None, features=None, scale=True,
                      proj_dim=2, proj_features=False, color=None,
                      colormap=palettes.DEFAULT_SEQUENCE,
                      random_state=None, **kwargs):
    """Produce a two or three dimensional principal component plot of the data array ``X``
    projected onto it's largest sequential principal components. It is common practice to scale the
    data array ``X`` before applying a PC decomposition. Variable scaling can be controlled using
    the ``scale`` argument.

    Parameters
    ----------
    X : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features.

    y : ndarray or Series of length n
        An array or series of target or class values.

    ax : matplotlib Axes, default: None
        The axes to plot the figure on. If None is passed in the current axes.
        will be used (or generated if required).

    features: list, default: None
        a list of feature names to use
        If a DataFrame is passed to fit and features is None, feature
        names are selected as the columns of the DataFrame.

    scale : bool, default: True
        Boolean that indicates if user wants to scale data.

    proj_dim : int, default: 2
        Dimension of the PCA visualizer.

    proj_features : bool, default: False
        Boolean that indicates if the user wants to project the features
        in the projected space. If True the plot will be similar to a biplot.

    color : list or tuple of colors, default: None
        Specify the colors for each individual class.

    colormap : string or cmap, default: None
        Optional string or matplotlib cmap to colorize lines.
        Use either color to colorize the lines on a per class basis or
        colormap to color them on a continuous scale.

    random_state : int, RandomState instance or None, optional (default None)
        If input data is larger than 500x500 and the number of components to
        extract is lower than 80% of the smallest dimension of the data, then
        the more efficient `randomized` solver is enabled, this parameter sets
        the random state on this solver.

    kwargs : dict
        Keyword arguments that are passed to the base class and may influence
        the visualization as defined in other Visualizers.

    Examples
    --------
    >>> from sklearn import datasets
    >>> iris = datasets.load_iris()
    >>> X = iris.data
    >>> y = iris.target
    >>> pca_decomposition(X, color=y, proj_dim=3, colormap='RdBu_r')

    """
    # Instantiate the visualizer
    visualizer = PCADecomposition(
        ax=ax, features=features, scale=scale, proj_dim=proj_dim,
        proj_features=proj_features, color=color, colormap=colormap,
        random_state=random_state, **kwargs
    )

    # Fit and transform the visualizer (calls draw)
    visualizer.fit(X, y)
    visualizer.transform(X)
    visualizer.poof()

    # Return the axes object on the visualizer
    return visualizer.ax
