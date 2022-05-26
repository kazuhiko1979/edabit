"""
Create a function that returns the count of all bridges in a two-dimensional grid.

Bridge B should be counted if:

It connects from one end of the grid to the one opposite to it.
It is unobstructed.
Example
"#########/#       #/#   #   #/#   #   #/#### ####/#   #   #/#   #   #/#       #/#########"
In this case the number 4 is returned because, when unraveled, the string reveals four bridges that meet the requirements listed above as shown:

#########/
#       #/
#   #   #/
#   #   #/
#### ####/
#   #   #/
#   #   #/
#       #/
#########
Notes
Slashes / act as separators.
Intersecting bridges can still count, as shown.
Vertical bridges count as long as the requirements are met.
"""

# s = "#########/#       #/#   #   #/#   #   #/#### ####/#   #   #/#   #   #/#       #/#########"
# s = "   ###   /    #    /    #    /#   #   #/#########/#   #   #/    #    /    #    /   ###   "
# s = "         /         /         /#########/#   #   #/#########/         /         /         "
# s = "    #    /#########/#########/#########/#########/#########/#########/#########/ ####### "
# s = "#########/#########/#########/#########/#########/#########/#########/#########/#########"
# s = "# # # # #/# # # # #/# # # # #/# # # # #/#########/# # # # #/# # # # #/# # # # #/# # # # #"
s = "##     ##/##     ##/##     ##/##     ##/#########/##     ##/##     ##/##     ##/##     ##"

def bridges(s):

    # v2
    # print('横橋カウント')
    # for i in s.split("/"):
    #     print(i)
    # print(s.count('#'*9))
    #
    # # print('------')
    #
    # print('縦橋カウント')
    # for i in range(9):
    #     print(s[i::10])
    # print([s[i::10] for i in range(9)].count('#'*9))
    #
    # return s.count('#'*9) + [s[i::10] for i in range(9)].count('#'*9)


    # v1
    s = s.split("/")
    for i in s:
        print(i)
    #
    # 水平”＃”橋になっている数をカウント
    horizon = sum([1 for i in s if set(i) == {"#"}])
    # 縦”＃”橋になっている数をカウント
    vertical = sum(1 for i in range(len(s[0])) if all(j[i] == "#" for j in s))

    return horizon + vertical



print(bridges("   ###   /    #    /    #    /#   #   #/#########/#   #   #/    #    /    #    /   ###   "))
print(bridges("#########/#       #/#   #   #/#   #   #/#### ####/#   #   #/#   #   #/#       #/#########"))
print(bridges("##     ##/##     ##/##     ##/##     ##/#########/##     ##/##     ##/##     ##/##     ##"))