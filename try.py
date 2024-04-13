list=[]
a=[]
for i in range(1,6):
    score=int(input("enter the value:"))
    a.append(score)
b=(max(a))
#print(b)
for i in a:
    if b>i:
        #print("b is greatr than i value:",i)
        list.append(i)
       
    '''else:
        print("i value is greater:",i)'''
#print(list)
print("The runner is:",max(list))
