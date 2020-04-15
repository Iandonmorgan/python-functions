
for i in range(101):
    if i == 0:
        print(i)
    elif i % 5 == 0 and i % 7 == 0:
        print("ChickenMonkey")
    elif i % 5 == 0:
        print("Chicken")
    elif i % 7 == 0:
        print("Monkey")
    else:
        print(i)