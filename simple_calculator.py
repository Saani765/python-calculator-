from stack import Stack

class SimpleCalculator:
	
    def __init__(self):
        """
        Instantiate any data attributes
        """
        self.history = []

    def evaluate_expression(self, input_expression):
        """
        Evaluate the input expression and return the output as a float
        Return a string "Error" if the expression is invalid
        """
        expression = input_expression.replace(" ", "")  # Remove spaces from the input expression

        if not self.is_valid_expression(expression):
            self.history.append((input_expression, "Error"))
            return "Error"

        operand_stack = Stack()
        operator_stack = Stack()

        for char in expression:
            if char.isdigit():
                operand_stack.push(int(char))
            else:
                operator_stack.push(char)

        operand2 = operand_stack.pop()
        operand1 = operand_stack.pop()
        operator = operator_stack.pop()

        result = self.perform_operation(operand1, operator, operand2)
        self.history.append((input_expression, result))
        return result

    def get_history(self):
        """
        Return history of expressions evaluated as a list of (expression, output) tuples
        The order is such that the most recently evaluated expression appears first
        """
        return self.history

    def is_valid_expression(self, expression):
        """
        Check if the expression is a valid arithmetic expression with 1 operator and 2 operands
        """
        operators = ["+", "-", "*", "/"]
        valid_operator_count = sum(expression.count(op) for op in operators)
        return valid_operator_count == 1 and len(expression.split(operators[0])) == 2

    def perform_operation(self, operand1, operator, operand2):
        """
        Perform the arithmetic operation based on the operator
        """
        if operand1 is None or operand2 is None:
            return "Error"
        if operator == "+":
            return operand1 + operand2
        elif operator == "-":
            return operand1 - operand2
        elif operator == "*":
            return operand1 * operand2
        elif operator == "/":
            if operand2 == 0:
                return "Error"
            return operand1 / operand2



