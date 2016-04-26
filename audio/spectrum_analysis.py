#!/usr/bin/python

import matplotlib.pyplot as pyplot

from scipy.integrate import simps
from numpy import trapz

BLOCK_SIZE = 1000

class Spectrum():

    def __init__(self, raw_data, category):
        self.category = category
        self.xvalues, self.yvalues = self.parse_data(raw_data)


    def parse_data(self, raw_data):
        xvalues = []
        yvalues = []

        count = 0
        while count < len(raw_data):
            frequency = float(raw_data[count])
            level = float(raw_data[count + 1])

            xvalues.append(frequency)
            yvalues.append(level)

            count += 2

        pyplot.plot(xvalues, yvalues)
        pyplot.show()
        return xvalues, yvalues


    def get_area(self, min, max):
        values = []

        for i in range(0, len(self.xvalues)):
            if self.xvalues[i] > min and self.xvalues[i] < max:
                values.append(self.yvalues[i])

        # Compute the area using the composite trapezoidal rule.
        trapz_area = trapz(values, dx=BLOCK_SIZE)

        # Compute the area using the composite Simpson's rule.
        simps_area = simps(values, dx=BLOCK_SIZE)
        return [ trapz_area, simps_area ]

    def training_data(self):
        training_data = []

        max_value = int(max(self.xvalues)/BLOCK_SIZE + 1)

        for i in range(1, max_value):
            areas = self.get_area(i - 1 * BLOCK_SIZE, i * BLOCK_SIZE)
            training_data.extend(areas)

        return training_data