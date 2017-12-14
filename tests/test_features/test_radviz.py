# tests.test_features.test_radviz
# Test the RadViz feature analysis visualizers
#
# Author:   Benjamin Bengfort <bbengfort@districtdatalabs.com>
# Created:  Fri Oct 07 12:19:19 2016 -0400
#
# Copyright (C) 2016 District Data Labs
# For license information, see LICENSE.txt
#
# ID: test_radviz.py [01d5996] benjamin@bengfort.com $

"""
Test the RadViz feature analysis visualizers
"""

##########################################################################
## Imports
##########################################################################

import unittest
import numpy as np
import numpy.testing as npt
import warnings

from tests.base import VisualTestCase
from tests.dataset import DatasetMixin
from yellowbrick.features.radviz import *


##########################################################################
## RadViz Base Tests
##########################################################################

class RadVizTests(VisualTestCase, DatasetMixin):
    X = np.array(
            [[ 2.318, 2.727, 4.260, 7.212, 4.792],
             [ 2.315, 2.726, 4.295, 7.140, 4.783,],
             [ 2.315, 2.724, 4.260, 7.135, 4.779,],
             [ 2.110, 3.609, 4.330, 7.985, 5.595,],
             [ 2.110, 3.626, 4.330, 8.203, 5.621,],
             [ 2.110, 3.620, 4.470, 8.210, 5.612,]]
        )

    y = np.array([1, 1, 0, 1, 0, 0])

    def setUp(self):
        self.occupancy = self.load_data('occupancy')

    def tearDown(self):
        self.occupancy = None

    def test_normalize_x(self):
        """
        Test the static normalization method on the RadViz class
        """
        expected = np.array(
            [[ 1.        ,  0.00332594,  0.        ,  0.07162791,  0.01543943],
             [ 0.98557692,  0.00221729,  0.16666667,  0.00465116,  0.00475059],
             [ 0.98557692,  0.        ,  0.        ,  0.        ,  0.        ],
             [ 0.        ,  0.98115299,  0.33333333,  0.79069767,  0.96912114],
             [ 0.        ,  1.        ,  0.33333333,  0.99348837,  1.        ],
             [ 0.        ,  0.99334812,  1.        ,  1.        ,  0.98931116]]
        )

        Xp = RadViz.normalize(self.X)
        npt.assert_array_almost_equal(Xp, expected)

    def test_radviz(self):
        """
        Assert no errors occur during radviz visualizer integration
        """
        visualizer = RadViz()
        visualizer.fit_transform(self.X, self.y)
        visualizer.poof()
        self.assert_images_similar(visualizer)

    def test_integrated_radviz(self):
        """
        Test radviz on the real, occupancy data set
        """

        # Load the data from the fixture
        X = self.occupancy[[
            "temperature", "relative_humidity", "light", "C02", "humidity"
        ]]
        y = self.occupancy['occupancy'].astype(int)

        # Convert X to an ndarray
        X = X.view((float, len(X.dtype.names)))

        # Test the visualizer
        visualizer = RadViz()
        visualizer.fit_transform(X, y)
        visualizer.poof()
        self.assert_images_similar(visualizer)




class RadVizNullTests(unittest.TestCase):
    def test_raise_warning_if_nans_exist(self):
        """
        Test that a warning is raised if any nans are in the data
        """
        data = np.array([
            [1, 2, 3],
            [1, 2, np.nan],
        ])
        
        self.assertWarns(UserWarning, warn_if_nans_exist, data)

    def test_count_rows_with_nans(self):
        """
        Test that a warning is raised if any nans are in the data
        """
        data0 = np.array([
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3],
        ])

        data2 = np.array([
            [np.nan, 2, 3],
            [1, np.nan, 3],
        ])

        data3 = np.array([
            [np.nan, 2, 3],
            [1, np.nan, 3],
            [np.nan, np.nan, np.nan],
        ])

        self.assertEqual(0, count_nan_rows(data0))
        self.assertEqual(2, count_nan_rows(data2))
        self.assertEqual(3, count_nan_rows(data3))

    def test_drop_nan_rows_no_nans(self):
        """
        Test that an array with no nulls is returned intact
        """
        data = np.array([
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
        ])

        observed = drop_rows_containing_nans(data)
        np.testing.assert_array_equal(data, observed)

    def test_drop_nan_rows(self):
        """
        Test that an array with nulls is returned without null containing rows
        """
        data = np.array([
            [1, 2, np.nan],
            [4, 5, 6],
            [np.nan, np.nan, np.nan],
        ])

        expected = np.array([
            [4, 5, 6],
        ])

        observed = drop_rows_containing_nans(data)
        np.testing.assert_array_equal(expected, observed)


def warn_if_nans_exist(data):
    """Warn if nans exist in a numpy array."""
    null_count = count_nan_rows(data)
    total = len(data)
    percent = null_count / total

    # if np.isnan(data).any():
    if null_count > 0:
        warnings.warn(
            'Warning! Found {} rows of {} ({}%) with nan/null/None '
            'values which are cannot be plotted.'.format(null_count, total, percent))


def count_nan_rows(data):
    """Count the number of rows that contain any nan values."""
    if data.shape[0] >= 2:
        return np.where(np.isnan(data).sum(axis=1) != 0, 1, 0).sum()


def drop_rows_containing_nans(data):
    """Drop rows in a numpy array that contain nan values."""
    return data[~np.isnan(data).any(axis=1)]
