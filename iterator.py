def pick_fruits(x):
    fruits = ['apple','banana','grape','orange']
    return fruits[x]

list1 = [1,3,2,0,3,2,1,3,2]
choices = map(pick_fruits, list1)
print(choices)
for choice in choices:
    print(choice)


