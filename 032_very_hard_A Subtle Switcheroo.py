"""
A Subtle Switcheroo
Create a function which replaces all instances of "nts" with "nce" and vice versa if they are at the end of a word.

Examples
switcheroo("The elephants in France were chased by ants!") ➞ "The elephance in Frants were chased by ance!"

switcheroo("While he rants, I fall into a trance...") ➞ "While he rance, I fall into a trants..."

switcheroo("Bounced over the fence!") ➞ "Bounced over the fents!"
Notes
Empty strings should return just an empty string (see example #2).
Ignore punctuation and any instances where "nts" or "nce" are not at the end of a word (see example #3).
"""
import re

def switcheroo(txt):

	# v2
	return re.sub(r'(nts|nce)(?=\W)', lambda x: 'nts' if x.group(1) == 'nce' else 'nce', txt)

	# v1
	# replacement = {'nts':'nce', 'nce':'nts'}
	# ans = re.sub(r'n[cets]+\b', lambda x:replacement[x.group(0)],txt)
	# return ans
	
print(switcheroo("The elephants in France were chased by ants!"))
