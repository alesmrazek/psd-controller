#!/usr/bin/python3

import time

class PSD:
    
    """PSD Controller"""

    def __init__(self, P=0.0, S=0.0, D=0.0, sumMax=20, timeSample = 20 ):

        """PSD Initialization"""

        # sum maximum limit
        self.sumMax = sumMax

        self.sample_time = timeSample

        # proportional gain
        self.Kp = P
        # sum gain
        self.Ks = S
        # difference gain
        self.Kd = D

        self.sum = 0

        self.last_time = 0
        self.last_error = 0

        self.reset()

    def Update(self, process_variable):

        error = self.SetPoint - process_variable

        delta_error = error - self.last_error

        time_now = time.time()

        if self.last_time == 0:
            delta_time = 1
        else:
            delta_time = time_now - self.last_time

        self.last_time = time_now

        self.sum += delta_time * (delta_error/2)

        difference = delta_error / delta_time

        if (self.sum < -self.sumMax):
            self.sum = -self.sumMax

        if (self.sum > self.sumMax):
            self.sum = self.sumMax

        output = (self.Kp * error) + (self.Ks * self.sum) + (self.Kd * difference)

        self.last_error = error

        return output

    def setPoint(self, set_point):

        if set_point != self.SetPoint:

            self.sum = 0.0
            self.last_error = 0.0

            self.SetPoint = set_point

    def setTimeSample(self, time_sample):

        """Sample time in ms"""

        self.sample_time = time_sample

    def reset(self):

        """Reset PSD controller"""

        self.SetPoint = 0.0

        self.sum = 0.0

        self.last_time = 0
        self.last_error = 0.0

        self.output = 0.0


