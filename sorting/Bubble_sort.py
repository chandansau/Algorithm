def bubble_sort(num):
    n = len(num)
    for i in range(n):
        for j in range(n-i-1):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]

    return num


nu = [2, 8, 4, 6, 9, 7, 8]
bubble_sort(nu)
print(nu)
