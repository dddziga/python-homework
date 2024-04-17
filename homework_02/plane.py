"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
import homework_02.exceptions as exceptions

class Plane(Vehicle):
    def __init__(self, weight: int = 0, fuel: int = 0, fuel_consumption: int = 0, max_cargo: int = 0):
        super().__init__(weight, fuel, fuel_consumption, max_cargo)
        self.max_cargo = max_cargo
        self.cargo = 0

    def load_cargo(self, load: int):
        new_cardo = load + self.cargo
        if new_cardo <= self.max_cargo:
            self.cargo = new_cardo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0
        return current_cargo