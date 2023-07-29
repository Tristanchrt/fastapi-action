def reverse_string(input_string):
    """Reverse the given string."""
    return input_string[::-1]

def is_prime(number):
    """Check if the given number is prime."""
    if number < 2:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def calculate_factorial(n):
    """Calculate the factorial of a given non-negative integer."""
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

def fibonacci_sequence(n):
    """Generate the Fibonacci sequence up to the nth term."""
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

def is_palindrome(input_string):
    """Check if the given string is a palindrome."""
    return input_string == input_string[::-1]