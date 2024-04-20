a=input("Enter your string:")
replacevalue=(input("user input:"))
indexvalue=int(input("Enter the before index value:")) 
secsplit=int(input("Enter the after index value:"))
if indexvalue <= len(a): 
    list=[]
    for i in a:
       list.append(i)
    z=a[:indexvalue-1]
    b=a[secsplit:]
    print(z+replacevalue+b)
else:
    print("index value is out off range")





