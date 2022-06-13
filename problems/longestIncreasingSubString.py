'''

'abc' => 'c'
(valid: 'ac', 'b', 'abc', ...)
(invalid: 'cba', 'zzz', 'cc', ...)

'cba' => 'cba'
'ccc' => 'ccc'
'cab' => 'cb'
'dacaba' => 'dcba'

abc => cba

'ac' < 'bc < 'c'

output = ''
loop str(cba):

addaacba
    ^^

buffer: dda
expected output: ccba

worst
case: O(n * m)

'''


# Enter your code here. Read input from STDIN. Print output to STDOUT

def longestIncreasingString(s):
    buff = ""

    for i in range(len(s)):
        if ord(s[i]) >= ord(s[i+1]):
            buff += s[i]
        else:
            j = len(buff)
            while j != -1:
                if ord(buff[j]) >= ord(s[i+1]):
                    buff = buff[0:j]
                    buff += s[i + 1]
                j = j - 1

    return buff
