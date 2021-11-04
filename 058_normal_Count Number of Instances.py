"""
Create a class named User and create a way to check the number of users (number of instances) were created, so that the value can be accessed as a class attribute.

Examples
u1 = User("johnsmith10")
User.user_count ➞ 1

u2 = User("marysue1989")
User.user_count ➞ 2

u3 = User("milan_rodrick")
User.user_count ➞ 3
Make sure that the usernames are accessible via the instance attribute username.

u1.username ➞ "johnsmith10"

u2.username ➞ "marysue1989"

u3.username ➞ "milan_rodrick"
"""

class User:

    user_count = 0

    def __init__(self, username):
        self.username = username
        User.user_count += 1


u1 = User("johnsmith10")
print(u1.username)
print(User.user_count)

u2 = User("marysue1989")
print(u2.username)
print(User.user_count)

u3 = User("milan_rodrick")
print(u3.username)
print(User.user_count)


