class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


class ElectricVehicle:
    def __init__(self, battery_capacity, battery_life):
        self.battery_capacity = battery_capacity
        self.battery_life = battery_life

    def get_range(self):
        range = self.battery_capacity / self.battery_life
        print(f"Range: {range}")


class GasolineVehicle:
    def __init__(self, fuel_capacity, mpg):
        self.fuel_capacity = fuel_capacity
        self.mpg = mpg

    def get_mpg(self):
        return self.fuel_capacity * self.mpg


class HybridVehicle(Vehicle, ElectricVehicle, GasolineVehicle):
    def __init__(
        self,
        make,
        model,
        year,
        battery_capacity,
        battery_life,
        fuel_capacity,
        mpg,
    ):
        Vehicle.__init__(self, make, model, year)
        ElectricVehicle.__init__(self, battery_capacity, battery_life)
        GasolineVehicle.__init__(self, fuel_capacity, mpg)


my_car = HybridVehicle("Toyota", "Hilux", 2024, 5, 2, 20, 3)
print(my_car.battery_capacity)
