# 13-08-2025 | 23-05-2026

"""
    Problem:
        Fibonacci sequence for given lenth and with start sequence.

    Args:
        start_sequence (lst[int]) - Starting values.
        length (int) - Length of the sequence.

    Return: 
        lst[int] - Fibo sequence of the given length.
"""

def fibonacci_sequence(start_sequence, length):
    if length <= 0:
        return []

    fibo = start_sequence[:length]

    while len(fibo) < length:
        fibo.append(fibo[-1] + fibo[-2])

    return fibo
