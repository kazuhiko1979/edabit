"""
A word nest is created by taking a starting word, and generating a new string by placing the word inside itself. This process is then repeated.

Nesting 3 times with the word "incredible":

start  = incredible
first  = incre(incredible)dible
second = increin(incredible)credibledible
third  = increinincr(incredible)ediblecredibledible
The final nest is increinincrincredibleediblecredibledible (depth = 3)

Valid word nests can always be collapsed to show the starting word, by reversing the process above:

word = "incredible"
nest = "increinincrincredibleediblecredibledible"

Steps:
=> "increinincrincredibleediblecredibledible" # starting nest
=> "increinincr(incredible)ediblecredibledible" # find word in nest
=> "increinincr            ediblecredibledible" # remove word
=> "increinincrediblecredibledible" # join remaining halves
=> "increin(incredible)credibledible" # find word in nest...

... repeat steps until single word remains

=> "incredible" (return True as "incredible" = word)
When invalid word nests are collapsed, the starting word isn't found:

word = "spring"
nest = "sprspspspringringringg"

Steps:
=> "sprspspspringringringg" # starting nest
=> "sprspsp(spring)ringringg" # find word in nest
=> "sprspsp        ringringg" # remove word
=> "sprspspringringg" # join remaining halves
=> "sprsp(spring)ringg" # find word in nest...

... repeat steps until single word remains

=> "sprg" (return False as "sprig" != "spring")
Given a starting word and a final word nest, return True if the word nest is valid. Return False otherwise.

Examples
valid_word_nest("deep", "deep") ➞ True

valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel") ➞ True

valid_word_nest("painter", "ppaintppapaipainterinternteraintererainter") ➞ False
# Doesn't show starting word after being collapsed.

valid_word_nest("shape", "sssshapeshapehahapehpeape") ➞ False
# Word placed outside, not inside itself.
Notes
Valid word nests can only be created by repeatedly placing the word inside itself, so at any point when collapsing the nest,
there should only be one instance of the word to be found.
"""
import re

def valid_word_nest(word, nest):

    # while nest != word:
    #
    #     match = re.search(word, nest)
    #     match_start = match.start()
    #     match_end = match.end()
    #
    #     if match_start:
    #         nest = nest[:match_start] + '' + nest[match_end:]
    #
    #     if len(word) >= len(nest):
    #         break
    #
    # return nest


    while len(nest) > len(word):

        match = re.search(word, nest)
        if match:
            if len(re.findall(word, nest)) > 1:
                return False
            else:
                nest = re.sub(word, '', nest)
        else:
            return False

    return word == nest

print(valid_word_nest("deep", "deep"))
print(valid_word_nest("novel", "nonnonovnovnovelelelvelovelvel"))
print(valid_word_nest("painter", "ppaintppapaipainterinternteraintererainter"))
print(valid_word_nest("shape", "sssshapeshapehahapehpeape"))
