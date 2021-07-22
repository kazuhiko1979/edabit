"""
Create a function that takes the memory size (MS is a string type) as an argument and returns the actual memory size.

Examples
actual_memory_size(32GB) ➞ 29.76GB

actual_memory_size(2GB) ➞ 1.86GB

actual_memory_size(512MB) ➞ 476MB
Notes
The actual storage loss on a USB device is 7% of the overall memory size!
If the actual memory size was greater than 1 GB, round your result to two decimal places.
For the purposes of this challenge, there are 1000 MB in a Gigabyte.
"""


def actual_memory_size(MS):

    if 'GB' in MS:

        MS = "{}".format(float(int(MS[:-2])*0.93))

        if float(MS) < 1:

            MS = round(float(MS) * 1000)
            return "{}MB".format(MS)

        return "{}GB".format(MS)

    else:

        return "{}MB".format(round(float(int(MS[:-2]) * 0.93)))



    # if 'MB' in MS:
    #     print(MS[:-2])

    # num_GB = ""
    # num_MB = ""
    #
    # if 'GB' in MS:
    #     for i in MS:
    #         if i.isdigit():
    #             num_GB = num_GB + i
    #     num_GB = int(num_GB) * 0.93
    #
    #     if num_GB < 1:
    #         num_GB = round(num_GB * 1000)
    #         return "{}MB".format(str(num_GB))
    #     else:
    #         return "{}GB".format(str(num_GB))
    #
    # if 'MB' in MS:
    #     for j in MS:
    #         if j.isdigit():
    #             num_MB = num_MB + j
    #     num_MB = round(int(num_MB) * 0.93)
    #
    #     return "{}MB".format(str(num_MB))

print(actual_memory_size('32GB'))
print(actual_memory_size('512MB'))
print(actual_memory_size("1GB"))










