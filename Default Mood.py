"""
Create a function that takes in a current mood and return a sentence in the
following format: "Today, I am feeling {mood}".
However, if no argument is passed, return "Today, I am feeling neutral".

Examples
mood_today("happy") ➞ "Today, I am feeling happy"
mood_today("sad") ➞ "Today, I am feeling sad"
mood_today() ➞ "Today, I am feeling neutral"
"""
def mood_today(mood="neutral"):

    # return f"Today, I am feeling {mood}"
    return 'Today, I amd feeling {}'.format(mood)

print(mood_today("happy"))
print(mood_today("sad"))
print(mood_today())

