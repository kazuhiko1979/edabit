"""
Create a function to check if a candidate is qualified in an imaginary coding interview of an imaginary tech startup.

The criteria for a candidate to be qualified in the coding interview is:

The candidate should have complete all the questions.
The maximum time given to complete the interview is 120 minutes.
The maximum time given for very easy questions is 5 minutes each.
The maximum time given for easy questions is 10 minutes each.
The maximum time given for medium questions is 15 minutes each.
The maximum time given for hard questions is 20 minutes each.
If all the above conditions are satisfied, return "qualified", else return "disqualified".

You will be given a list of time taken by a candidate to solve a particular question and the total time taken by the candidate to complete the interview.

Given a list , in a true condition will always be in the format [very easy, very easy, easy, easy, medium, medium, hard, hard].

The maximum time to complete the interview includes a buffer time of 20 minutes.

Examples
interview([5, 5, 10, 10, 15, 15, 20, 20], 120) ➞ "qualified"

interview([2, 3, 8, 6, 5, 12, 10, 18], 64) ➞  "qualified"

interview([5, 5, 10, 10, 25, 15, 20, 20], 120) ➞ "disqualified"
# Exceeded the time limit for a medium question.

interview([5, 5, 10, 10, 15, 15, 20], 120) ➞ "disqualified"
# Did not complete all the questions.

interview([5, 5, 10, 10, 15, 15, 20, 20], 130) ➞ "disqualified"
# Solved all the questions in their respected time limits but exceeded the total time limit of the interview.
"""


key = [5, 5, 10, 10, 15, 15, 20, 20]

def interview(lst, tot):

    # v3
    return ("qualified" if tot <= 120 and len(lst) == 8 and
                           all(v <= key[i] for i, v in enumerate(lst)) else "disqualified")

    # v2
    # key = [5, 5, 10, 10, 15, 15, 20, 20]
    # if tot > 120 or len(lst) < 8:
    #     return "disaqualified"
    # while len(lst) > 0:
    #     if lst.pop() > key.pop():
    #         return "disaqualified"
    # return "qualified"


    # v1
    if len(lst) == len(key) and tot <= 120:
        for i, x in zip(lst, key):
            if i <= x:
                continue
            if i > x:
                return "disqualified"
                break
        return "qualified"
    else:
        return "disqualified"

print(interview([5, 5, 10, 10, 15, 15, 20, 20], 120))
print(interview([2, 3, 8, 6, 5, 12, 10, 18], 64))
print(interview([5, 5, 10, 10, 25, 15, 20, 20], 120))





