"""
Who Won the League?
The 2019/20 season of the English Premier League (EPL) saw Liverpool FC win the title for the first time despite their bitter rivals, Manchester United, having won 13 titles!

Create a function that receives an alphabetically sorted array of the results achieved by each team in that season and the name of one of the teams. The function should return a string giving the final position of the team, the number of points achieved and the goal difference (see examples for precise format).

The results table is given in the following format:

Team	Played	Won	Drawn	Lost	G/Diff
Arsenal	38	14	14	10	8
Aston Villa	38	9	8	21	-26
Bournemouth	38	9	7	22	-26
Brighton	38	9	14	15	-15
Burnley	38	15	9	14	-7
Chelsea	38	20	6	12	15
Crystal Palace	38	11	10	17	-19
Everton	38	13	10	15	-12
Leicester City	38	18	8	12	26
Liverpool	38	32	3	3	52
Manchester City	38	26	3	9	67
Manchester Utd	38	18	12	8	30
Newcastle	38	11	11	16	-20
Norwich	38	5	6	27	-49
Sheffield Utd	38	14	12	12	0
Southampton	38	15	7	16	-9
Tottenham	38	16	11	11	14
Watford	38	8	10	20	-28
West Ham	38	10	9	19	-13
Wolves	38	15	14	9	11
Examples
table = [
  ["Arsenal", 38, 14, 14, 10, 8],
  ["Aston Villa", 38, 9, 8, 21, -26],
  ...
  ...
  ["West Ham", 38, 10, 9, 19, -13],
  ["Wolves", 38, 15, 14, 9, 11]
]

EPLResult(table, "Liverpool")
  ➞ "Liverpool came 1st with 99 points and a goal difference of 52!"

EPLResult(table, "Manchester Utd")
  ➞ "Manchester Utd came 3rd with 66 points and a goal difference of 30!"

EPLResult(table, "Norwich")
  ➞ "Norwich came 20th with 21 points and a goal difference of -49!"
Notes
Score 3 points for a win and 1 point for a draw.
If teams are tied on points, their position is determined by better goal difference.
The input table should be considered immutable - do not make any changes to it!
"""

table = [
	['Arsenal', 38, 14, 14, 10, 8],
	['Aston Villa', 38, 9, 8, 21, -26],
	['Bournemouth', 38, 9, 7, 22, -26],
	['Brighton', 38, 9, 14, 15, -15],
	['Burnley', 38, 15, 9, 14, -7],
	['Chelsea', 38, 20, 6, 12, 15],
	['Crystal Palace', 38, 11, 10, 17, -19],
	['Everton', 38, 13, 10, 15, -12],
	['Leicester City', 38, 18, 8, 12, 26],
	['Liverpool', 38, 32, 3, 3, 52],
	['Manchester City', 38, 26, 3, 9, 67],
	['Manchester Utd', 38, 18, 12, 8, 30],
	['Newcastle', 38, 11, 11, 16, -20],
	['Norwich', 38, 5, 6, 27, -49],
	['Sheffield Utd', 38, 14, 12, 12, 0],
	['Southampton', 38, 15, 7, 16, -9],
	['Tottenham', 38, 16, 11, 11, 14],
	['Watford', 38, 8, 10, 20, -28],
	['West Ham', 38, 10, 9, 19, -13],
	['Wolves', 38, 15, 14, 9, 11]
]

import numpy as np

def EPLResult(table, team):
	result = sorted(table, key=lambda x: ((x[2] * 3) + (x[3] * 1), x[5]), reverse=True)
	for i, l in enumerate(result, 1):
		if l[0] == team:
			return '{} came {}{} with {} points and a goal difference of {}!'.format(team, i,
				 "st" if i == 1 else "nd" if i == 2 else "rd" if i == 3 else "th",
				 l[2] * 3 + l[3] * 1, l[-1])


# # ポイント計算とゴール差を結合して新しいリストを作成
	# table = [[i[0], i[2] * 3 + i[3], i[5]] for i in table]
	#
	# # ポイント数とゴール差で降順ソート
	# sorted_table = sorted(table, key=lambda x:(x[1], x[2]), reverse=True)
	#
	# # チームの位置を検索
	# team_position = np.where(np.array(sorted_table)[:, 0] == team)[0][0] + 1
	#
	# # 順位の表現を取得
	# def ordinal(n):
	# 	return "%d%s" % (n, "tsnrhtdd"[((n // 10) % 10 != 1) * (n % 10 < 4) * n % 10::4])
	#
	# # チームの成績をフォーマットして返す
	# for position, data in enumerate(sorted_table, start=1):
	# 	if position == team_position:
	# 		return "{} came {} with {} points and a goal difference of {}!".format(data[0], ordinal(position), data[1], data[2])


print(EPLResult(table, "Liverpool"))
print(EPLResult(table, "Manchester Utd"))
print(EPLResult(table, "Norwich"))
print(EPLResult(table, "Tottenham"))
print(EPLResult(table, "Aston Villa"))
print(EPLResult(table, "Southampton"))
print(EPLResult(table, "Manchester City"))
