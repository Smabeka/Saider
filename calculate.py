def add(a, b):
    """Add two numbers and return their sum.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of a and b.
    """
    return a + b

def subtract(a, b):
    """Subtract the second number from the first number.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The difference between a and b.
    """
    return a - b

def multiply(a, b):
    """Multiply two numbers and return their product.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The product of a and b.
    """
    return a * b

def divide(a, b):
    """Divide the first number by the second number.

    Args:
        a (float): The numerator.
        b (float): The denominator.

    Raises:
        ValueError: If the denominator is zero.

    Returns:
        float: The quotient of a divided by b.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b