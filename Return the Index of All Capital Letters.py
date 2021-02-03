"""
Create a function that takes a single string as argument and returns an ordered list containing the indices
of all capital letters in the string.

Examples
index_of_caps("eDaBiT") ➞ [1, 3, 5]
index_of_caps("eQuINoX") ➞ [1, 3, 4, 6]
index_of_caps("determine") ➞ []
index_of_caps("STRIKE") ➞ [0, 1, 2, 3, 4, 5]
"""
def index_of_caps(word):

    print([index for index, letter in enumerate(word) if letter.isupper()])
    # print([i for i, x in enumerate(word) if x.isupper()])

index_of_caps("eDaBiT")
index_of_caps("eQuINoX")
index_of_caps("determine")
index_of_caps("STRIKE")
index_of_caps("sUn")
index_of_caps("SpiDer")
index_of_caps("accOmpAnY")
index_of_caps("@xCE#8S#i*$en")
index_of_caps("1854036297")
index_of_caps("Fo?.arg~{86tUx=|OqZ!")

