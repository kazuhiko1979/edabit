"""
Smiley Faces :)
You will be given a string of characters containing only the three characters : ( ) :

Create a function returns a number based on the number of sad and smiley faces there are.

The happy faces :) and (: are worth 1.
The sad faces :( and ): are worth -1.
Worked Example
happiness_number(":):(") ➞ -1
# The first 2 characters are :)        +1      Total: 1
# 2nd and 3rd characters are ):     -1      Total: 0
# 3rd and 4th characters are :(      -1      Total: -1
Examples
happiness_number(":):(") ➞ -1

happiness_number("(:)") ➞ 2

happiness_number("::::") ➞ 0
Notes
All test cases will be valid.
"""
def happiness_number(s):

    return s.count(':)') + s.count('(:') - s.count(':(') - s.count('):')

    # c = 0
    # for a, b in zip(s, s[1:]):
    #     if a + b in (':)', '(:'):
    #         c += 1
    #     if a + b in (':(', '):'):
    #         c -= 1
    # return c


    # happy = 0
    # sad = 0
    # happy += s.count(":)")
    # happy += s.count("(:")
    # sad -= s.count(":(")
    # sad -= s.count("):")
    # return happy + sad



    # i = 0
    # res = []
    # count = 0
    #
    # faces = {':)': 1,
    #          '(:': 1,
    #          ':(': -1,
    #          '):': -1,
    #          }
    #
    # while i < len(list(s)):
    #     if i+1 >= len(list(s)):
    #         break
    #     else:
    #         face = list(s)[i] + list(s)[i+1]
    #         res.append(face)
    #         i += 1
    #
    # print(res)
    #
    # for j in res:
    #     if j in faces.keys():
    #         count += faces.get(j)
    # return count

print(happiness_number(":):("))
print(happiness_number("(:)"))








