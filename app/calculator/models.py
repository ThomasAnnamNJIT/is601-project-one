from abc import ABC, abstractmethod
from typing import List, Tuple


class CalculatorOperation(ABC):

    def __init__(self, values: List[Tuple[int, int]]):
        """ constructor method"""
        self.__values = values

    @abstractmethod
    def perform_operation(self) -> float:
        raise NotImplementedError("Not implemented")

    def get_values(self):
        return self.__values

