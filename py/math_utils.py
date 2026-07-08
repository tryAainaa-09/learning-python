def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a and b."""
    if b == 0:
        raise ValueError("Denominator cannot be zero.")
    return a / b

def factorial(n):
    """Return the factorial of n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

PI = 3.14159 

class Calculator:
    """A simple calculator class."""
    
    def __init__(self):
        self.history = []

    def calculate(self, operation, a, b):
        """Perform a calculation and store it in history."""
        if operation == 'add':
            result = add(a, b)
        elif operation == 'subtract':
            result = subtract(a, b)
        elif operation == 'multiply':
            result = multiply(a, b)
        elif operation == 'divide':
            result = divide(a, b)
        else:
            raise ValueError("Invalid operation.")
        
        self.history.append((operation, a, b, result))
        return result