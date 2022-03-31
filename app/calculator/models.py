from abc import ABC, abstractmethod
from typing import List, Tuple


class Calculator(ABC):

    def __init__(self, values: List[Tuple[int, int]]):
        """ constructor method"""
        self.__values = values

    @abstractmethod
    def perform_operation(self) -> float:
        raise NotImplementedError("Not implemented")

    @classmethod
    def create(cls, tuple_list: List[Tuple[int, int]]):
        """ factory design pattern to create instances of a calculator"""
        return cls(tuple_list)

    def get_values(self):
        return self.__values
