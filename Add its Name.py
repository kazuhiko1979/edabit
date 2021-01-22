"""Given three arguments ⁠— a dictionary obj, a key name and a value ⁠— return a dictionary with that name and value in it (as key-value pairs).

Examples
add_name({}, "Brutus", 300) ➞ { "Brutus": 300 }

add_name({ "piano": 500 }, "Brutus", 400) ➞ { "piano": 500, "Brutus": 400 }

add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440) ➞ { "piano": 500, "stereo": 300, "Caligula": 440 }
"""
def add_name(object, name, value):
    object[name] = value
    return object


if __name__ == '__main__':
    print(add_name({}, "Brutus", 300))
    print(add_name({"piano": 500}, "Brutus", 400))
    print(add_name({ "piano": 500, "stereo": 300 }, "Caligula", 440))


