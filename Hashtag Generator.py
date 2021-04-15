"""
Create a function that is a Hashtag Generator by using the following rules:

The output must start with a hashtag (#).
Each word in the output must have its first letter capitalized.
If the final result, a single string, is longer than 140 characters, the function should return false.
If either the input (str) or the result is an empty string, the function should return false.
Examples
generate_hashtag("    Hello     World   " ) ➞ "#HelloWorld"

generate_hashtag("") ➞ false, "Expected an empty string to return false"

generate_hashtag("Edabit Is Great") ➞ "#EdabitIsGreat", "Should remove spaces."
"""


def generate_hashtag(txt):

    if txt == "" or txt.isspace():
        return False
    elif len(txt.replace(' ', '')) >= 140:
        return False

    new_capitals = []
    [new_capitals.append(i.title()) for i in txt.split()]
    hash = "#"
    return hash + ''.join(new_capitals)

print(generate_hashtag("    Hello     World   "))
print(generate_hashtag("Edabit Is Great"))
print(generate_hashtag(""))
print(generate_hashtag("" * 100))
print(generate_hashtag("Do We have A Hashtag"))
print(generate_hashtag("Smmmmmmmmmmmmmmmmmmmmmmmmmmmmaaaaaaaaaaaaaaaaaaaaaaaaaaaaalllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll Dog"))
print(generate_hashtag("eda" + " " * 140 + "bit"))
