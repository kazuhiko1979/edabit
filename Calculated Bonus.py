"""
A financial institution provides professional services to banks and claims charges from the customers based on the number of man-days provided. Internally, it has set a scheme to motivate and reward staff to meet and exceed targeted billable utilization and revenues by paying a bonus for each day claimed from customers in excess of a threshold target.

This quarterly scheme is calculated with a threshold target of 32 days per quarter, and the incentive payment for each billable day in excess of such threshold target is shown as follows:

Days	Bonus
0 to 32 days	Zero
33 to 40 days	SGD$325 per billable day
41 to 48 days	SGD$550 per billable day
Greater than 48 days	SGD$600 per billable day
Please note that incentive payment is calculated progressively. As an example, if an employee reached total billable days of 45 in a quarter, his/her incentive payment is computed as follows:

32*0 + 8*325 + 5*550 = 5350
Write a function to read the billable days of an employee and return the bonus he/she has obtained in that quarter.

Examples
bonus(15) ➞ 0

bonus(37) ➞ 1625

bonus(50) ➞ 8200
"""


def bonus(days):

    # zero_bonus_days = 32
    # d33_d40_days = 8
    # d41_d48_days = 8
    # than_48_days = days - 48
    #
    # if days >= 49:
    #     total = ((zero_bonus_days * 0) + (d33_d40_days * 325) + (d41_d48_days * 550) + (than_48_days * 600))
    # elif days >= 41 and days <= 48:
    #     d41_d48_days = days - 40
    #     total = ((zero_bonus_days * 0) + (d33_d40_days * 325) + (d41_d48_days * 550))
    # elif days >= 33 and days <= 40:
    #     d33_d40_days = days - 32
    #     total = ((zero_bonus_days * 0) + (d33_d40_days * 325))
    # else:
    #     total = 0
    #
    # return total

    max_days = 48
    app_days = days - 32
    list_days = [i for i in range(1, app_days + 1)]
    list_prices = [325, 325, 325, 325, 325, 325, 325, 325, 550, 550, 550, 550, 550, 550, 550, 550,]
    list_dict = dict(zip(list_days, list_prices))

    if days <= 32:
        return 0

    if app_days <= 16:
        for i in list_dict.keys():
            if i == app_days:
                sub_total = sum(list_dict.values())
                return sub_total

    if app_days >= 17:
        days = days - max_days
        return days * 600 + 7000

print(bonus(48))
print(bonus(45))
print(bonus(37))
print(bonus(50))
print(bonus(15))
