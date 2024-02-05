from abc import ABC, abstractmethod


# Abstraction (High-level module)
class Worker(ABC):
    @abstractmethod
    def work(self):
        pass


# Low-level module implementing the abstraction
class Robot(Worker):
    def work(self):
        print("Robot is working")


# Another low-level module implementing the abstraction
class Human(Worker):
    def work(self):
        print("Human is working")


# High-level module depending on abstractions
class Manager:
    def __init__(self, worker: Worker):
        self.worker = worker

    def manage(self):
        print("Manager is managing:")
        self.worker.work()


# Dependency injection
if __name__ == '__main__':
    # Injecting a Robot into the Manager
    robot_worker = Robot()
    manager_robot = Manager(robot_worker)
    manager_robot.manage()

    # Injecting a Human into the Manager
    human_worker = Human()
    manager_human = Manager(human_worker)
    manager_human.manage()
