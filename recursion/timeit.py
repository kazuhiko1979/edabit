import random
import time
import datetime

start = datetime.datetime.now()
dataset = []
for _ in range(100000):
    dataset.append(random.randint(1, 1000000))
end = datetime.datetime.now()
print(end - start)


start = datetime.datetime.now()
result = [random.randint(1, 1000000) for _ in range(100000)]
# print(result)
end = datetime.datetime.now()
print(end - start)

students = ['imanish','imayu', 'saito', 'suzuki', 'tanaka']

# for
new_students = []
for student in students:
    new_students.append(student.upper())
print(new_students)

#　内包表記
print([student.upper() for student in students])

# lambda & map
func = list(map(lambda student: student.upper(), students))
print(func)


