"""
Write a function that adds two numbers. The catch, however, is that the numbers will be strings.

Examples
add_str_nums("4", "5") ➞ "9"

add_str_nums("abcdefg", "3") ➞ "-1"

add_str_nums("1", "") ➞ "1"

add_str_nums("1874682736267235927359283579235789257", "32652983572985729") ➞ "1874682736267235927391936562808774986"
Notes
If there are any non-numerical characters, return "-1".
An empty parameter should be treated as "0".
Python supports the addition of integers without limit, try this challenge without using this functionality.
Your function doesn't have to add negative numbers.
Zeros at the beginning of the string should be trimmed.
"""

def add_str_nums(num1, num2):

    if num1 == "":
        num1 = '0'

    if num2 == "":
        num2 = '0'

    try:
        return str(int(num1) + int(num2))
    except ValueError:
        return "-1"

print(add_str_nums("4", "5"))
print(add_str_nums("abcdefg", "3"))
print(add_str_nums("1", ""))
print(add_str_nums("1874682736267235927359283579235789257", "32652983572985729"))
print(add_str_nums("", ""))