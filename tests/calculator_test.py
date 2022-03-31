"""This makes the calculator operation unit test setup"""

from app.calculator.add import Addition
from app.calculator.models import CalculatorOperation
from app.calculator.multiply import Multiplication
from app.calculator.subtract import Subtraction


def test_calculator_adds():
    """Tests that the calculator can add a list of tuples correctly"""
    # Arrange
    addition = Addition([(1, 2), (3, 4)])
    # Act
    result = addition.perform_operation()
    # Assert
    assert result == 10.0


def test_calculator_multiplies():
    """Tests that the calculator can multiply a list of tuples correctly"""
    # Arrange
    multiply = Multiplication([(1, 2), (3, 4)])
    # Act
    result = multiply.perform_operation()
    # Assert
    assert result == 24.0


def test_calculator_subtracts():
    """Tests that the calculator can subtract a list of tuples correctly"""
    # Arrange
    subtraction = Subtraction([(1, 2), (3, 10)])
    # Act
    result = subtraction.perform_operation()
    # Assert
    assert result == 6.0


def test_calculator_factory_pattern():
    """Tests that the factory pattern creates
    any instance of the Calculator class can subtract a list of tuples correctly"""
    # Arrange
    values = [(1, 2), (3, 10)]
    # Act
    subtraction = Subtraction.create(values)
    # Assert
    assert isinstance(subtraction, CalculatorOperation)
    assert isinstance(subtraction, Subtraction)
