from abc import abstractmethod, ABC


class Pizza(ABC):
    @abstractmethod
    def prepare(self):
        pass


class CheesePizza(Pizza):
    def prepare(self):
        return "Preparing Cheese Pizza"


class PepperoniPizza(Pizza):
    def prepare(self):
        return "Preparing Pepperoni Pizza"


class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return CheesePizza()
        elif pizza_type == "pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type")


# Example usage:
if __name__ == "__main__":
    cheese_pizza = PizzaFactory.create_pizza("cheese")
    print(cheese_pizza.prepare())  # Output: Preparing Cheese Pizza

    pepperoni_pizza = PizzaFactory.create_pizza("pepperoni")
    print(pepperoni_pizza.prepare())  # Output: Preparing Pepperoni Pizza
