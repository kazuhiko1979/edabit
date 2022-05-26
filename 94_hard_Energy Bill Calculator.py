"""
Energy Bill Calculator
Create a function that calculates an energy bill.

Given a billing start date and end date, start and end meter reading, a unit price in pence, and a standing charge (a daily rental fee for your meter) as arguments, calculate your bill.

An energy bill is calculated by multiplying the difference between meter readings with the unit price and adding the number of days multiplied by the standing charge. You then have to add 5% tax.

(days between dates x standing charge) + (diference bewteen meter readings x unit price) + 5% tax

Examples
energy_bill("2020,01,01", "2020,04,01", 1000, 2000, 0.188, 0.243),  = "$220.62"
"2020,04,01" (end date) - "2020,01,01" ( start date ),  = 91 days
  2000 ( end meter read )- 1000 ( start meter read ) = 1000 units used
  1000 (units) * 0.188p (each unit cost) = $188
  91 (days) * 0.243p (standing charge) == $22.113
  22.113 (Total standing charge cost) + $188 (total unit cost) = $210.113
  210.113 (cost) * 0.05 (uk tax on energy) = 10.50565
  210.113 (cost) + 10.50565 (tax) = 220.61865
  answer = "$220.62"
Notes
If the end date is an earlier date from the start date return "Invalid date".
If the end meter reading is less then the start meter reading return "Invalid meter readings".
Please bring to my attention any clarity issues.
"""
from datetime import datetime

def energy_bill(start_date, end_date, start_read, end_read, tariff, stand):


	# v2
	start_date = datetime.strptime(start_date, "%Y,%m,%d")
	end_date = datetime.strptime(end_date, "%Y,%m,%d")
	if end_date < start_date:
		return "Invalid date"
	if end_read < start_read:
		return "Invalid meter readings"

	res = ((end_read - start_read) * tariff + (end_date - start_date).days * stand) * 1.05
	return "${:.2f}".format(res)


	# v1
	# start_date = datetime.strptime(start_date.replace(',', '-'), '%Y-%m-%d')
	# end_date = datetime.strptime(end_date.replace(',', '-'), '%Y-%m-%d')
	#
	# diff_days = (end_date - start_date).days
	#
	# if diff_days > 0:
	# 	units = end_read - start_read
	# 	if units >= 0:
	# 		total_units_cost = units * tariff
	# 		total_standing_charge_cost = diff_days * stand
	# 		cost = total_standing_charge_cost + total_units_cost
	# 		tax = cost * 0.05
	# 		return '$' + str(round(cost + tax, 2))
	# 	else:
	# 		return "Invalid meter readings"
	# else:
	# 	return "Invalid date"


print(energy_bill("2020,01,01", "2020,04,01", 1000, 2000, 0.188, 0.243))
print(energy_bill("1987,11,01", "1989,02,21", 874, 6253, 0.061, 0.124))
print(energy_bill("2011,09,02", "2012,09,05", 3297, 4721, 0.151, 0.176))
print(energy_bill("2010,01,01", "2020,01,01", 2000, 2000, 0.171, 0.213))
print(energy_bill("1984,04,19", "1991,04,10", 2000, 1000, 0.61, 0.074))
print(energy_bill("2020,01,01", "2019,01,01", 1000, 2000, 0.171, 0.243))

