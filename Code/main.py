# External import

import pyosm
import pynmea2
import pandas
import numpy
import pandarm
import PyQt5

# Interal imports

from gps.gps import GPSManager


class CarNavApp:
    def __init__(self):
        self.GPSManager = GPSManager()
        self.lot_lng_speed = [0, 0, 0]

    def _update(self):
        self.lot_lng_speed = self.GPSManager.get_location_speed()
