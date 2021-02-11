"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


def isPalindrome_silly(x: int) -> bool:
    """
    Clean and pythonic but not in the spirit of the question
    :param x:
    :return:
    """
    if x < 0:
        return False

    xl = list(str(x))

    if xl == xl[::-1]:
        return True
    else:
        return False