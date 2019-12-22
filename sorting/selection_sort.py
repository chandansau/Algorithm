"""
BCTC ------ AVGCTC --------- WCTC
O(n^2)      O(n^2)          O(n^2)

"""

def selection_sort(nums):
    for i in range(len(nums)):
        index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[index]:
                index = j
        if index != i:
            nums[i], nums[index] = nums[index], nums[i]  # swaping the elements
            # swap(nums, index, i)
    return nums


# def swap(nums, j, i):
#     nums[i] , nums[j]= nums[j], nums[i]


num = [2, 4, 1, 9, -1]
selection_sort(num)  # TC = O(n^2) its similar to Bubble sort
print(num)
