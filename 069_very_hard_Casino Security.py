"""
Casino Security
You're head of security at a casino that has money being stolen from it. You get the data in the form of strings and you have to set off an alarm if a thief is detected.

If there is no guard between thief and money, return "ALARM!"
If the money is protected, return "Safe"
String Components
x - Empty Space
T - Thief
G - Guard
$ - Money
Examples
security("xxxxTTxGxx$xxTxxx") ➞ "ALARM!"

security("xxTxxG$xxxx$xxxx") ➞ "Safe"

security("TTxxxx$xxGxx$Gxxx") ➞ "ALARM!"
Notes
Money at the extremes are safe.
"""

def security(data):
#     money_index = data.find("$")
#     thief_index = data.find("T")
#     while thief_index != -1:
#         if money_index > thief_index:
#             if "G" not in data[thief_index:money_index]:
#                 return "ALARM!"
#         thief_index = data.find("T", thief_index + 1)
#     return "Safe"
#
# print(security("xxTxxx$xxxTxxxGxxT"))
# print(security("xGxx$xxGxxxTTT"))
# print(security("TxGxx$xxx$xxxGxxT"))
# print(security("GxxxTxxGxxTxx$xx$xxTxxG"))

