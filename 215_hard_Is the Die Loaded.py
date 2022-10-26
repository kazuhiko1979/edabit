"""
Is the Die Loaded
The Chi-Squared (χ²) goodness of fit test estimates if an empirical (observed) distribution fits a theoretical (expected) distribution within reasonable margins. For example, to figure out if a die is loaded you could roll it many times and note the results. Because of randomness, you can't expect to get the same frequency for all faces, but if one or more faces turn up much more frequently than some others, it is reasonable to assume the die is loaded.

The formula to calculate the Chi-Square parameter is:

Chi-squared

Below is an example of a die rolled 600 times:

Face	1	2	3	4	5	6
Observed frequency	101	116	89	108	97	89
Expected frequency	100	100	100	100	100	100
Difference	1	16	-11	8	-3	-11
In this example, the Chi-Square parameter has a value of:

χ² = ((1)^2 + (16)^2 + (-11)^2 + (8)^2 + (-3)^2 + (-11)^2) / 100 = 5.72
This parameter is then compared to a critical value, calculated taking into account the number of categories and the confidence level. Here, the critical value is 11.0705. Since 5.72 < 11.0705, it is safe to assume the die is unloaded.

Given a list with the six observed frequencies, write a function that returns True if a die is unloaded, or False if it is loaded. Take 11.0705 as the critical value for all cases.

Examples
fair_die([44, 52, 33, 40, 41, 30]) ➞ True
(χ² = 7.75) < 11.0705

fair_die([34, 27, 23, 20, 32, 28]) ➞ True
(χ² = 1.6) < 11.0705

fair_die([10, 20, 11, 5, 19, 16]) ➞ False
(χ² = 12.556) > 11.0705
"""
# v2
critical = 11.0705

def fair_die(lst):

	expected = sum(lst) / 6.0
	chi_sq = sum([(obs - expected) ** 2 for obs in lst]) / expected
	return chi_sq < critical

# v1
# def fair_die(lst):
#
# 	expected_freq = ([i / j * (sum(lst) / len(lst)) for i, j in zip(lst, lst)])
# 	value = round(sum([abs(o-e) ** 2 for o, e in zip(lst, expected_freq)]) / (sum(lst) / len(lst)), 2)
# 	return value < 11.0705

print(fair_die([8, 10, 5, 15, 15, 10]))
print(fair_die([21, 22, 17, 31, 29, 30]))
print(fair_die([8, 16, 16, 9, 11, 3]))
print(fair_die([14, 10, 16, 14, 15, 15]))
print(fair_die([7, 18, 15, 21, 14, 28]))
print(fair_die([29, 34, 33, 38, 41, 35]))
print(fair_die([10, 20, 11, 5, 19, 16]))
