number=list("123456789")
letters=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
output=[]
while True:
    a=input("enter the number:")
    if a in number or a=="10":
        output.append(int(a))
    elif a in letters :
        continue
    else:
        break

print(output)
print(sum(output))