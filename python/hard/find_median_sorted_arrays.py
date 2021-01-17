from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    m = len(nums1)
    n = len(nums2)

    mn = (m + n)

    med_idx = int(mn / 2)

    comb, other = nums1, nums2

    if n > m:
        comb, other = nums2, nums1

    if (m == 0) or (n == 0):

        if (mn % 2) == 0:
            return (comb[med_idx - 1] + comb[med_idx]) / 2.0
        else:
            return comb[med_idx]

    index1 = 0
    while (index1 <= med_idx):
        if (index1 >= len(comb)) or (len(other) == 0):
            comb = comb + other
            break
        n1 = comb[index1]
        n2 = other[0]

        if n1 > n2:
            comb.insert(index1, n2)
            other.pop(0)

        index1 += 1

    if (mn % 2) == 0:
        return (comb[med_idx - 1] + comb[med_idx]) / 2.0
    else:
        return comb[med_idx]


if __name__ == "__main__":
    tests = [([1,3],
            [2]),
             ([1,2],
            [3,4]),
             ([0,0],
            [0,0]),
             ([],
            [1]),
             ([2],
            []),
             ([100001],
            [100000])]
    for test in tests:
        print(findMedianSortedArrays(test[0],test[1]))