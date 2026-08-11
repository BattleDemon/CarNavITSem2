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

        self.speed = None

        # Set a refrence to the gps's serial data
        self.ser = serial.Serial(self.port, baudrate=9600, timeout=0.5)

        # Create thread for gps location update
        self.update_thread = _thread.start_new_thread(self._update)

    def _update(self):  # _ for internal function, loop to update gps location
        while True:
            rawdata = self.ser.readline()

            # Check if the raw data is the correct type
            # $GNRMC gives longitude, latitude, speed (in Knots), UTC time, and date
            if rawdata[0:5] == "$GNRMC":
                # Parse rawdate into usable data
                data = pynmea2.parse(rawdata)

                # Set local refrence to needed data
                lat = data.latitude
                lng = data.longitude

                speed = data.spd_over_grnd

                # Set class data
                self._set_location_speed(lat, lng, speed)

    def get_location(self):  # Called by other files when needed to get location
        return [self.lat, self.lng]

    # Set location in class
    def _set_location_speed(self, lat, lng, speed):
        self.lat = lat
        self.lng = lng
        self.speed = speed
