"""
BCTC ------ AVGCTC --------- WCTC
O(nlog(n))         O(nlog(n))         O(nlog(n))

"""


def merge_sort(lst):
    if len(lst)>1:
        mid_index=len(lst)//2
        left_half=lst[:mid_index]
        right_half=lst[mid_index:]
        # print(left_half, right_half)
        merge_sort(left_half)
        merge_sort(right_half)
        i=0
        j=0
        k=0
        #print("***",len(left_half), len(right_half))
        while i < len(left_half) and j < len(right_half):
            if left_half[i]<right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k]=right_half[j]
                j += 1
            k += 1
        # print(lst)
        while i<len(left_half):
            lst[k]=left_half[i]
            i +=1
            k +=1
        while j<len(right_half):
            lst[k]=right_half[j]
            j += 1
            k += 1
        print(lst)
nm=[2, 5, 3, 4, 7, 3, 8, 5]
merge_sort(nm)
