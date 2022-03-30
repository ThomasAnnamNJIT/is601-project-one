from app.calculator.models import CalculatorOperation


class Multiplication(CalculatorOperation):

    def perform_operation(self) -> float:
        result = 1.0
        for value in self.get_values():
            result *= value[1]*value[0]
        return result
