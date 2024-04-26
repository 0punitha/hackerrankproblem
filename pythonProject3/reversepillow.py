list_1=[1,2,3,4]
list_2=[]
count=0
n=int(input("enter n value:"))
time=int(input("enter the times:"))
for j in range(n):
    pass
for i in list_1:
    list_2.append(i)
    a=(list_2[3-1::-1])
list_3=list_1+a
for i in list_3:
    count+=1
    if count==time:
        print("pillow having person:",list_3[time])