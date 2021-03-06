#!/usr/bin/python

from numpy import trapz
from numpy import nan_to_num

BLOCK_SIZE = 100


# This function takes in a list of frequencies (ranging from o to 22050 Hz)
# and a list of levels in dB.  It builds a set of training data corresponding
# to the frequencies, levels, and category, and returns it
def generate(frequencies, levels, file_name):
    training_data = []
    differences = []

    max_value = int(max(frequencies)/BLOCK_SIZE + 1)
    for i in range(1, max_value):
        area = get_area(i - 1 * BLOCK_SIZE, i * BLOCK_SIZE, frequencies, levels)
        training_data.append(area)

        if i > 1:
            differences.append(area/training_data[i - 2])

    training_data.extend(differences)
    # if training_data[2] <= -2599.123:
    #     print file_name
    return nan_to_num(training_data)


def get_area(min, max, frequencies, levels):
    values = []

    for i in range(0, len(frequencies)):
        if frequencies[i] > min and frequencies[i] < max:
            values.append(levels[i])

    # Compute the area using the composite trapezoidal rule.
    area = trapz(values, dx=BLOCK_SIZE)
    return area

