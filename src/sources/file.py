import logging

class InputDataCorrupted(Exception):
    pass

class Source:
    def __init__(self, address):
        self.address=address
        self.handleds_address = f'{self.address}_handleds'
        with open(self.address, 'r') as f:
            self.input_log = [x.strip('\n') for x in f.readlines()]
        self.handleds_log = self._get_or_make()

    def next(self):
        try:
            target = self.handleds_log[-1]
        except IndexError:
            return self.input_log[0]

        i = 0
        try:
            while self.input_log[i] != target:
                i+= 1
        except IndexError:
            logging.error('input log is corrupted as target could not be found')
            raise InputDataCorrupted

        try:
            return self.input_log[i+1]
        except IndexError:
            logging.info('all caught up')
            return ''

    def _get_or_make(self):
        try:
            with open(self.handleds_address, 'r') as f:
                return f.readlines()
        except FileNotFoundError:
            open(self.handleds_address, 'w').close()
            return self._get_or_make()

    def update_handleds(self, line):
        self.handleds_log.append(line)

    def commit(self):
        with open(self.handleds_address, 'a') as f:
            f.writelines([x+'\n' for x in self.handleds_log])



