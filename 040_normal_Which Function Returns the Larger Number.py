"""
Your function will be passed two functions, f and g, that don't take any parameters. Your function has to call them, and return a string which indicates which function returned the larger number.

If f returns the larger number, return the string f.
If g returns the larger number, return the string g.
If the functions return the same number, return the string neither.
Examples
which_is_larger(lambda: 5, lambda: 10) ➞ "g"

which_is_larger(lambda: 25,  lambda: 25) ➞ "neither"

which_is_larger(lambda: 505050, lambda: 5050) ➞ "f"
Notes
This exercise is designed as an introduction to higher order functions (functions which use other functions to do their work).
"""

def which_is_larger(f, g):

    if f() > g():
        return "f"
    elif f() < g():
        return "g"
    else:
        return "neither"

print(which_is_larger(lambda: 5, lambda: 10))
print(which_is_larger(lambda: 10, lambda: 5))
print(which_is_larger(lambda: 25, lambda: 25))



