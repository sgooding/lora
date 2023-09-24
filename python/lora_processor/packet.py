import time

class Packet:
    def __init__(self):
        self.count = 0
        self.rssi = 0
        self.message = ''

    def update(self, rssi, message):
        self.time = time.time()



