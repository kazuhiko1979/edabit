"""
Create a function that returns which chapter is nearest to the page you're on. If two chapters are equidistant, return the chapter with the higher page number.

Examples
nearest_chapter({
  "Chapter 1" : 1,
  "Chapter 2" : 15,
  "Chapter 3" : 37
}, 10) ➞ "Chapter 2"


nearest_chapter({
  "New Beginnings" : 1,
  "Strange Developments" : 62,
  "The End?" : 194,
  "The True Ending" : 460
}, 200) ➞ "The End?"


nearest_chapter({
  "Chapter 1a" : 1,
  "Chapter 1b" : 5
}, 3) ➞ "Chapter 1b"
Notes
All page numbers in the dictionary will be valid integers.
"""
from collections import defaultdict


def nearest_chapter(chapt, page):



    # res = defaultdict(list)
    #
    # for key, val in chapt.items():
    #     val = val - page
    #     val = abs(val)
    #     res[key].append(val)
    #
    # res = sorted([i[0] for i in dict(res).items() if i[1] == min(dict(res).values())])
    #
    # if len(res) > 1:
    #     ans = res.pop()
    #     return ans
    # elif len(res) == 1:
    #     return res[-1]
    #

print(nearest_chapter({
	"Chapter 1" : 1,
	"Chapter 2" : 15,
	"Chapter 3" : 37
}, 10))

print(nearest_chapter({
	"New Beginnings" : 1,
	"Strange Developments" : 62,
	"The End?" : 194,
	"The True Ending" : 460
}, 200))

#
print(nearest_chapter({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5
}, 3))
#
print(nearest_chapter({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5,
	"Chapter 1c" : 50,
	"Chapter 1d" : 100
}, 75))
#
#
print(nearest_chapter({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5,
	"Chapter 1c" : 50,
	"Chapter 1d" : 100,
	"Chapter 1e" : 200,
}, 150))


print(nearest_chapter({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5,
	"Chapter 1c" : 50,
	"Chapter 1d" : 100,
	"Chapter 1e" : 200
}, 74))

print(nearest_chapter({
	"Chapter 1a" : 1,
	"Chapter 1b" : 5,
	"Chapter 1c" : 50,
	"Chapter 1d" : 100,
	"Chapter 1e" : 200,
    "Chapter 1f": 400,

}, 300))



