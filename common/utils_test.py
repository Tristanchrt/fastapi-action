import utils

def test_reverse_string():
    assert utils.reverse_string("Hello, World!") == "!dlroW ,olleH"

def test_is_prime():
    assert utils.is_prime(13) is True
    assert utils.is_prime(27) is False

def test_calculate_factorial():
    assert utils.calculate_factorial(5) == 120

def test_fibonacci_sequence():
    assert utils.fibonacci_sequence(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def test_is_palindrome():
    assert utils.is_palindrome("racecar") is True
    assert utils.is_palindrome("hello") is False
