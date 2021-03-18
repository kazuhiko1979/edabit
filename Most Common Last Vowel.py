def common_last_vowel(txt):

    return sorted(txt.lower(), key=lambda x: x in 'aeiou')[-1]

  
    # vowels = []
    # max(vowels, default=0)
    # d = {}
    #
    # for vowel in txt.lower():
    #     if vowel in 'aiueo':
    #         vowels.append(vowel)
    # print(vowels)
    # for key in vowels:
    #     if key not in d:
    #         d[key] = 0
    #     d[key] += 1
    #
    # vowels = max(d, key=d.get) if vowels else 0
    # return vowels


print(common_last_vowel("Hello World!"))
print(common_last_vowel("Watch the characters dance!"))
print(common_last_vowel("OOI UUI EEI AAI"))
print(common_last_vowel("amy and acts"))
print(common_last_vowel("munch munch munch tasty tasty brunch"))