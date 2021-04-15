"""
0 represents the dog.
Each list represents a house and each 1 represents an empty room.
Return the house and the room where it is located, there can be only one dog lost per building.
Examples
lost_dog([1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ "Dog not found!"

lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1])
➞ {"Dog1": "House (2) and Room (1)", "Dog2": "House (3) and Room (2)"}

lost_dog([1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1])
➞ {"Dog1": "House (1) and Room (6)", "Dog2": "House (2) and Room (1)", "Dog3": "Ho
"""
# import numpy as np
#
# lst = [[1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1]]
#
# # lst = [[1, 1, 1, 1, 1, 0],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 0, 1, 1, 1]]
#
# arr = np.array(lst)
# locate = np.argwhere(arr==0)
# # print(locate)
# num_locate = int(len(locate))
#
# n_locate =[i for i in range(1, num_locate+1)]
# # print(n_locate)
#
# for key, value in locate:
#     # print("House({}) and Room ({})".format(key+1, value+1))
#
#     key = ([i for i in range(key)])
#     value = ([j for j in range(value)])
#     print(key)
#     print(value)
#     # d = {"Dog{}".format(k): v1 for k, v1 in zip(n_locate, score)}
#
#     # d = {"Dog{}".format(k): v1+1 for k, v1, v2 in zip(n_locate, key, value)}
#     d = {"Dog{}".format(k): (v1+1) for k, v1, v2 in zip(n_locate, key, value)}
#     print(d)


def lost_dog(*houses):

	dogs = {}

	for i,e in enumerate(houses):

		if 0 in e:
			dogs['Dog{}'.format(len(dogs)+1)] = 'House ({}) and Room ({})'.format(i+1,e.index(0)+1)
	return dogs if len(dogs)>0 else 'Dog not found!'


print(lost_dog([1, 1, 1, 1, 1, 1],  [0, 1, 1, 1, 1, 1],  [1, 0, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1]))











