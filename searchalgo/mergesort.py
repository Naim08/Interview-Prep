'''
Like QuickSort, Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one. See following C implementation for details.

MergeSort(arr[], l,  r)
If r > l
     1. Find the middle point to divide the array into two halves:
             middle m = (l+r)/2
     2. Call mergeSort for first half:
             Call mergeSort(arr, l, m)
     3. Call mergeSort for second half:
             Call mergeSort(arr, m+1, r)
     4. Merge the two halves sorted in step 2 and 3:
             Call merge(arr, l, m, r)


'''

def MergeSort(arr, left, right):

    if right > left:
        middle = left + ((right - left) // 2)
        MergeSort(arr, left, middle)
        MergeSort(arr, middle + 1, right)
        merge(arr, left, middle + 1, right)

    return arr

def merge(arr, l, m, r):
    left_index = l
    right_index = m

    while left_index <= m and right_index <= r:
        if arr[left_index] > arr[right_index]:
            arr[left_index], arr[right_index] = arr[right_index], arr[left_index]
            left_index += 1
            continue
        else:
            right_index += 1
            continue


    while left_index <= m:
        if arr[left_index] < arr[left_index + 1]:
            arr[left_index], arr[left_index + 1] = arr[left_index + 1], arr[left_index]
            left_index += 1

    while right_index < r:
        if arr[right_index] > arr[right_index + 1]:
            arr[right_index], arr[right_index + 1] = arr[right_index + 1], arr[right_index]
            right_index += 1


    return arr


print(MergeSort([1,50, 10, 6], 0, 4))