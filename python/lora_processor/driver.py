from lora_processor.serial_reader import SerialReader
from lora_processor.postgres_publisher import PostgresPublisher

class Driver:
    def __init__(self):
        self.serial_reader = SerialReader()
        self.postgres = PostgresPublisher()

    def setup(self):
        pass

    def run(self):

        while True:
            # 1. check if serial is connected
            if not self.serial_reader.is_connected:
                # try to connect
                self.serial_reader.connect()
                continue
            
            if not self.postgres.is_connected:
                self.postgres.connect()
                continue

            packets = self.serial_reader.read()

            if len(packets) > 0:
                self.postgres.publish(packets)

