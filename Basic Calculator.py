# Basic Calculator
# Create a function that takes two numbers and a mathematical operator + - / * and will perform
# a calculation with the given numbers.
#
# Examples
# calculator(2, "+", 2) ➞ 4
# calculator(2, "*", 2) ➞ 4
# calculator(4, "/", 2) ➞ 2
def calculator(num1, operator, num2):
    if "+" in operator:
        return int(num1 + num2)
    if "-" in operator:
        return int(num1 - num2)
    if "*" in operator:
        return int(num1 * num2)
    if "/" in operator:
        return "Can't divide by 0!" if num2 == 0 else int(num1 / num2)


if __name__ == "__main__":
    print(calculator(2, "+", 2))
    print(calculator(2, "*", 2))
    print(calculator(4, "/", 2))
    print(calculator(4, "/", 0))




