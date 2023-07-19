"""Python serial number generator."""

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

    def __init__(self, start =0):
        """Make new generator and start at star"""
        self.start = self.next = start

    def __repr__(self):
        """representation"""
        return f"<SerialGenerator start= {self.start} next = {self.next}>"
    
    def generate(self):
        """return next serial"""
        self.next += 1
        return self.next 
    
    def reset(self):
        """reset number to original"""
        self.next = self.start