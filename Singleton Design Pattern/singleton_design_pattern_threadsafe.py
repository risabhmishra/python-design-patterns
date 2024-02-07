import threading


class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialization code here
        pass


# Example usage:
if __name__ == "__main__":
    singleton1 = ThreadSafeSingleton()
    singleton2 = ThreadSafeSingleton()

    print(singleton1 is singleton2)  # Output: True
