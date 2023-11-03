try:
    age = int(input("write your age: "))
except ValueError:
    print("Value Error")
else:
    if age <=21:
        print("You can't smoke cigarettes")
    else:
        print("You can smoke cigarettes")