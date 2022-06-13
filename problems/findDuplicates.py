'''

Find The Duplicates
Given two sorted arrays arr1 and arr2 of passport numbers, implement a function findDuplicates that returns an array of all passport numbers that are both in arr1 and arr2. Note that the output array should be sorted in an ascending order.

Let N and M be the lengths of arr1 and arr2, respectively. Solve for two cases and analyze the time & space complexities of your solutions: M ≈ N - the array lengths are approximately the same M ≫ N - arr2 is much bigger than arr1.

Example:
input:  arr1 = [1, 2, 3, 5, 6, 7], arr2 = [3, 6, 7, 8, 20]

output: [3, 6, 7] # since only these three values are both in arr1 and arr2

'''

def find_duplicates(arr1, arr2):
    sm_arr = arr2 if len(arr1) > len(arr2) else arr1
    lg_arr = arr1 if len(arr1) > len(arr2) else arr2

    sm_i = 0
    lg_i = 0
    duplicateContainer = []
    while sm_i < len(sm_arr) and lg_i < len(lg_arr):
        if sm_arr[sm_i] == lg_arr[lg_i]:
            duplicateContainer.append(sm_arr[sm_i])
            sm_i += 1
            lg_i += 1
        elif sm_arr[sm_i] > lg_arr[lg_i]:
            lg_i += 1
        elif sm_arr[sm_i] < lg_arr[lg_i]:
            sm_i += 1

    return duplicateContainer

assert find_duplicates([1, 2, 3, 5, 6, 7], [3, 6, 7, 8, 20]) == [3, 6, 7]
assert find_duplicates([10,20,30,40,50,60,70], [10,20,30,40,50,60,70]) == [10, 20, 30, 40, 50, 60, 70]