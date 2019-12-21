# memorization concept


def fact(n):
    c = 1
    for i in range(1, n+1):
        c = c*i
    return c


n = int(input("Enter any number\t"))
print(fact(n))


# -------------------2nd process ---------------------------

import math
print(math.factorial(n))
