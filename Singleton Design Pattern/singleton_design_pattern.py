class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialization code here
        pass


# Example usage:
if __name__ == "__main__":
    singleton1 = Singleton()
    singleton2 = Singleton()

    print(singleton1 is singleton2)  # Output: True
