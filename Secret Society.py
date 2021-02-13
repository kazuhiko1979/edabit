"""
A group of friends have decided to start a secret society. The name will be the first letter of each of their names, sorted in alphabetical order.

Create a function that takes in a list of names and returns the name of the secret society.

Examples
society_name(["Adam", "Sarah", "Malcolm"]) ➞ "AMS"
society_name(["Harry", "Newt", "Luna", "Cho"]) ➞ "CHLN"
society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]) ➞ "CJMPRR"
Notes
The secret society's name should be entirely uppercased.
"""
def society_name(friends):

    return ''.join(sorted([x[0] for x in friends if x.istitle]))

    # results = ""
    # for i in friends:
    #     if i.istitle():
    #         results += str(i[0])
    # return ''.join(sorted(results))


print(society_name(["Adam", "Sarah", "Malcolm"]))
print(society_name(["Harry", "Newt", "Luna", "Cho"]))
print(society_name(["Phoebe", "Chandler", "Rachel", "Ross", "Monica", "Joey"]))
