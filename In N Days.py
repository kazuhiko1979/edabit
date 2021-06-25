"""
If today was Monday, in two days, it would be Wednesday.

Create a function that takes in a list of days as input and the number of days to increment by. Return a list of days after n number of days has passed.

Examples
after_n_days(["Thursday", "Monday"], 4) ➞ ["Monday", "Friday"]

after_n_days(["Sunday", "Sunday", "Sunday"], 1) ➞ ["Monday", "Monday", "Monday"]

after_n_days(["Monday", "Tuesday", "Friday"], 1) ➞ ["Tuesday", "Wednesday", "Saturday"]

"""
week = {
    "Monday": 1,
    "Tuesday": 2,
    "Wednesday": 3,
    "Thursday": 4,
    "Friday": 5,
    "Saturday": 6,
    "Sunday": 7,
}
week_swap = {v: k for k, v in week.items()}


def after_n_days(days, n):

    return [week_swap[(week[day] + n) % 7] for day in days]


print(after_n_days(["Thursday", "Monday"], 4))