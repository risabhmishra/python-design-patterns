import copy


class Prototype:
    def __init__(self):
        self._objects = {}

    def register_object(self, name, obj):
        self._objects[name] = obj

    def unregister_object(self, name):
        del self._objects[name]

    def clone(self, name, **attrs):
        obj = copy.deepcopy(self._objects.get(name))
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
    car_prototype = Prototype()
    car = Car()
    car_prototype.register_object("Car", car)

    cloned_car = car_prototype.clone("Car", year=2023)
    print(cloned_car)  # Output: 2023 Toyota Camry
