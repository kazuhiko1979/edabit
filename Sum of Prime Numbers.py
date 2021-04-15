"""
Create a function that takes a list of numbers and returns the sum of all prime numbers in the list.

Examples
sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) ➞ 17

sum_primes([2, 3, 4, 11, 20, 50, 71]) ➞ 87

sum_primes([]) ➞ None
Notes
Given numbers won't exceed 101.
A prime number is a number which has exactly two divisors.
"""
def sum_primes(lst):

    prime_list = []

    for j in lst:
        if j > 1:
            for i in range(2, int(j/2)+1):
                if j % i == 0:
                    break
            else:
                prime_list.append(j)

    if sum(prime_list) == 0:
        return None
    else:
        return sum(prime_list)

print(sum_primes([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(sum_primes([2, 3, 4, 11, 20, 50, 71]))
print(sum_primes([]))






