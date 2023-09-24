import psycopg2

class PostgresPublisher:

    def __init__(self):
        self.host = ''
        self.is_connected = False

    def connect(self):
        # connect to host
        pass

    def publish(self, packets):

        for packet in packets:
            self.send_packet(packet)

    def send_packet(self, packet):
        # upload
        pass