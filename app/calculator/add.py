from app.calculator.models import CalculatorOperation


class Addition(CalculatorOperation):

    def perform_operation(self) -> float:
        result = 0.0
        for item in self.get_values():
            result += item[0] + item[1]
        return result
