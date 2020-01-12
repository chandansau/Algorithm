# search all duplicate number from the list
a=[1,1,1,2,3,4,5,6,9,6,5,7,8,9,10,10]
a.sort()
list(set([i for i in a if a.count(i)>=2]))
