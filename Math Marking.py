"""
Given a list of math equations (given as strings), return the percentage of correct answers as a string. Round to the nearest whole number.

Examples
mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10"]) ➞ "75%"

mark_maths(["1-2=-2"]), "0%"

mark_maths(["2+3=5", "4+4=9", "3-1=2"]) ➞ "67%"
Notes
You can expect only addition and subtraction.
Note how there aren't any spaces in any given equation.
"""
def mark_maths(lst):


    target = "="

    original_answers = []
    correct_answers = []

    for math in lst:

        idx = math.find(target)
        original_answers.append(int(math[idx + 1:]))
        correct_answers.append(int(eval(math[:idx])))

    count = 0
    for pair in zip(original_answers, correct_answers):
        if pair[0:1] == pair[1:2]:
            count += 1

    return '{:.0%}'.format(count / len(original_answers))


print(mark_maths(["2+2=4", "3+2=5", "10-3=3", "5+5=10","2+2=4", "3+2=5", "10-3=3", "5+5=10"]))
print(mark_maths(["1-2=-2"]))
print(mark_maths(["2+3=5", "4+4=9", "3-1=2"]))
print((mark_maths(["2+1=1", "2-1=2", "1+2=-2", "2-1=0", "1-2=0", "2+1=2", "2-1=1", "1-2=0", "2+1=1", "1+2=-1", "1+2=1", "1+2=-1", "1-2=-2", "1-1=2", "1+2=-1", "1-1=2", "2-1=0", "1-2=-2", "2+1=-2", "1-1=-1", "1-1=1", "1+2=1", "1-1=2"])))
print(mark_maths(["1+1=-1", "2+1=-2", "2+1=-2", "1-1=-2", "1-2=1", "1-1=-1", "2-2=-2", "2+2=1", "2+1=-2", "1-2=0", "2+1=-2", "2-1=1", "2+2=-1", "1-2=-1", "1-2=0", "1-2=2"]))
