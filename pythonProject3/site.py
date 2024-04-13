list_1 = ['a', 'b', 'in', 's', 'sdy', 4, 5, 'punitha']

for i in list_1:
    if isinstance(i, str):  # Check if the element is a string
        if len(i) >= 2:  # Check if the length of the string is >= 2
            for j in i:  # Iterate over each character in the string
                if j not in ['a', 'e', 'i', 'o', 'u']:  # Check if it's a consonant
                    print(j)