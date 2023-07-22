"""
Breaking News!
A local news station needs your help to generate the scrolling text for the headlines!

Create a function that returns a list of strings, where each string contains a single frame of what the scrolling text will look like.

Text will scroll from right to left.
The screen will have a width of n characters.
Start and stop when no letters appear on the screen.
The example below will demonstrate the output when the screen width is 10.

Examples
news_at_ten("edabit", 10) ➞ [
  "          ",
  "         e",
  "        ed",
  "       eda",
  "      edab",
  "     edabi",
  "    edabit",
  "   edabit ",
  "  edabit  ",
  " edabit   ",
  "edabit    ",
  "dabit     ",
  "abit      ",
  "bit       ",
  "it        ",
  "t         ",
  "          "
]
Notes
Every string should be n characters long, so you should pad the string with spaces if the text isn't long enough.
Similarly, if the text is too long for the screen width, then it's only possible to display a fraction of the text at a time.
See the Tests tab for more examples.
"""

def news_at_ten(txt, n):

    str_1 = ' ' * n + txt + ' ' * n
    lst_1 = []

    for i in range(len(txt)+ n + 1):
        lst_1.append(str_1[:n]) # 空白
        str_1 = str_1[1:len(txt) + n + 1] + str_1[0]

    return lst_1




    # s = " " * n + txt + " " * n
    # return [s[i: i + n] for i in range(n + len(txt) + 1)]


# def news_at_ten(text, n):
#     result = []
#     text_length = len(text)
#     padding = n
#
#     for i in range(text_length + n):
#         if i < n:
#             line = text[:i]
#             line = line.rjust(padding)
#         else:
#             line = text[i - n:i]
#             line = line.rjust(padding)
#
#         result.append(line)
#         padding -= 1
#
#     print(result)

    # results = []
    # for line in result:
    #     line_len = len(list(line)[3:13])
    #     if line_len <= n:
    #         results.append("".join(list(line)[3:13] + [" "] * (10 - line_len)))
    #
    # results.append("".join([" "] * n))
    # return results


    # result.append(' ' * n)
    # return result

# # Test cases
# test_cases = [
#     ('edabit', 10),
#     ('The latest news from News at Ten', 17),
#     ('Woman singlehandedly boosts seaside town economy with sea-shell business!', 7),
#     ('news', 30),
#     ('Hello World', 11)
# ]

# for text, n in test_cases:
#     result = news_at_ten(text, n)
#     for line in result:
#         print(line)
#     print()

print(news_at_ten("edabit", 10))
print(news_at_ten('The latest news from News at Ten', 17))




# def news_at_ten(text, n):
#
#     result = []
#     padding = n - 1
#
#     for i in range(len(text) + n):
#         if i < n:
#             line = text[:i] + text[i:]
#             line = line.rjust(n + padding)
#         else:
#             line = text[i - n:i]
#             line = line.rjust(n + padding)
#
#         result.append(line)
#         padding -= 1
#
#     results = []
#     for line in result:
#         line_len = len(list(line)[3:13])
#         if line_len <= n:
#             results.append("".join(list(line)[3:13] + [" "] * (10 - line_len)))
#
#     results.append("".join([" "] * n))
#     return results
#
# print(news_at_ten("edabit", 10))


