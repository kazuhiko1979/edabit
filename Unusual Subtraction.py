def not_good_math(n, k):

    i = 0
    while i < k:
        if n % 10 == 0:
            n = n // 10
        else:
            n = n - 1

        i = i + 1
    return n

print(not_good_math(540, 5))
print(not_good_math(1000000000, 9))
print(not_good_math(42023110, 10))
