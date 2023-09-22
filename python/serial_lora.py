import serial
import io
import time

from lora_processor.packet import Packet
from lora_processor.stats import Stats

def loop(open_device):
    line = open_device.readline().decode('utf-8')
    if ( len(line) > 0
       and len(line.split("#")) == 2 ):
        count = int(line.split("#")[1].strip())
        packet = Packet()
        packet.update(count)
        return packet
    return None

def main():
    count = None
    dropped = 0
    stats = Stats()
    last_update = 0
    with serial.Serial('/dev/ttyACM0') as ser:
        while ser:
            packet = loop(ser)

            if not packet:
                continue

            if count is None:
                count = packet.count
                stats.initial_count(count)
            else:
                dropped = packet.count - (count + 1)
                count = packet.count
                stats.update(count, dropped)

            if time.time() - last_update > 5.0:
                stats.print()
                last_update = time.time()

if __name__ == '__main__':
    main()
