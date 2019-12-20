numbers = [1, 2, 2, 4, 4, 5]
for i in numbers:
    if numbers.count(i) == 1:
        numbers.remove(i)

print(numbers)
