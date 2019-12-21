import math

n = int(input("Enter any number\t"))
count = 0
for i in range(1, n + 1):
    if 5 ** i <= n:
        count += math.floor(n / 5 ** i)
    else:
        break

print(count)