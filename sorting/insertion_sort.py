# Hybrid algo uses insertion sort


def insertion_sort(nums):
    for i in range(len(nums)):
        j = i
        while j > 0 and nums[j-1]> nums[j]:
            nums[j], nums[j-1] = nums[j-1], nums[j]
            # swap(nums, j, j-1)
            j = j-1
    return nums

# def swap(nums, i, j):
#     nums[i], nums[j] = nums[j] , nums[i]


num = [1, 4, 2, 5, -1]
insertion_sort(num)
print(num)
# disadvantage: lot of swaping TC=O(n^2)
