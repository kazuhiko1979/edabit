"""
The insurance guy calls. They were about to pay you all that fortune you've been anxiously waiting for, but they detected further irregularities; the list of stolen items is misformatted and appears to contain other entries that don't belong there. Find and remove them.

You receive a dict with nested dicts with strings as values. Convert their values to number and return a dict with entries that evaluate to type int.

Examples
find_and_remove({
    "workshop": {
      "bedsheets": "2000",
      "working": "v0g89t7t",
      "pen": "370",
      "movies": "wo1a3d5d",
    },
  }), {
    "workshop": {
      "bedsheets": 2000,
      "pen": 370
      }
  }
find_and_remove({
  "bedroom": {
    "slippers": "10000",
    "piano": "5500",
    "call": "vet",
    "travel": "world",
  },
}), {
  "bedroom": {
    "slippers": 10000,
    "piano": 5500,
  },
}
"""


def find_and_remove(dct):

    remove_list_categories = []
    remove_list_items = []

    for categories, goods in dct.items():
        for good in goods.items():
            if not good[1].isdigit():
                remove_list_categories.append(categories)
                remove_list_items.append(good[0])
            else:
                dct[categories][good[0]] = int(dct[categories][good[0]])

    # return remove_helper(remove_list_categories, remove_list_items, dct)


# def remove_helper(categories, items, dct):

    # for c, i in zip(categories, items):

    for c, i in zip(remove_list_categories, remove_list_items):
        del dct[c][i]

    return dct
