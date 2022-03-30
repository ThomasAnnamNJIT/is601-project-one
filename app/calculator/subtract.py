from app.calculator.models import CalculatorOperation


class Subtraction(CalculatorOperation):

    def perform_operation(self) -> float:
        result = 0.0
        for item in self.get_values():
            result = item[1] - item[0] - result
        return result
