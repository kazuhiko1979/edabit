"""
Given a dictionary containing up to six phrases, return a list containing the matching phrases according to the given string (p).
Ignore any digit that is placed after or before the given string.
Whether the first letter is capitalized or not, if all letters of the word match the given string (p), it is valid.
If it does not match the given string (p) then None.
Examples
find_pattern({
  "Phrase1": "CCOVIDD-19 is no good",
  "Phrase2": "COVID-18 is no good",
  "Phrase3": "COVID-17 is no good"
}, "COVID-19")

➞ ["Phrase1 = COVID-19", "Phrase2 = None", "Phrase3 = None"]
find_pattern({
  "Phrase1": "Edabit is great",
  "Phrase2": "Edabit is very great",
  "Phrase3": "Edabit is really great"
}, "really")

➞ ["Phrase1 = None", "Phrase2 = None", "Phrase3 = really"]
"""

def find_pattern(dict_, p):

    ret = []
    for i in dict_:
        if p.lower() in dict_[i].lower():
            ret.append(i + ' = ' + p)
        else:
            ret.append(i + ' = None')
    return sorted(ret)


    # tmp1 = []
    # tmp2 = []
    #
    # for i in dict_.items():
    #     m = i[1].find(p)
    #
    #     if m >= 0:
    #         tmp1.append('{}'.format(i[0]))
    #         tmp2.append(' = {}'.format(p))
    #     else:
    #         tmp1.append('{}'.format(i[0]))
    #         tmp2.append(' = {}'.format(None))
    #
    #     tmp1 = sorted(tmp1)
    #
    # tmp2 = sorted([[str(i)+k] for i, k in enumerate(tmp2)])
    #
    # target_forward = '='
    #
    # tmp3 = []
    #
    # for i, k in zip(tmp1, tmp2):
    #
    #     k = " ".join(sorted(k))
    #     idx_forward = k.find(target_forward)
    #     k = k[idx_forward+1:]
    #
    #     items = i + ' =' + k
    #     tmp3.append(items)
    #
    # return tmp3


print(find_pattern({
    "Phrase1": 'Made in China',
    "Phrase2": 'Made in Brazil',
    "Phrase3": 'Made in America',
    "Phrase4": 'Made in Colombia',
}, 'Jhonson'))

print(find_pattern({
    "Phrase1": 'Edabit is great',
    "Phrase2": 'Edabit is very great',
    "Phrase3": 'Edabit is really great',
}, 'really'))

print(find_pattern({
    "Phrase1": 'COVID-19 is no good',
    "Phrase2": 'COVID-18 is no good',
    "Phrase3": 'COVID-17 is no good',
}, 'COVID-19'))

print(find_pattern({
    "Phrase1": 'Made12 in China',
    "Phrase2": 'Made in Brazil',
    "Phrase3": '32Made in America',
    "Phrase4": 'Made in Colombia',

}, 'Made'))
