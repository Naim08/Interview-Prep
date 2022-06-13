# input: '2xyh1xi'
# output: 'hi'


# Enter your code here. Read input from STDIN. Print output to STDOUT

#CNGUYEN @ HQ.BILL.COM


def decode(s):
    msg = ""
    isSkipped = False
    i = 0
    while i < len(s):
        if isSkipped == True:
            msg += s[i]
            isSkipped = False
            i += 1
        else:
            if s[i].isdigit():
                i = int(s[i]) + i + 1
                isSkipped = True
            else:
                i += 1
                continue

    return msg


print(decode("2xyh1xi5tyreu!"))