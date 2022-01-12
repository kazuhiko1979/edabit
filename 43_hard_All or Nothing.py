"""
All or Nothing
Suppose a student can earn 100% on an exam by getting the answers all correct or all incorrect. Given a potentially incomplete answer key and the student's answers, write a function that determines whether or not a student can still score 100%. Incomplete questions are marked with an underscore, "_".

["A", "_", "C", "_", "B"]   # answer key
["A", "D", "C", "E", "B"]   # student's solution

➞ True

# Possible for student to get all questions correct.

["B", "_", "B"]   # answer key
["B", "D", "C"]   # student's solution

➞ False

# First question is correct but third is wrong, so not possible to score 100%.

["T", "_", "F", "F", "F"]   # answer key
["F", "F", "T", "T", "T"]   # student's solution

➞ True

# Possible for student to get all questions incorrect.
Examples
possibly_perfect(["B", "A", "_", "_"], ["B", "A", "C", "C"]) ➞ True

possibly_perfect(["A", "B", "A", "_"], ["B", "A", "C", "C"]) ➞ True

possibly_perfect(["A", "B", "C", "_"], ["B", "A", "C", "C"]) ➞ False

possibly_perfect(["B", "_"], ["C", "A"]) ➞ True

possibly_perfect(["B", "A"], ["C", "A"]) ➞ False

possibly_perfect(["B"], ["B"]) ➞ True
"""

def possibly_perfect(key, answers):


    correct = [k == a for k, a in zip(key, answers)]
    return all(correct) or not any(correct)

    # return len(set(i==j for i, j in zip(key, answers) if i!="_"))==1


    # right, wrong = 0, 0
    #
    # for k, a in zip(key, answers):
    #     if k == a:
    #         right += 1
    #     elif k != a and k != '_':
    #         wrong += 1
    # return right * wrong == 0


    # countTrue = 0
    # countFalse = 0
    #
    # for key, val in zip(key, answers):
    #     if key == val:
    #         countTrue += 1
    #     if key == '_':
    #         countTrue += 1
    #         countFalse += 1
    #     if key != val:
    #         countFalse += 1
    #
    # if len(answers) == abs(countTrue - countFalse) or \
    #         countTrue == len(answers) == countFalse or len(answers) == countTrue:
    #     return True
    # else:
    #     return False


    # return "True: {} False: {}".format(countTrue, countFalse)

print(possibly_perfect(['A', '_', 'C', '_', 'B'], ['A', 'D', 'C', 'E', 'B']))
print(possibly_perfect(['B', '_', 'B'], ['B', 'D', 'C']))
print(possibly_perfect(['T', '_', 'F', 'F', 'F'], ['F', 'F', 'T', 'T', 'T']))
print(possibly_perfect(['B', 'A', '_', '_'], ['B', 'A', 'C', 'C']))
print(possibly_perfect(['A', 'B', 'A', '_'], ['B', 'A', 'C', 'C']))
print(possibly_perfect(['A', 'B', 'C', '_'], ['B', 'A', 'C', 'C']))