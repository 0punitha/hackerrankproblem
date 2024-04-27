alpha="abcdefghijklmnopqrstuvwxyz"
list_1=[]
count=0
for i in alpha:
    list_1.append(i)
print(list_1)
inputstr=input("enter the value:")
for j in inputstr:
    if j in list_1:
       a=(list_1.index(j)+1)+2
       print(list_1[a-1])

     
   

