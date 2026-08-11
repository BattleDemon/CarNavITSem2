import serial
import pynmea2
import _thread

# location of gps port
GPS_PORT = "/dev/ttyAMA0"


# GPS manager class
class GPSManager:
    def __init__(self):
        self.port = GPS_PORT
        self.lat = None
        self.lng = None

        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        # Create thread for gps location update
        self.update_thread = _thread.start_new_thread(self._update)

    def _update(self):  # _ for internal function, loop to update gps location
        while True:
            rawdata = self.ser.readline()

            if (
                rawdata[0:6] == "$GPRMC"
            ):  # Filter for only GPS message containing location, time, velocity
                data = pynmea2.parse(rawdata)

                lat = data.latitude
                lng = data.longitude

                self._set_location(lat, lng)  # Update internal position

    def get_location(self):  # Called by other files when needed to get location
        return [self.lat, self.lng]

    def _set_location(self, lat, lng):  # Internal set lat and lng
        self.lat = lat
        self.lgn = lng
