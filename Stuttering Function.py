"""
Write a function that stutters a word as if someone is struggling to read it.
The first two letters are repeated twice with an ellipsis ...
and space after each, and then the word is pronounced with a question mark ?.
Examples
stutter("incredible") ➞ "in... in... incredible?"
stutter("enthusiastic") ➞ "en... en... enthusiastic?"
stutter("outstanding") ➞ "ou... ou... outstanding?"
"""
def stutter(word):

#     str = "... "
#     word_twice = word[0:2]
#     result = (word_twice + str) * 2, word + "?"
#
#     for i in result:
#         return i, end=' ')
#
    # return f'{word[0:2]}... {word[0:2]}... {word}?'
    return '{}... {}... {}?'.format(word[0:2], word[0:2], word)

if __name__ == '__main__':
    print(stutter("incredible"))
