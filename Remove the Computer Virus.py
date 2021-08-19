"""
Your computer might have been infected by a virus! Create a function that finds the viruses in files and removes them from your computer.

Examples
remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg") ➞ "PC Files: spotifysetup.exe, dog.jpg"

remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe ") ➞ "PC Files: antivirus.exe, cat.pdf"

remove_virus("PC Files: notvirus.exe, funnycat.gif") ➞ "PC Files: notvirus.exe, funnycat.gif")
Notes
Bad files will contain "virus" or "malware", but "antivirus" and "notvirus" will not be viruses.
Return "PC Files: Empty" if there are no files left on the computer.
"""
import re

def remove_virus(files):


    PC, *files = re.split(r': |, ', files)
    pattern = r'(?<!not)(?<!anti)(malware|virus)'
    files = filter(lambda x: not re.findall(pattern, x), files)
    return '{}: {}'.format(PC, ', '.join(files) or 'Empty')

    # PC, *files = re.split(r': |, ', files)
    # pattern = r'(?<!not)(?<!anti)(malware|virus)'
    # files = filter(lambda x: not re.findall(pattern, x), files)
    # return '{}: {}'.format(PC, ', '.join(files) or 'Empty')



    # files = files[10:].split(', ')
    # tmp = []
    # tmp1 = []
    #
    # for words in files:
    #     if words.startswith("anti"):
    #         tmp.append(words)
    #     if words.startswith("not"):
    #         tmp.append(words)
    #     elif "virus" not in words:
    #         tmp.append(words)
    #
    # for words in tmp:
    #     if "malware" not in words:
    #         tmp1.append(words)
    #
    # tmp1 = ', '.join(map(str, tmp1))
    #
    # if tmp1 == '':
    #     return "PC Files: Empty"
    # return "PC Files: " + tmp1

print(remove_virus("PC Files: spotifysetup.exe, virus.exe, dog.jpg"))
print(remove_virus("PC Files: antivirus.exe, cat.pdf, lethalmalware.exe, dangerousvirus.exe "))
print(remove_virus("PC Files: notvirus.exe, funnycat.gif"))
print(remove_virus("PC Files: virus.exe, bestmalware.exe, memzvirus.exe"))