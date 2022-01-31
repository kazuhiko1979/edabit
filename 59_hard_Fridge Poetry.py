"""
Fridge Poetry
Write a function that returns True if it's possible to build a phrase txt1 using only the characters from another phrase txt2.

Examples
can_build("got 2 go", "gogogo 2 today") ➞ True

can_build("sit on top", "its a moo point") ➞ True

can_build("long high add or", "highway road go long") ➞ False

can_build("fill tuck mid", "truck falls dim") ➞ False
Notes
All letters will be in lower case.
Numbers and special characters included.
Ignore whitespaces.
Do not count white space as a character.
"""

def can_build(txt1, txt2):

    # print([txt2.count(i) for i in set(txt1) if i.isalpha()])
    # return all(txt2.count(i) >= txt1.count(i) for i in set(txt1) if i.isalpha())


    for i in list(txt1):
        if i != ' ' and txt1.count(i) > txt2.count(i):
            return False
    return True


    # for i in ''.join(txt1):
    #
    #     if i in ''.join(txt2):
    #         txt1 = txt1.replace(i, "")
    #         pop_index_of_txt2 = txt2.find(i)
    #         txt2 = txt2[:pop_index_of_txt2] + txt2[pop_index_of_txt2 + 1:]
    #     elif i == ' ':
    #         txt1 = txt1.replace(i, "")
    #     else:
    #         return False
    #
    # return not txt1

print(can_build("got 2 go", "gogogo 2 today"))
print(can_build("for an angel", "angel forest nymph awaken"))
print(can_build("sit on top", "its a moo point"))
print(can_build("solar to oven", "love desolate rose thorn"))
print(can_build("gate im in", "magnetizing"))
print(can_build("dool", "ken doll"))
print(can_build("long high add or", "highway road go long"))
print(can_build("fill tuck mid", "truck falls dim"))




