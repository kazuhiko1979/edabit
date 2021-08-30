"""
Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

Form the fullname by simply joining the first and last name together, separated by a space.
Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.
Examples
emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")
emp_1.fullname ➞ "John Smith"

emp_2.email ➞ "mary.sue@company.com"

emp_3.firstname ➞ "Antony"
Notes
The attributes firstname and lastname are already made for you.
"""


class Employee:

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.fullname = firstname + ' ' + lastname
        self.email = '{}.{}@company.com'.format(firstname, lastname).lower()

    # @property
    # def fullname(self):
    #     return self.firstname + ' ' + self.lastname
    #
    # @property
    # def email(self):
    #     txt = self.firstname + '.' + self.lastname + '@company.com'
    #     return txt.lower()

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

print(emp_1.firstname)
print(emp_1.email)
print(emp_1.fullname)

