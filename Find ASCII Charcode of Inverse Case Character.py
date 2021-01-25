"""
Create a function that takes a single character as an argument and returns the char code of its lowercased / uppercased counterpart.
Examples
Given that:
  - "A" char code is: 65
  - "a" char code is: 97
counterpartCharCode("A") ➞ 97
counterpartCharCode("a") ➞ 65
"""
def counterpartCharCode(char) -> int:

    # if char.islower():
    #     char = char.upper()
    #     return ord(char)
    #
    # elif char.isupper():
    #     char = char.lower()
    #     return ord(char)
    #
    # else:
    #     return ord(char)

    char = char.swapcase()
    return ord(char)

print(counterpartCharCode("A"))
print(counterpartCharCode("a"))
print(counterpartCharCode("$"))