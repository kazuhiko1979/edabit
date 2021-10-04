"""
素数
easy
Kate は音楽の野外フェスを行うことになり、入場者の中から抽選でプレゼントを渡す企画を立てています。
そこで、素数の値で入場した方を当選者とすることにしました。
入場者番号 number が与えられるので、素数かどうか判定する isPrime という関数を作成してください。
"""
def isPrime(number):

    if number == 1:
        return False

    for p in range(2, number):
        if number % p == 0:
            return False
    return number

print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(25))
print(isPrime(29))
print(isPrime(36))
print(isPrime(45))
print(isPrime(85))
print(isPrime(455))




