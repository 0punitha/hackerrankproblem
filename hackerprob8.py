x=int(input("x value:"))
y=int(input("y value:"))
z=int(input("z value:"))
n=int(input("add value:"))
list=[]
for i in range(0,x+1):
    for j in  range(0,y+1):
        for k in  range(0,z+1):
            list.append([i+j+k])
            if(i+j+k != n):
                print([i,j,k],end=" ") 
            