"""
In electronics, a digital-to-analog converter (DAC, D/A, or D-to-A) is a system that converts a binary representation of that signal into an analog output. An 8 bit converter can represent a maximum of 2^8 different values, with each successive value differing by 1/256 of the full scale value, this becomes the system resolution.

Create a function that takes a decimal number representation of a signal and returns the analog voltage level that would be created by a DAC if it were given the same number in binary.

While value range is 0-1023, reference range is 0-5.00 volts. Value and reference is directly proportional.

This DAC has 10 bits of resolution and the DAC reference is set at 5.00 volts.

Examples
V_DAC(0) ➞ 0

V_DAC(1023) ➞ 5

V_DAC(400) ➞ 1.96
Notes
You should return your value rounded to two decimal places.
"""
def V_DAC(value):

    MAX_VOLT = 5
    MAX_VALUE = 1023

    if value != 0:
        ref_num = MAX_VOLT / MAX_VALUE
        return round(value * ref_num, 2)
    else:
        return 0

print(V_DAC(1023))
print(V_DAC(500))
print(V_DAC(400))
print(V_DAC(850))
print(V_DAC(0))

