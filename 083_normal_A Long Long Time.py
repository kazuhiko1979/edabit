"""
A Long Long Time
Create a function that takes three values:

h hours
m minutes
s seconds
Return the value that's the longest duration.

Examples
longest_time(1, 59, 3598) ➞ 1

longest_time(2, 300, 15000) ➞ 300

longest_time(15, 955, 59400) ➞ 59400
Notes
No two durations will be the same.
"""

def longest_time(h, m, s):

    # return max((h*3600, h), (m*60, m), (s, s))[1]

    m = {h*60*60:h, m*60:m, s:s}
    return m[max(m)]


    # res = {h: h,
    #        m: m,
    #        s: s
    #        }
    #
    # res[h] = res[h] * 60 * 60
    # res[m] = res[m] * 60
    #
    # return max(res, key=res.get)

print(longest_time(1, 59, 3598))
print(longest_time(2, 300, 15000))
