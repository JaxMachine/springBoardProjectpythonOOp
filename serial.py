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
    def __init__(self, start =0) -> None:
        """Intializer for the Class"""

        #Hold Start number and nex number in different variables to account for reset
        self.start = self.next = start

    def __repr__(self):
        """Show Representation"""
        return f"<SerialGenerator start={self.start} next={self.next}>"

    def generate(self):
        "Return next serial number"
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Reset to Orginal Start Number"""

        self.next = self.start