# this code repackages some fundamental math operators into new functions that will return the result as a floating point number.
#calculator/calculations.py

"""Provide several math calculations.
This module allows the user to make mathematical calculations.
Examples:
    >>> from calculator import calculations
    >>> calculations.add(2, 4)
    6.0
    >>> calculations.multiply(2.0, 4.0)
    8.0
    >>> from calculator.calculations import divide
    >>> divide(4.0, 2)
    2.0

the module contains the following functions:
- 'add(a, b)' - Returns the sum of two numbers.
- 'subtract(a, b)' - Returns the difference of two numbers.
- 'multiply(a, b)' - Returns the product of two numbers.
- 'divide(a, b)' - Returns the quotient of two numbers,
"""

from typing import Union

def add(a: Union[float, int],  b: Union[float, int]) -> float:
    """Compute and return the sum of two numbers.

    Examples:
        >>> add(4.0, 2.0)
        6.0
        >>> add(4, 2)
        6.0


    Args:
        a (float): A number representing the first addend in the addition.
        b (float): A number representing the second addend in the addition.


    Returns:
        float: A number representiong the arithmetic sum of 'a' and 'b'    

    """
    return float(a + b)

def subtract(a: Union[float, int],  b: Union[float, int]) -> float:
    """Calculate the difference of two numbers.

    Examples:
        >>> subtract(4.0, 2.0)
        2.0
        >>> subtract(4, 2)
        2.0

    Args:
        a (float): A number representing the minuend in the subtraction.
        a (float): A number representing the subtrahend in the subtraction.

    Returns:
        float: A number representing the difference between 'a' and 'b'.      
    """
    return float(a - b)

def multiply(a: Union[float, int],  b: Union[float, int]) -> float:
    """Compute and return the product of two numbers.

    Examples:
        >>> multiply(4.0, 2.0)
        8.0
        >>> multiply(4, 2)
        8.0

    Args:
        a (float): A number representing the multiplicand in the multiplication.
        b (float): A number representing the multiplier in the multiplication.

    Returns:
        float: A number representing the product of 'a' and 'b'. 

    """
    return float(a * b)

def divide(a: Union[float, int],  b: Union[float, int]) -> float:
    """Compute and return the quotient of two numbers.

    Examples:
        >>> divide(4.0, 2.0)
        2.0
        >>> divide(4, 2)
        2.0
        >>> divide(4, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: division by zero

    Args:
        a (float): A number representing the dividend in the division.
        b (float): A number representing the divisor in the division.

    Returns:
        float: A number representing the quotient of 'a' and 'b'.

    Raises:
        ZeroDivisionError: An error occurs when divior is '0'. 

    """
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return float(a / b)
