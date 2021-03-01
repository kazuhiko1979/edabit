"""
A game of table tennis almost always sounds like Ping! followed by Pong! Therefore, you know that Player 2 has won if you hear Pong! as the last sound (since Player 1 didn't return the ball back).

Given a list of Ping!, create a function that inserts Pong! in between each element. Also:

If win equals True, end the list with Pong!.
If win equals False, end with Ping! instead.
Examples
ping_pong(["Ping!"], True) ➞ ["Ping!", "Pong!"]

ping_pong(["Ping!", "Ping!"], False) ➞ ["Ping!", "Pong!", "Ping!"]

ping_pong(["Ping!", "Ping!", "Ping!"], True) ➞ ["Ping!", "Pong!", "Ping!", "Pong!", "Ping!", "Pong!"]
Notes
You will always return the ball (i.e. the Pongs are yours).
Player 1 serves the ball and makes Ping!.
Return a list of strings.
"""
def ping_pong(lst, win):

    # result = []
    #
    # if win is True:
    #     for i in lst:
    #         result.append(i)
    #         result.append("Pong!")
    #     return result
    #
    # else:
    #     for i in range(0, len(lst)):
    #         result.append(lst[i])
    #         if i != len(lst)-1:
    #             result.append("Pong!")
    #     return result

    lst = ["Ping!", "Pong!"] * len(lst)
    if not win:
        lst.pop()
    return lst

print(ping_pong(["Ping!"], True))
print(ping_pong(["Ping!", "Ping!"], False))
print(ping_pong(["Ping!", "Ping!", "Ping!"], True))
