#!/usr/bin/env python3
"""
Author: Rudi César Comiotto Modena
Email: rudi.modena@gmail.com
"""
import numpy as np


def calculate(list_numbers):
    """
    Function that outputs some statistics of the rows, columns, and elements in a 3 x 3 matrix.
    The statistics are:
    - mean;
    - variance;
    - standard deviation;
    - max;
    - min
    - sum.
    """

    # If the list containing less than 9 elements it should raise a ValueError
    if len(list_numbers) < 9:
        raise ValueError("List must contain nine numbers.")

    # Convert the list into a 3 x 3 Numpy array
    np_matrix = np.array(list_numbers).reshape((3, 3))

    # Dictionary with the statistics to evaluate
    dict_statistics = {
        'mean': np.mean,
        'variance': np.var,
        'standard deviation': np.std,
        'max': np.max,
        'min': np.min,
        'sum': np.sum,
    }

    # Create the dictionary with the statistics of the list
    calculations = dict()
    for name, function in dict_statistics.items():
        calculations[name] = [
            function(np_matrix, axis=0).tolist(),
            function(np_matrix, axis=1).tolist(),
            function(np_matrix).tolist()]
    return calculations
