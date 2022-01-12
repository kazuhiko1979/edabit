"""
Leaderboard Sort
Given an array of users, each defined by an object with the following properties: name, score, reputation create a function that sorts the array to form the correct leaderboard.

The leaderboard takes into consideration the score of each user of course, but an emphasis is put on their reputation in the community, so to get the trueScore, you should add the reputation multiplied by 2 to the score.

Once you know the trueScore of each user, sort the array according to it in descending order.

Examples
leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]) ➞ [
  { "name": "c", "score": 115, "reputation": 30 },  # trueScore = 175
  { "name": "b", "score": 90, "reputation": 40 },   # trueScore = 170
  { "name": "a", "score": 100, "reputation": 20 }   # trueScore = 140
]
"""

def leaderboards(users):



    # return sorted(users, key = lambda i: (i['score']+i['reputation']*2), reverse=True)

    # users_list = []
    #
    # for i in users:
    #     i["trueScore"] = i.get("score") + i.get("reputation") * 2
    #     users_list.append(tuple(i.items()))
    #
    # sorted_users = sorted(users_list, key = lambda kv: kv[3], reverse=True)
    #
    # return [{'name': dict(i)['name'], 'score': dict(i)['score'], 'reputation': dict(i)['reputation']} for i in
    #         sorted_users]


print(leaderboards([
  { "name": "a", "score": 100, "reputation": 20 },
  { "name": "b", "score": 90, "reputation": 40 },
  { "name": "c", "score": 115, "reputation": 30 },
]))


print(leaderboards([
    { 'name': 'tkincaid0', 'score': 4128, 'reputation': 3002 },
    { 'name': 'sblackater1', 'score': 6208, 'reputation': 3050 },
    { 'name': 'ocallis2', 'score': 6883, 'reputation': 3812 },
    { 'name': 'shoofe3', 'score': 4900, 'reputation': 174 },
    { 'name': 'cbrazear4', 'score': 7862, 'reputation': 2940 },
    { 'name': 'oszachnie5', 'score': 6217, 'reputation': 1772 },
    { 'name': 'lingcourt6', 'score': 5746, 'reputation': 1263 },
    { 'name': 'tquincey7', 'score': 4209, 'reputation': 1419 },
    { 'name': 'mcapsey8', 'score': 6961, 'reputation': 2699 },
    { 'name': 'cbester9', 'score': 4090, 'reputation': 3934 },
  ]))