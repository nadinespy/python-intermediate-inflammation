"""Module containing models representing patients and their data.

The Model layer is responsible for the 'business logic' part of the software.

Patients' data is held in an inflammation table (2D array) where each row contains 
inflammation data for a single patient taken over a number of days 
and each column represents a single day across all patients.
"""

import numpy as np


def load_csv(filename):
    """Load a Numpy array from a CSV

    :param filename: Filename of CSV to load
    """
    return np.loadtxt(fname=filename, delimiter=',')


def patient_normalise(data):
    """
    Normalise patient data between 0 and 1 of a 2D inflammation data array.

    Any NaN values are ignored, and normalised to 0

    :param data: 2D array of inflammation data
    :type data: ndarray

    """
    if np.any(data < 0):
        raise ValueError('inflammation values should not be negative')
    if not isinstance(data, np.ndarray):
        raise TypeError('data input should be ndarray')
    if len(data.shape) != 2:
        raise ValueError('inflammation array should be two-dimensional')
    max_val = np.nanmax(data, axis=1)
    with np.errstate(invalid='ignore', divide='ignore'):
        normalised = data / max_val[:, np.newaxis]
    normalised[np.isnan(normalised)] = 0
    normalised[normalised < 0] = 0
    return normalised


def daily_mean(data):
    """Calculate the daily mean of a 2D inflammation data array.

   :param data: A 2D data array with inflammation data (each row
   contains measurements for a single patient across all days).
   :returns: An array of mean values of measurements for each day.
    """

    return np.mean(data, axis=0)


def daily_max(data):
    """Calculate the daily max of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row
    contains measurements for a single patient across all days).
    :returns: An array of max values of measurements for each day.
    """
    return np.max(data, axis=0)


def daily_min(data):
    """Calculate the daily min of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row
    contains measurements for a single patient across all days).
    :returns: An array of minimum values of measurements for each day.
    """
    return np.min(data, axis=0)


def daily_std(data):
    """Calculate the daily std of a 2D inflammation data array.

    :param data: A 2D data array with inflammation data (each row
    contains measurements for a single patient across all days).
    :returns: An array of standard deviations of measurements for each day.
    """
    return np.std(data, axis=0)


def daily_above_threshold(patient_num, data, threshold):
    """Determine whether or not each daily inflammation value exceeds a given threshold for a given patient.

    :param patient_num: The patient row number
    :param data: A 2D data array with inflammation data
    :param threshold: An inflammation threshold to check each daily value against
    :returns: A boolean list representing whether or not each patient's daily inflammation exceeded the threshold
    """
    return list(map(lambda x: x > threshold, data[patient_num]))

