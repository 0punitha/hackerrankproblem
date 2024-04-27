count=int(input("enter a number:"))
list_1=[]
male="male"
Female="female"
married="married"
for i in range(1,count+1):
    a=input("enter a name ,age ,gender,marrital status:")
    b=a.split(" ")
    list_1.append(b)
for i in list_1:
    #print(i[0])
    if i[2]== male:
        print("Mr",i[0])
    elif(i[3]==married and i[2]==Female ):
        print("Mrs",i[0])
    else:
        print("Miss",i[0])
else:
    print("Transgender",i[0])



