# list to dictionary convert

lst=[1,4,2,4,5,6]
for i in range(len(lst)):
    dict(i=lst[i])
print(a)

# ------------- 2nd process --------------

lst=[1,4,2,4,5,6]
a={i:lst[i] for i in range(len(lst))}
# type(a)
print(a)
