'''
Given a string, that contains special character together with alphabets (‘a’ to ‘z’ and ‘A’ to ‘Z’), reverse the string in a way that special characters are not affected.


Input:   str = "a,b$c"
Output:  str = "c,b$a"
Note that $ and , are not moved anywhere.
Only subsequence "abc" is reversed

Input:   str = "Ab,c,de!$"
Output:  str = "ed,c,bA!$"

'''
import logging


def isLetter(c: str) -> str:
    return c.isalpha()


def reverse(s: str) -> str:

    s = list(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if not isLetter(s[i]):
            i = i + 1

        elif not isLetter(s[j]):
            j = j - 1
        else:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            i = i + 1
            j = j - 1

    s = "".join(s)
    return s


print(reverse("ab^asasc"))

'''
Solution: time complexity O(n)
'''
