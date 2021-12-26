from abc import ABC, abstractmethod


class Strategy(ABC):

    @abstractmethod
    def do(self, value: str):
        pass


class Car:

    def __init__(self, strategy: "Strategy") -> None:
        self.__strategy = strategy

    @property
    def strategy(self):
        return self.__strategy

    @strategy.setter
    def strategy(self, strategy: "Strategy") -> None:
        self.__strategy = strategy

    def process(self) -> None:
        self.strategy.do(f"Hello from {self.strategy.__class__.__name__!r}.do()")


class BMW(Strategy):

    def do(self, value: str) -> None:
        print(value)


class Mercedes(Strategy):

    def do(self, value: str) -> None:
        print(value)


# Initialize instance of Car with strategy 'BMW'
x = Car(BMW())

x.process()  # Hello from 'BMW'. do()

# Change strategy to 'Mercedes'
x.strategy = Mercedes()
x.process()  # Hello from 'Mercedes'.do()

# Change strategy to 'BMW'
x.strategy = BMW()
x.process()  # Hello from 'BMW'.do()
