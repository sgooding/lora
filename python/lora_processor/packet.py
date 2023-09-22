import time

class Packet:
    def __init__(self):
        self.count = 0
    def update(self, count):
        self.count = count
        self.time = time.time()

