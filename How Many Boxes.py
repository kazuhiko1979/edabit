"""
You work in a factory, and your job is to take items from a conveyor belt and pack them into boxes. Each box can hold a
maximum of 10 kgs. Given an array containing the weight (in kg) of each item, how many boxes would you need to pack all of the items?

Example
boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]) ➞ 5

// Box 1 = [2, 1, 2, 5] (10kg)
// Box 2 = [4, 3] (7kg)
// Box 3 = [6, 1, 1] (8kg)
// Box 4 = [9] (9kg)
// Box 5 = [3, 2] (5kg)
Notes
There will always be a minimum of 1 item to pack. All items will weigh less than or equal to 10 kgs,
and need to be packed in the order that they arrive.
"""


def boxes(weights):

    each_box = []
    count = 0

    for i in weights:
        each_box.append(i)
        if sum(each_box) == 10:
            count += 1
            each_box.clear()

        if sum(each_box) > 10:
            add = each_box.pop()
            if sum(each_box) < 10:
                count += 1
                each_box.clear()
                each_box.append(add)
                if sum(each_box) == 10:
                    count += 1
                    each_box.clear()

    if each_box:
        count += 1

    return count

    # box, count = 0, weights[0]
    # for x in weights[1:]:
    #     if x + count > 10:
    #         box += 1
    #         count = 0
    #     count += x
    # return box + 1

print(boxes([2, 1, 2, 5, 4, 3, 6, 1, 1, 9, 3, 2]))
print(boxes([7, 1, 2, 6, 1, 2, 3, 5, 9, 2, 1, 2, 5]))
print(boxes([1, 3, 3, 3, 2, 1, 1, 9, 7, 10, 8, 6, 1, 2, 9]))
print(boxes([4, 1, 2, 3, 5, 5, 1, 9]))







