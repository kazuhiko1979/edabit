"""
Given a number, find the "round" of each digit of the number. An integer is called "round" if all its digits except the leftmost (most significant) are equal to zero.

Round numbers: 4000, 1, 9, 800, 90
Not round numbers: 110, 707, 222, 1001
Create a function that takes a number and returns the "round" of each digit (except if the digit is zero) as a string. Check out the following examples for more clarification.

Examples
sum_round(101) ➞ "1 100"

sum_round(1234) ➞ "4 30 200 1000"

sum_round(54210) ➞ "10 200 4000 50000"
"""
def sum_round(num):

    tmp = ""
    list_val = [tmp.zfill(int(key)) for key, val in enumerate(str(num), 1)]

    num = list(str(num)[::-1])

    tmp = [key.replace(key[0], val, 1) for key, val in zip(list_val, num)]
    tmp = [i for i in tmp if i[0] != '0']

    return ' '.join(tmp)

print(sum_round(101))
print(sum_round(54210))
print(sum_round(1234))
