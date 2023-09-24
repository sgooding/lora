from serial import Serial
from lora_processor.packet import Packet

class SerialReader:
    def __init__(self, device=None):
        self.device = device
        self.timeout = 5 # seconds
        self.is_connected = False

        self.rssi = None
        self.message = None
        self.packet = None

        if self.device is None:
            self.device = '/dev/ttyACM0'

    def connect(self):
        self.open()
        self.is_connected = True

    def open(self):
        # open device
        self.serial = Serial(self.device, timeout=self.timeout)
        self.serial.open()

    def close(self):
        if self.serial.is_open():
            self.serial.close()

    def read(self):
        packets = []
        if self.serial.is_open():
            line = self.serial.readline().decode('utf-8')
            packet = self.process_line(line)
            packets.append(packet)
        return packets

    def process_line(self, line):
        # filter everything out except a packet
        line = line.decode('utf-8')
        if line.find('RSSI:') == 0:
            self.rssi = int(line.split(':')[1].strip())
        if line.find('#') > 0:
            self.message = line

        if( self.rssi is not None
            and self.message is not None ):
            self.packet = Packet()
            self.packet.update(self.rssi, self.message)
            self.rssi = None
            self.message =None

        if self.packet is not None:
            return self.packet

