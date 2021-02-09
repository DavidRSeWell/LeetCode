"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x
causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""

# Most relevant for python?
def reverse(x: int) -> int:

    INT_MAX = 2 ** 31 - 1        # 2 ** 31 - 1 = 2147483647
    INT_MIN = -2 ** 31           # -2 ** 31    = -2147483648
    INT_MIN_REV = -8463847412    # Reverse of INT_MIN

    # Handle the special case where x is exactly the reverse of INT_MIN
    if x == INT_MIN_REV:
        return INT_MIN

    # Assume that x is a positive integer to avoid special cases
    remainder = abs(x)
    result = 0

    # Pop each digit, check for overflow, and build reversed result
    while remainder:
        remainder, digit = divmod(remainder, 10)
        if result > INT_MAX // 10 or result == INT_MAX // 10 and digit > 7:
            return 0
        result = digit + result * 10

    # Convert result to a negative number, if input is negative
    if x < 0:
        result = -result

    return result

# Bad for current problem but more pythonic
def convert(x):
    try:
        x = int(x)
        if (x <= -2**31) or (x >= 2**31 -1):
            return 0
    except:
        return 0
    return x

class Solution:
    def reverse(self, x: int) -> int:
        s_x = str(x)[::-1]
        if x < 0:
            s_x = "-" + s_x[:-1]
        return convert(s_x)


if __name__ == "__main__":

    tests = [
        (123,321),
        (-123,-321),
        (0,0),
        (2**32,0)
    ]

    print("Running tests")

    for test,ans in tests:
        assert reverse(test) == ans

    print("Passed all tests")