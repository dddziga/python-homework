"""
Объявите следующие исключения:
- LowFuelError
- NotEnoughFuel
- CargoOverload
"""
class LowFuelError(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'LowFuelError, {0}'.format(self.message)
        else:
            return 'Low fuel'

class NotEnoughFuel(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'NotEnoughFuel, {0}'.format(self.message)
        else:
            return 'Not enough fuel'

class CargoOverload(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None

    def __str__(self):
        if self.message:
            return 'CargoOverload, {0}'.format(self.message)
        else:
            return 'Cargo over load'