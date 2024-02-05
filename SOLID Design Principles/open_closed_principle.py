from enum import Enum


class Color(Enum):
    red = 1
    blue = 2
    green = 3


class Size(Enum):
    small = 1
    medium = 2
    large = 3


class Product:
    """
    Represents a product with a name, color, and size.

    Attributes:
        name (str): The name of the product.
        color (Color): The color of the product.
        size (Size): The size of the product.
    """

    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


class Specification:
    """
    Base class for product specifications.

    Methods:
        is_satisfied(item): Checks if a product satisfies the specification.
    """

    def is_satisfied(self, item):
        """
        Checks if a product satisfies the specification.

        Args:
            item (Product): The product to be checked.

        Returns:
            bool: True if the product satisfies the specification, False otherwise.
        """
        pass

    def __and__(self, other):
        """
        Creates a new specification that represents the logical AND of two specifications.

        Args:
            other (Specification): The other specification to AND with.

        Returns:
            AndSpecification: The combined specification.
        """
        return AndSpecification(self, other)


class Filter:
    """
    Base class for product filters.

    Methods:
        filter(items, spec): Filters products based on the given specification.
    """

    def filter(self, items, spec):
        """
        Filters products based on the given specification.

        Args:
            items (list): The list of products to be filtered.
            spec (Specification): The specification to filter products.

        Returns:
            list: The filtered list of products.
        """
        pass


class ColorSpecification(Specification):
    """
    Specification for filtering products by color.

    Attributes:
        color (Color): The color to filter by.
    """

    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    """
    Specification for filtering products by size.

    Attributes:
        size (Size): The size to filter by.
    """

    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size


class AndSpecification(Specification):
    """
    Represents the logical AND of two specifications.

    Attributes:
        args (tuple): The specifications to AND together.
    """

    def __init__(self, *args):
        self.args = args

    def is_satisfied(self, item):
        return all(map(lambda spec: spec.is_satisfied(item), self.args))


class BetterFilter(Filter):
    """
    Improved product filter that yields products that satisfy a given specification.

    Methods:
        filter(items, spec): Filters products based on the given specification.

    """

    def filter(self, items, spec):
        """
        Filters products based on the given specification.

        Args:
            items (list): The list of products to be filtered.
            spec (Specification): The specification to filter products.

        Yields:
            Product: The products that satisfy the specification.
        """
        for item in items:
            if spec.is_satisfied(item):
                yield item


if __name__ == '__main__':
    # Example usage and test

    # Creating a list of products
    products = [
        Product("Product1", Color.red, Size.small),
        Product("Product2", Color.blue, Size.medium),
        Product("Product3", Color.green, Size.large),
        Product("Product4", Color.red, Size.medium),
    ]

    # Creating specifications for filtering
    red_color_spec = ColorSpecification(Color.red)
    medium_size_spec = SizeSpecification(Size.medium)

    # Combining specifications using logical AND
    red_and_medium_spec = red_color_spec & medium_size_spec

    # Using the BetterFilter to filter products
    filtered_products = list(BetterFilter().filter(products, red_and_medium_spec))

    # Displaying the filtered products
    print("Filtered Products:")
    for product in filtered_products:
        print(f"- {product.name} (Color: {product.color}, Size: {product.size})")
