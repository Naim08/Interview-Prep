'''

Given an array of integers of size ‘n’.
Our aim is to calculate the maximum sum of ‘k’
consecutive elements in the array.

Input  : arr[] = {100, 200, 300, 400}
         k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}
         k = 4
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23}
of size 4.

Input  : arr[] = {2, 3}
         k = 3
Output : Invalid
There is no subarray of size 3 as size of whole
array is 2.

'''

from functools import reduce


def bruteForce(arr: list, k: int) -> int:
    if len(arr) < k:
        return -1

    arr.sort(reverse=True)

    return reduce(lambda x, y: x + y, arr[:k])


def optimial(arr: list, k: int) -> int:


    return

a = [4, 5, 6, 3]

print (bruteForce(a, 3))
