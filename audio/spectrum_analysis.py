#!/usr/bin/python

import matplotlib.pyplot as pyplot

from numpy import trapz
from numpy import nan_to_num

BLOCK_SIZE = 500

class SpectrumAnalyzer():

    def __init__(self, raw_data, category="unknown"):
        self.category = category
        self.frequencies, self.levels = self.parse_data(raw_data)


    def parse_data(self, raw_data):
        if len(raw_data) is 2:
            return raw_data[0], raw_data[1]

        frequencies = []
        levels = []

        count = 0
        while count < len(raw_data):
            frequency = float(raw_data[count])
            level = float(raw_data[count + 1])

            frequencies.append(frequency)
            levels.append(level)

            count += 2

        return frequencies, levels


    def get_area(self, min, max):
        values = []

        for i in range(0, len(self.frequencies)):
            if self.frequencies[i] > min and self.frequencies[i] < max:
                values.append(self.levels[i])

        # Compute the area using the composite trapezoidal rule.
        area = trapz(values, dx=BLOCK_SIZE)
        return area

    def training_data(self):
        training_data = []

        max_value = int(max(self.frequencies)/BLOCK_SIZE + 1)

        for i in range(1, max_value):
            area = self.get_area(i - 1 * BLOCK_SIZE, i * BLOCK_SIZE)
            training_data.append(area)

            if i > 1:
                training_data.append(training_data[i - 1] - area)

        return nan_to_num(training_data)