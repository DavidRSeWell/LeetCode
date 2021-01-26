"""
No claims of optimality for this implementation but it is an implementation
"""


def swap(array, l, r):
    array_new = array
    nl, nr, nr1 = array[l], array[r], array[r - 1]
    array_new[r] = nl
    array_new[l] = nr1
    array_new[r - 1] = nr
    return array_new


def quicksort(array, l, r):
    pivotr = r
    pivotl = l

    while l < r:
        if array[r] < array[l]:
            array = swap(array, l, r)
            r -= 1
        else:
            l += 1

    if r > 0:
        array = quicksort(array, pivotl, r - 1)
    if r < pivotr:
        array = quicksort(array, r, pivotr)
    return array


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
arrays = quicksort(test, 0, len(test) - 1)

print("Final array")
print(arrays)