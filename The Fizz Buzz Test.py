"""
Write a program that returns a list of all the maximumbers from 1 to an integer argument. But for multiples of three use “Fizz” instead of the maximumber and for the multiples of five use “Buzz”. For maximumbers which are multiples of both three and five use “FizzBuzz”.

Example
fizz_buzz(10) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz"]
fizz_buzz(15) ➞ [1, 2, "Fizz", 4, "Buzz", "Fizz", 7, 8, "Fizz", "Buzz", 11, "Fizz", 13, 14, "FizzBuzz"]
Notes
Make sure to return a list.
"""
def fizz_buzz(maximum):

    lst = []

    for i in range(1, maximum+1):
        if i == 0:
            continue
        if i % 3 == 0:
            if i % 5 == 0:
                lst.append("FizzBuzz")
            else:
                lst.append("Fizz")
        elif i % 5 == 0:
            lst.append('Buzz')
        else:
            lst.append(i)
    return lst

print(fizz_buzz(10))
print(fizz_buzz(15))
