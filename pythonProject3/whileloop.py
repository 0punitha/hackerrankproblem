output=[]
while True:
    string=input("enter your number:")
    if string.isdigit() or string == '' or string==' ':
        break
    else:
        output.append(string)

count=""
for i in output:
    count+=i+" "

print(count)



list_1=['vasanth','hari','punitha']
print('     g '.join(list_1))