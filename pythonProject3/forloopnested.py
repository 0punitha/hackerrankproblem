list_1=['a','b','in','s','sdy',4,5,'punitha']
count=""
list_2=[]
for i in list_1:
    if (type(i)==str):
        for j in i:
            if j not in ['a','e','i','o','u']:
                count+=j
                print(count)
        list_2.append(count)
        count=""
print(list_2)
for i in list_2:
    if i != '':
        print(i[::-1])












