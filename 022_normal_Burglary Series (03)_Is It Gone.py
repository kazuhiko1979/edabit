"""
Your spouse is not concerned with the loss of material possessions but rather with his/her favorite pet. Is it gone?!

Given a dictionary of the stolen items and a string in lower cases representing the name of the pet (e.g. "rambo"), return:

"Rambo is gone..." if the name is on the list.
"Rambo is here!" if the name is not on the list.
Note that the first letter of the name in the return statement is capitalized.

Examples
 items = {
  "tv": 30,
  "timmy": 20,
  "stereo": 50,
} ➞ "Timmy is gone..."
# Timmy is in the dictionary.


 items = {
  "tv": 30,
  "stereo": 50,
} ➞ "Timmy is here!"
# Timmy is not in the  dictionary.


items = { } ➞ "Timmy is here!"
# Timmy is not in the dictionary.
"""


def find_it(items, name):

    if not bool(items):
        return name.capitalize() + " is here!"

    for item in items.items():
        if name in item[0]:
            return name.capitalize() + " is gone..."
    return name.capitalize() + " is here!"


print(find_it({
  "tv": 30,
  "stereo": 50,
}, "rocky"))

print(find_it({}, "rambo"))

print(find_it({
  "tv": 30,
  "stereo": 50,
	"julius": 100,
}, "julius"))


print(find_it({
  "tv": 30,
  "stereo": 50,
	"batman": 200,
}, "batman"))

