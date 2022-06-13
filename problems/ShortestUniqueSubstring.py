'''

Smallest Substring of All Characters
Given an array of unique characters arr and a string str, Implement a function getShortestUniqueSubstring that finds the smallest substring of str containing all the characters in arr. Return "" (empty string) if such a substring doesn’t exist.

Come up with an asymptotically optimal solution and analyze the time and space complexities.

Example:

input:  arr = ['x','y','z'], str = "xyyzyzyx"

output: "zyx"

Test Case #1
Input:

["A"], ""
Expected:

""

Test Case #2
Input: ["A"], "B"
Expected: ""

Test Case #3
Input:

["A"], "A"
Expected:

"A"

test case 4
Input:

["A","B","C"], "ADOBECODEBANCDDD"
Expected:

"BANC"

test case 5
Input:

["A","B","C","E","K","I"], "KADOBECODEBANCDDDEI"
Expected:

"KADOBECODEBANCDDDEI"

test case 6
Input:

["x","y","z"], "xyyzyzyx"
Expected:

"zyx"

test case 7
Input:

["x","y","z","r"], "xyyzyzyx"
Expected:

""
'''


def get_shortest_unique_substring(arr, str):
    unique_counter = [] * 26
    i, j = 0

    for char in str:
        if arr.indexOf(char):

    pass  # your code goes here