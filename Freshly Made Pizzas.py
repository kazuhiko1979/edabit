"""
Create a Pizza class with the attributes order_number and ingredients (which is given as a list). Only the ingredients will be given as input.

You should also make it so that its possible to choose a ready made pizza flavour rather than typing out the ingredients manually! As well as creating this Pizza class, hard-code the following pizza flavours.

Name	Ingredients
hawaiian	ham, pineapple
meat_festival	beef, meatball, bacon
garden_feast	spinach, olives, mushroom
Examples
p1 = Pizza(["bacon", "parmesan", "ham"])    # order 1
p2 = Pizza.garden_feast()                  # order 2
p1.ingredients ➞ ["bacon", "parmesan", "ham"]

p2.ingredients ➞ ["spinach", "olives", "mushroom"]

p1.order_number ➞ 1

p2.order_number ➞ 2
Notes
All words are given in lowercase.
See the Resources tab for some helpful tutorials on classes!
"""

class Pizza:

    order = 0

    def __init__(self, ingredients):

        self.ingredients = ingredients
        self.order_number = self.orderNumber()


    @staticmethod
    def orderNumber():
        Pizza.order += 1
        return Pizza.order


    @staticmethod
    def hawaiian():
        return Pizza(['ham', 'pineapple'])

    @staticmethod
    def garden_feast():
        return Pizza(['spinach', 'olives', 'mushroom'])

    @staticmethod
    def meat_festival():
        return Pizza(['beef', 'meatball', 'bacon'])


p1 = Pizza(["bacon", "parmesan", "ham"])
p2 = Pizza.garden_feast()
p3 = Pizza.hawaiian()
p4 = Pizza.meat_festival()
p5 = Pizza(["pepperoni", "bacon"])
my_pizza = Pizza(["cheese", "caviar", "oyster", "uranium"])

print(p1.ingredients)
print(p2.ingredients)
print(p3.ingredients)
print(p4.ingredients)
print(p5.ingredients)


print(my_pizza.ingredients)
print(p1.order_number)
print(p2.order_number)
print(p3.order_number)
print(p4.order_number)
print(p5.order_number)
print(my_pizza.order_number)











