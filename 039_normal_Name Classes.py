"""
Write a class called Name and create the following attributes given a first name and last name (as fname and lname):

An attribute called fullname which returns the first and last names.
A attribute called initials which returns the first letters of the first and last name. Put a . between the two letters.
Remember to allow the attributes fname and lname to be accessed individually as well.

Examples
a1 = Name("john", "SMITH")
a1.fname ➞ "John"

a1.lname ➞ "Smith"

a1.fullname ➞ "John Smith"

a1.initials ➞ "J.S"
Notes
Make sure only the first letter of each name is capitalised.
"""

class Name:

    def __init__(self, fname, lname):
        self.fname = fname.capitalize()
        self.lname = lname.capitalize()
        self.fullname = self.fname + " " + self.lname
        self.initials = self.fname[0] + "." + self.lname[0]

    # def fname(self):
    #     return self.firstName.capitalize()
    #
    # def lname(self):
    #     return self.lastName.capitalize()
    #
    # def fullname(self):
    #     return "{} {}".format(self.firstName.capitalize(), self.lastName.capitalize())
    #
    # def initials(self):
    #     return "{}.{}".format(self.firstName[0].capitalize(), self.lastName[0].capitalize())


a1 = Name("john", "SMITH")
a2 = Name("sARah", "fRolliE")

print(a1.fname)
print(a1.lname)
print(a1.fullname)
print(a1.initials)

print(a2.fname)
print(a2.lname)
print(a2.fullname)
print(a2.initials)





