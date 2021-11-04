"""
When importing objects from a module in Python, the syntax usually is as follows:

from module_name import object
Given a string of an incorrect import statement, return the fixed string. All import statements will be the wrong way round.

Examples
fix_import("import object from module_name") ➞ "from module_name import object"

fix_import("import randint from random") ➞ "from random import randint"

fix_import("import pi from math") ➞ "from math import pi"
Notes
All Tests will be valid strings.
"""

def fix_import(s):

    # return 'from {} import {}'.format(s.split()[-1], s.split()[1])

    x = s.split(" ")
    return x[2] + " " + x[3] + " " + x[0] + " " + x[1]

    # replaced_s = []
    #
    # s = s.split(' ')
    #
    # replaced_s.append(s[2])
    # replaced_s.append(s[3])
    # replaced_s.append(s[0])
    # replaced_s.append(s[1])
    #
    # return ' '.join(replaced_s)

print(fix_import("import object from module_name"))
print(fix_import("import randint from random"))
print(fix_import("import pi from math"))



