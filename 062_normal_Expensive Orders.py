"""
Write a function that has two parameters: orders and cost. Return any orders that are greater than the cost.

Examples
expensive_orders({ "a": 3000, "b": 200, "c": 1050 }, 1000)
➞ { "a": 3000, "c": 1050 }

expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000)
➞ { "Gucci Fur": 24600 }

expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40)
➞ {}
"""

def expensive_orders(orders, cost):

    # return {key: val for key, val in orders.items() if val > cost}

    result = {}
    for key, value in orders.items():
        if value > cost:
            result[key] = value
    return result


print(expensive_orders({"a": 3000, "b": 200, "c": 1050}, 1000))
print(expensive_orders({ "Gucci Fur": 24600, "Teak Dining Table": 3200, "Louis Vutton Bag": 5550, "Dolce Gabana Heels": 4000 }, 20000))
print(expensive_orders({ "Deluxe Burger": 35, "Icecream Shake": 4, "Fries": 5 }, 40))



