from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, name):
        self.__name = name

    @abstractmethod
    def num_of_wheels(self) -> int:
        raise NotImplementedError("Not implemented")

    def get_name(self):
        return self.__name
