class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """ Creates a SerialGenerator with start counter """
        self.start = start
        self.counter = start

    def generate(self):
        """ Return the next sequential number based on start attribute """
        curr_val = self.counter
        self.counter += 1
        return curr_val

    def reset(self):
        """ Reset the number back to original start and returns None """
        self.counter = self.start
