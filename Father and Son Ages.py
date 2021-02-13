"""
Create a function that takes two arguments: a father's current age f_age and his son's current age s_age. Сalculate how many years ago the father was twice as old as his son, or in how many years he will be twice as old.

Examples
age_difference(36, 7) ➞ 22
# 22 years from now, the father will be 58 years old and his son will be 29 years old.
age_difference(55, 30) ➞ 5
# 5 years ago, the father was 50 years old and his son was 25 years old.
age_difference(42, 21) ➞ 0
"""
def age_difference(f_age, s_age):

    # 36 - 7 = 29
    dif = f_age - s_age

    # 29 * 2 = 58
    dif = dif * 2

    # 58 - 36 = 22
    dif = dif - f_age

    return abs(dif)

print(age_difference(36, 7))
print(age_difference(55, 30))
print(age_difference(42, 21))