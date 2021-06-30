"""
RGB is a color model that defines color by the combination of Red, Green, and Blue. An RGB tuple is composed of three numbers that specify the intensity of each color. Because it uses 8 bits (0s or 1s) for each color, each intensity can be transformed into a hexadecimal number with two digits at most.

There are 256 possible shades for each color, since "11111111" (or hex "ff") corresponds to decimal 255, plus the number 000. The combination of all 256 possible shades for the three primary colors gives 256 cubed, or over 16 million possible colors.

Write a function that takes a color in RGB or hex and returns the opposite. If it takes in the three integers in an RGB tuple, it should return a string with the equivalent hexadecimal notation, plus a hash sign (#) at the front. If it takes in a string in hex, it should return a tuple with the three integers corresponding to RGB.

Examples
rgb_or_hex(150, 50, 76) ➞ "#96324c"
# 150 is hex 96, 50 is hex 32 and 76 is hex 4c.

rgb_or_hex("#303749") ➞ (48, 55, 73)
# 30 is dec 48, 37 is dec 55 and 49 is dec 73.

rgb_or_hex(170, 14, 0) ➞ "#aa0e00"
# 170 is hex aa, 14 is hex e and 0 is hex 0.
Notes
Remember that all three colors should be two-digit hex numbers, so for Green value 14, the hex value should be 0e rather than just e.
Try using formatting or filling methods to minimize if statements.
Trivia
Black is defined as the absence of color, or RGB(0,0,0), while white is defined as all colors at full intensity, or RGB(255,255,255). When all colors are at the same intensity and some value between 0 and 255, the resulting color is a darker or lighter grey.
"""


def rgb_or_hex(*args):

    for i in str(args):
        if '#' in i:
            value = str(''.join(args)).lstrip('#')
            lv = len(value)
            return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

    return '#%02x%02x%02x' % args


print(rgb_or_hex(150, 50, 76))
print(rgb_or_hex("#303749"))