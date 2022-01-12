"""
Format X: Unpacking Dictionaries
For each challenge of this series you do not need to submit a function. Instead, you need to submit a template string that can formatted in order to get a certain outcome.

Write three dictionaries and a template string according to the following example. Notice the article "a" in the third example:

Example
dic1 = {"yourkeys": "yourvalues"}
dic2 = {"yourkeys": "yourvalues"}
dic3 = {"yourkeys": "yourvalues"}
template = "yourtemplatestringhere"

template.format(**dic1) ➞ "I like Mary, I don't like May."
template.format(**dic2) ➞ "I love Eda, I don't love Bit."
template.format(**dic3) ➞ "I have a Pidgey, I don't have a Rattata."
Tips
The elements of a dictionary can be unpacked and passed to .format() as keyword arguments using a double star operator **:

product = {"name": "pokeball", "price": 20}
"One {name} is ${price:.2f}".format(**product) ➞ "One pokeball is $20.00"
Notes
Submit a string, not a function.
Do not change the names of the variables template, dic1, dic2 and dic3.
"""

dic1 = {"verb": "like", "yes": "Mary", "no": "May"}
dic2 = {"verb": "love", "yes": "Eda", "no": "Bit"}
dic3 = {"verb": "have", "yes": "a Pidgey", "no": "a Rattata"}

template = "I {verb} {yes}, I don't {verb} {no}."

print(template.format(**dic1))
print(template.format(**dic2))
print(template.format(**dic3))