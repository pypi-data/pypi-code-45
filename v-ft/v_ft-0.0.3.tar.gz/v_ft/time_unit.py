#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ft times
"""
from featuretools.primitives import TimeSinceLast, TimeSinceFirst, AvgTimeBetween, TimeSince,TimeSincePrevious

class time_unit:
    def __init__(self,unit):
        self.unit = unit
        
        time_unit.time_since_last = TimeSinceLast(unit = self.unit+'s')
        time_unit.time_since_first = TimeSinceFirst(unit = self.unit+'s')
        time_unit.avg_time_between = AvgTimeBetween(unit = self.unit+'s')
        time_unit.time_since = TimeSince(unit = self.unit+'s')
        time_unit.time_since_previous = TimeSincePrevious(unit = self.unit+'s')
