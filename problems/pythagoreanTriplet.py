'''

Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

Input: arr[] = {3, 1, 4, 6, 5}
Output: True
There is a Pythagorean triplet (3, 4, 5).

Input: arr[] = {10, 4, 6, 12, 5}
Output: False
There is no Pythagorean triplet.


'''

def binarySearch(arr: list, num: int) -> int:
    return

def isTriplet(arr: list) -> bool:
    arr.sort()

    # Square all array values
    arr = [i*i for i in arr]
    l = 0
    while l < len(arr) - 1:
        return


    return True


isTriplet([3, 1, 4, 6, 5])