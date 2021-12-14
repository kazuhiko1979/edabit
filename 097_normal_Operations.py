"""
Operations
Write a function that does the following things: adding, subtracting, dividing, or multiplying values. It is simply referred to as variable operation variable. Of course, the variables have to be defined, but in this challenge, the variable will be defined for you. All you have to do is look at the variable, do some string to integer conversions use some if conditionals, and combine them based on the operation.

The numbers and operation will be given as a string, and you should return the value as a string as well.

Examples
operation("1", "2", "add" ) ➞ "3"

operation("4", "5", "subtract") ➞ "-1"

operation("6", "3", "divide") ➞ "2"
Notes
The numbers and operation will be given as a string, and you should also return the value as a string.
If the answer is "undefined", return "undefined" (e.g. dividing by zero).
For divide go ahead and round down to an integer.
"""

def operation(a, b, op):

  # try:
  #   return str(round(eval(a + {'a':'+', 's':'-', 'd':'/', 'm':'*'}[op[0]] + b)))
  # except:
  #   return "undefined"

  d = {'add': '+', 'subtract': '-', 'multiply': '+', 'divide': '//'}
  x = d.get(op)

  try:
    return str(eval(a+x+b))
  except:
    return 'undefined'



# if op == "add":
  #   return str(int(a) + int(b))
  # elif op == "subtract":
  #   return str(int(a) - int(b))
  #
  # elif op == "divide":
  #   try:
  #     return str(round(int(a) / int(b)))
  #   except:
  #     return "undefined"
  #
  # elif op == "multiply":
  #   try:
  #     return str(round(int(a) * int(b)))
  #   except:
  #     return "undefined"


print(operation("1", "2", "add"))
print(operation("4", "5", "subtract"))
print(operation("6", "3", "divide"))

print(operation("10", "10", "subtract"))
print(operation("0", "0", "subtract"))

print(operation("0", "1", "divide"))
print(operation("0", "25415", "divide"))

print(operation(operation("10", "10", "multiply"),operation("10","10","add"),"divide"))