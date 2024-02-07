import copy


class PrototypeFactory:
    def __init__(self):
        self._prototypes = {}

    def register_prototype(self, name, prototype):
        self._prototypes[name] = prototype

    def unregister_prototype(self, name):
        del self._prototypes[name]

    def create(self, name, **attrs):
        prototype = self._prototypes.get(name)
        if not prototype:
            raise ValueError(f"No prototype registered for {name}")
        obj = copy.deepcopy(prototype)
        obj.__dict__.update(attrs)
        return obj


class Car:
    def __init__(self):
        self.make = "Toyota"
        self.model = "Camry"
        self.year = 2022

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"


# Example usage:
if __name__ == "__main__":
    car_factory = PrototypeFactory()
    car = Car()
    car_factory.register_prototype("Car", car)

    cloned_car = car_factory.create("Car", year=2023)
    print(cloned_car)  # Output: 2023 Toyota Camry
