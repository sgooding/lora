from serial import Serial

class SerialReader:
    def __init__(self, device=None):
        self.device = device
        self.timeout = 5 # seconds
        if self.device is None:
            self.device = '/dev/ttyACM0'

    def open(self):
        # open device
        self.serial = Serial(self.device, timeout=self.timeout)
        self.serial.open()

    def close(self):
        if self.serial.is_open():
            self.serial.close()

    def read(self):
        if self.serial.is_open():
            line = self.serial.readline().decode('utf-8')


