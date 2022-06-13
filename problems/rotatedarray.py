'''

An element in a sorted array can be found in O(log n) time via binary search.
But suppose we rotate an ascending order sorted array at some pivot unknown
to you beforehand.
So for instance, 1 2 3 4 5 might become 3 4 5 1 2.
Devise a way to find an element in the rotated array in O(log n) time.

'''


def findElement(arr, num, left, right):
    left = 0
    right = len(arr) - 1
    mid = left + (right - left) // 2
    
    if num > arr[mid]:
    
    
