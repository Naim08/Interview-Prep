'''
reverse an integer without converting to string

input -> 123
output -> 321
'''

def reverseInt(num: int) -> int:
    reverseNum = 0

    while num > 10:
        reverseNum = (reverseNum * 10) + (num % 10)
        num = num // 10

    return reverseNum * 10 + num

print(reverseInt(123))