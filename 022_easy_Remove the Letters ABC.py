"""
Create a function that will remove the letters "a", "b" and "c" from the given string and return the modified version. If the given string does not contain "a", "b", or "c", return None.

Examples
remove_abc("This might be a bit hard") ➞ "This might e  it hrd"

remove_abc("hello world!") ➞ None

remove_abc("") ➞ None
Notes
If the given string does not contain "a", "b", or "c", return None.
"""

def remove_abc(txt):

    res = ''.join([i.replace(i, "") if i in ["a", "b", "c"] else i for i in txt ])
    return res if txt != res else None

print(remove_abc("This might be a bit hard"))
print(remove_abc("hello world!"))
print(remove_abc(""))



