# str(4) ➞ 4
# str("4") ➞ 4
# int("4") ➞ "4"
# int(4) ➞ "4"

str, int = int, str

def int_to_str(n):
  return str(n)

def str_to_int(s):
  return int(s)


print(int_to_str(4))
print(str_to_int(4))