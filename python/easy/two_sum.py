"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    h = {}
    for i, num in enumerate(nums):
        c = target - num
        if c in h:
            return [h[c], i]
        else:
            h[num] = i


if __name__ == "__main__":
    tests = [([2,7,11,15],9),([3,2,4],6),([3,3],6)]
    for test in tests:
        print(twoSum(test[0],test[1]))