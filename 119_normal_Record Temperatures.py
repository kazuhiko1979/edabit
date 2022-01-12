"""
Record Temperatures
You are given two lists that each contain data that represents the min and max weather temperatures for each day of the week.

The records list contains the all-time record low/high temperatures for that day of the week.

[[record low, record high], ...]
The current week list contains the daily low/high temperatures for each day of the current week.

[[daily low, daily high], ...]
A daily high temperature is considered a new record high if it is higher than the record high for that day of the week. A daily low temperature is considered a new record low if it is lower than the record low for that day of the week.

Compare the daily low/high temperatures of the current week to the record lows/highs and return a list with the updated record temperatures.

There may be multiple record temperatures in a week.
If there are no broken records return the original records list.
Example
#             sun       mon      tues       wed      thur      fri       sat
record_temps([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]])

➞           [[34, 82], [19, 82], [20, 89], [5, 88], [9, 88], [26, 89], [27, 83]]
The previous record low for Monday was 24. The current week's low for Monday was 19. So 19 replaces 24 as Monday's new record low.

Notes
There won't be a record high and record low set on the same day.
Index 0 will always be the low and index 1 will always be the high [low, high].
For reference these temps are °F but you do not need to convert any temperatures.
"""


def record_temps(records, currentweek):

    # return [[min(i[0], j[0]), max(i[1], j[1])] for i, j in zip(records, currentweek)]


    # result = []
    # for i, j in zip(records, currentweek):
    #     result.append([min(i+j)] + [max(i+j)])
    #
    # return result



    # result = []
    # for record, current in zip(records, currentweek):
    #     low_high_record = []
    #     record.extend(current)
    #     low_high_record.append(min(record))
    #     low_high_record.append(max(record))
    #     result.append(low_high_record)
    # return result


print(record_temps([[34, 82], [24, 82], [20, 89],  [5, 88],  [9, 88], [26, 89], [27, 83]],
            [[44, 72], [19, 70], [40, 69], [39, 68], [33, 64], [36, 70], [38, 69]]))


print(record_temps(
        [
          [25, 80],
          [27, 88],
          [19, 88],
          [23, 85],
          [21, 89],
          [23, 78],
          [17, 79],
        ],
        [
          [40, 70],
          [41, 68],
          [45, 68],
          [39, 65],
          [44, 72],
          [43, 69],
          [37, 68],
        ]
      ))