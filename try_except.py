
while True:
    try:
        age = int(input("What is your age ? "))
        break
    except:
        print("Please enter a number!")

if age < 15:
    print("You are too young!")


