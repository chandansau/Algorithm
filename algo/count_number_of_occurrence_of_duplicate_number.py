# count number of occurrence of duplicate number 
a=[1,1,1,2,3,4,5,6,9,6,5,7,8,9]
b=[]
for i in a:
    if a.count(i)>=2 and i not in b:
        b.append(i)
        print(i,"<--->",a.count(i))
