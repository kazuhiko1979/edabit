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

    s = s.split("/")

    # 水平”＃”橋になっている数をカウント
    horizon = sum([1 for i in s if set(i) == {"#"}])
    # 縦”＃”橋になっている数をカウント
    vertical = sum(1 for i in range(len(s[0])) if all(j[i] == "#" for j in s))

    return horizon + vertical

print(bridges("   ###   /    #    /    #    /#   #   #/#########/#   #   #/    #    /    #    /   ###   "))

