class Person:
    def __init__(self):
        self.name = None
        self.age = None
        self.gender = None
        self.address = None

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}, Address: {self.address}"


class PersonBuilder:
    def __init__(self, person=None):
        self.person = person if person else Person()

    def set_name(self, name):
        self.person.name = name
        return self

    def set_age(self, age):
        self.person.age = age
        return self

    def set_gender(self, gender):
        self.person.gender = gender
        return self

    def set_address(self, address):
        self.person.address = address
        return self

    def build(self):
        return self.person


class PersonDirector:
    @staticmethod
    def construct_with_address(name, age, gender, address):
        return PersonBuilder().set_name(name).set_age(age).set_gender(gender).set_address(address).build()

    @staticmethod
    def construct_without_address(name, age, gender):
        return PersonBuilder().set_name(name).set_age(age).set_gender(gender).build()


# Example usage:
if __name__ == "__main__":
    person_with_address = PersonDirector.construct_with_address("Alice", 30, "Female", "123 Street, City")
    print(person_with_address)

    person_without_address = PersonDirector.construct_without_address("Bob", 25, "Male")
    print(person_without_address)
