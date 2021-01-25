"""
Create a function that takes a string and returns
the number (count) of vowels contained within it.

Examples
count_vowels("Celebration") ➞ 5
count_vowels("Palm") ➞ 1
count_vowels("Prediction") ➞ 4
"""
def count_vowels(txt) -> int:
    v = 'aeiuo'
    return sum(txt.count(vow) for vow in v)

    # v = 'aeiou'
    # c = 0
    # for vow in v:
    #     c += txt.count(vow)
    # return c


print(count_vowels("Celebration"))
print(count_vowels("Palm"))
print(count_vowels("Prediction"))