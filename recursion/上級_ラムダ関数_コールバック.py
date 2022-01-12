"""
簡単な同期型コールバックは以下のようになります。
"""

def synchronousFunction(f, x):
    results = f(10)
    return f(x) + f(x * x) + results

def printSynchronous():
    def f(x):
        print("Call on " + str(x))
        return int(x / 2)

    return f

print(synchronousFunction(printSynchronous(), 254))



