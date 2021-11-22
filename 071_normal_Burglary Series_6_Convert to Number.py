"""
Burglary Series (06): Convert to Number
You prepare a list to send to the insurance company. As you finish, you notice you misformatted it. Given a dictionary with at least one key/value pair, convert all the values to numbers.

Examples
convert_to_number({ "piano": "200" }) ➞ { "piano": 200 }

convert_to_number({ "piano": "200", "tv": "300" }) ➞ { "piano": 200, "tv": 300 }

convert_to_number({ "piano": "200", "tv": "300", "stereo": "400" }) ➞ { "piano": 200, "tv": 300, "stereo": 400 }
Notes
You will only be tested for numbers (ints), not strings or floats.
"""

def convert_to_number(dictionary):

    temp = {key: int(val) for key, val in dictionary.items()}
    return temp

print(convert_to_number({ "piano": "200" }))


