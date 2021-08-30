import math


def recursiveDigitsAddedHelper_toDigitOne(total):

    if total < 10:
        return total

    if total > 100:
        return total + recursiveDigitsAdded(total)

    return total + recursiveDigitsAddedHelper_toDigitOne(math.floor(total / 10) + math.floor(total % 10))


def recursiveDigitsAddedHelper(digit, sub_total, total):

    if digit < 10:
        total = digit + sub_total
        return recursiveDigitsAddedHelper_toDigitOne(total)

    return recursiveDigitsAddedHelper(math.floor(digit / 10), sub_total + digit % 10, total)


def recursiveDigitsAdded(digit):

    return recursiveDigitsAddedHelper(digit, 0, 0)

print(recursiveDigitsAdded(5))
print(recursiveDigitsAdded(8))
print(recursiveDigitsAdded(98))
print(recursiveDigitsAdded(3528))
print(recursiveDigitsAdded(5462))
print(recursiveDigitsAdded(3528))
print(recursiveDigitsAdded(99999999999884))

