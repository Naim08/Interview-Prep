'''

function binarySearch(arr, num):
    begin = 0
    end = arr.length - 1

    while (begin <= end):
        mid = begin + floor((end-begin)/2)
        if arr[mid] < num:
            begin = mid + 1
        else if arr[mid] == num:
            return mid
        else:
            end = mid - 1

    return -1

'''

def binarySearch(arr, num):
    left = 0
    right = len(arr)

    while left <= right:
        mid = left + int((right - left) / 2)

        if num == arr[mid]:
            return mid
        elif num < arr[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


print(binarySearch([1, 4, 6, 8, 10], 10))
print(binarySearch([1, 4, 6, 8, 10], 8))
print(binarySearch([100, 546, 987, 81232, 1323210], 546))
