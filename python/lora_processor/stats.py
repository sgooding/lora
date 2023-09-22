
class Stats:
    def __init__(self):
        self.count = 0
        self.dropped = 0

    def initial_count(self, first_count):
        self.first_count = first_count

    def update(self, count, dropped):
        self.count += (count-self.first_count)
        self.dropped += dropped

    def print(self):
        print(' ~~~ STATS ~~~ \n COUNT   : {}\n DROPPED : {}'.format(self.count, self.dropped))

