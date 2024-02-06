from abc import ABC, abstractmethod


class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self):
        pass

    @abstractmethod
    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA(ABC):
    @abstractmethod
    def operation_a(self):
        pass


class ConcreteProductA1(AbstractProductA):
    def operation_a(self):
        return "Operation A1"


class ConcreteProductA2(AbstractProductA):
    def operation_a(self):
        return "Operation A2"


class AbstractProductB(ABC):
    @abstractmethod
    def operation_b(self):
        pass


class ConcreteProductB1(AbstractProductB):
    def operation_b(self):
        return "Operation B1"


class ConcreteProductB2(AbstractProductB):
    def operation_b(self):
        return "Operation B2"


# Example usage:
if __name__ == "__main__":
    factory1 = ConcreteFactory1()
    product_a1 = factory1.create_product_a()
    product_b1 = factory1.create_product_b()
    print(product_a1.operation_a())  # Output: Operation A1
    print(product_b1.operation_b())  # Output: Operation B1

    factory2 = ConcreteFactory2()
    product_a2 = factory2.create_product_a()
    product_b2 = factory2.create_product_b()
    print(product_a2.operation_a())  # Output: Operation A2
    print(product_b2.operation_b())  # Output: Operation B2
