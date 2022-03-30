from app.calculator.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__("Car")

    def num_of_wheels(self) -> int:
        return 4


if __name__ == "__main__":
    vehicle = Car()
    print(vehicle.get_name())
