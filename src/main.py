"""
Main module for the MLOps Git Exercise project.

This module contains the core functionality of the application.
"""


def main() -> str:
    """
    Main entry point for the application.

    Returns:
        str: A greeting message.
    """
    message = "Hello from MLOps Git Exercise!"
    print(message)
    return message


def add(a: float, b: float) -> float:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        float: The sum of a and b
    """
    return a + b


def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        float: The product of a and b
    """
    return a * b


if __name__ == "__main__":
    main()
