"""
Create a function that takes a country's name and its area as arguments and returns the area of the country's proportion of the total world's landmass.

Examples
area_of_country("Russia", 17098242) ➞ "Russia is 11.48% of the total world's landmass"
area_of_country("USA", 9372610), "USA is 6.29% of the total world's landmass"
area_of_country("Iran", 1648195) ➞ "Iran is 1.11% of the total world's landmass"

The total world's landmass is 148,940,000 [Km^2]
"""
def area_of_country(name, area):

    landmass = 148940000

    return "{} is {}% of the total world's landmass".format(name, round(area / landmass * 100, 2))

print(area_of_country("Russia", 17098242))
print(area_of_country("USA", 9372610))
print(area_of_country("Iran", 1648195))

