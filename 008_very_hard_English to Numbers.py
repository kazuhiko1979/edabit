"""
English to Numbers
This is a companion to my previous challenge.

Given an English description of an integer in the range 0 to 999, devise a function that returns the integer in numeric form.

Examples
eng2nums("four") ➞  4

eng2nums("forty") ➞ 40

eng2nums("six hundred") ➞ 600

eng2nums("one hundred fifteen") ➞ 115

eng2nums("seven hundred sixty seven") ➞ 767
Notes
No hyphens are used in test cases ("twenty three" not "twenty-three").
The word "and" is not used: "one hundred three" not "one hundred and three".
"""

def eng2nums(s):

	# v3
	d = {'thousand': '*1000', 'million': '*1000000', 'billion': '*1000000000', 'trillion': '*1000000000000', 'hundred': '*100', 'zero': '+0', 'one': '+1', 'two': '+2', 'three': '+3', 'four': '+4', 'five': '+5',
		 'six': '+6', 'seven': '+7', 'eight': '+8', 'nine': '+9', 'ten': '+10', 'eleven': '+11',
		 'twelve': '+12', 'thirteen': '+13', 'fourteen': '+14', 'fifteen': '+15', 'sixteen': '+16',
		 'seventeen': '+17', 'eighteen': '+18', 'nineteen': '+19', 'twenty': '+20', 'thirty': '+30',
		 'forty': '+40', 'fifty': '+50', 'sixty': '+60', 'seventy': '+70', 'eighty': '+80', 'ninety': '+90'}

	return eval(''.join(d[i] for i in s.split()))


	# v2
	# d = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
	# 	 'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15, 'sixteen': 16,
	# 	 'seventeen': 17, 'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
	# 	 'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90}
	#
	# l = s.split()
	# if len(l) == 1:
	# 	return d[s]
	# elif len(l) == 2:
	# 	return d[l[0]]*100 if 'hundred' in l else d[l[0]] + d[l[1]]
	# elif len(l) >= 3:
	# 	return d[l[0]]*100 + eng2nums(' '.join(l[2:]))



# v1
# def is_number(x):
#
#     if type(x) == str:
#         x = x.replace(',', '')
#     try:
#         float(x)
#     except:
#         return False
#     return True
#
#
# def eng2nums (textnum, numwords={}):
#
#     units = [
#         'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight',
#         'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen',
#         'sixteen', 'seventeen', 'eighteen', 'nineteen',
#     ]
#     tens = ['', '', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
#     scales = ['hundred', 'thousand', 'million', 'billion', 'trillion']
#     ordinal_words = {'first':1, 'second':2, 'third':3, 'fifth':5, 'eighth':8, 'ninth':9, 'twelfth':12}
#     ordinal_endings = [('ieth', 'y'), ('th', '')]
#
#     if not numwords:
#         numwords['and'] = (1, 0)
#         for idx, word in enumerate(units): numwords[word] = (1, idx)
#         for idx, word in enumerate(tens): numwords[word] = (1, idx * 10)
#         for idx, word in enumerate(scales): numwords[word] = (10 ** (idx * 3 or 2), 0)
#
#     textnum = textnum.replace('-', ' ')
#
#     current = result = 0
#     curstring = ''
#     onnumber = False
#     lastunit = False
#     lastscale = False
#
#     def is_numword(x):
#         if is_number(x):
#             return True
#         if word in numwords:
#             return True
#         return False
#
#     def from_numword(x):
#         if is_number(x):
#             scale = 0
#             increment = int(x.replace(',', ''))
#             return scale, increment
#         return numwords[x]
#
#     for word in textnum.split():
#         if word in ordinal_words:
#             scale, increment = (1, ordinal_words[word])
#             current = current * scale + increment
#             if scale > 100:
#                 result += current
#                 current = 0
#             onnumber = True
#             lastunit = False
#             lastscale = False
#         else:
#             for ending, replacement in ordinal_endings:
#                 if word.endswith(ending):
#                     word = "%s%s" % (word[:-len(ending)], replacement)
#
#             if (not is_numword(word)) or (word == 'and' and not lastscale):
#                 if onnumber:
#                     # Flush the current number we are building
#                     curstring += repr(result + current) + " "
#                 curstring += word + " "
#                 result = current = 0
#                 onnumber = False
#                 lastunit = False
#                 lastscale = False
#             else:
#                 scale, increment = from_numword(word)
#                 onnumber = True
#
#                 if lastunit and (word not in scales):
#                     # Assume this is part of a string of individual numbers to
#                     # be flushed, such as a zipcode "one two three four five"
#                     curstring += repr(result + current)
#                     result = current = 0
#
#                 if scale > 1:
#                     current = max(1, current)
#
#                 current = current * scale + increment
#                 if scale > 100:
#                     result += current
#                     current = 0
#
#                 lastscale = False
#                 lastunit = False
#                 if word in scales:
#                     lastscale = True
#                 elif word in units:
#                     lastunit = True
#
#     if onnumber:
#         curstring += repr(result + current)
#
#     return int(curstring)


print(eng2nums('four'))
print(eng2nums("forty"))
print(eng2nums("one hundred fifteen"))
print(eng2nums("seven hundred sixty seven"))
print(eng2nums("nine hundred ninety nine"))
print(eng2nums("twenty three"))
print(eng2nums("nine trillion eight billion seven million six thousand five hundred"))






