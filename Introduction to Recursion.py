def factorial(num):
    if num == 1:
        return num
    return num * factorial(num - 1)


print(factorial(5))
print(factorial(3))
print(factorial(2))
print(factorial(1))



