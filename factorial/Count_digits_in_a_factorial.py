# floor(digits) + 1;
import math
n = 10
digits = int(input("Enter a int value\t"))
for i in range(2, n + 1):
    digits += math.log10(i)

print(math.floor(digits) + 1)
