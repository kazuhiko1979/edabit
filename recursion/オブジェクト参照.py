import datetime

class Person:
    def __init__(self, firstName, lastName, heightM , weightKg,
                 birthYear):

        self.firstName = firstName
        self.lastName = lastName
        self.heightM = heightM
        self.weightKg = weightKg
        self.birthYear = birthYear


    def getStateString(self):
        return "First Name: " + self.firstName \
               + ", Last Name: " + self.lastName \
               + ", heightM: " + str(self.heightM) \
               + ", weightKg: " + str(self.weightKg) \
               + ", birthYear: " + str(self.birthYear)


    def getFullName(self):
        return self.firstName + " " + self.lastName

    def getAge(self):
        currentYear = datetime.datetime.now().year
        return currentYear - self.birthYear

    def getBmi(self):
        return self.weightKg / (self.heightM ** 2)


# def changePersonState(person):
#
#     person.firstName = "Denice"
#     person.lastName = "Harrison"
#     return person.getFullName()

def changePersonState(inputPerson):

    inputPerson = Person(inputPerson.firstName,
                         inputPerson.lastName,
                         inputPerson.heightM,
                         inputPerson.weightKg,
                         inputPerson.birthYear)

    inputPerson.firstName = "Denice"
    inputPerson.lastName = "Harrison"
    return inputPerson.getFullName()



carly = Person("Carly", "Angelo", 1.72, 85.5, 1996)

print(carly)
print(carly.getStateString())

# オブジェクト参照渡し
print(changePersonState(carly))

print(carly.getStateString())


"""
通常の値渡し例
"""
def square(x):
    x = x * x
    return x

num = 34
print(num)
print(square(num))

print(num)









