'''

Given a sorted array arr[] of distinct elements which is rotated at some
unknown point, the task is to find the maximum element in it.
'''


def rotateArray(arr, left, right):
    
    mid = left + (right - left) // 2
    
    if arr[mid - 1] > arr[mid] and arr[mid + 1] < arr[mid]:
        return mid
    elif arr[mid] < arr[left]:
        rotateArray(arr, left, mid)
    elif arr[mid] > arr[left]:
        rotateArray(arr, mid + 1, right)