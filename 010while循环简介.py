print ("Enter 'q' to quit.")
while True:
    age = input("Enter your age: \n")
    if age == 'q':
        print("Quit!")
        break
    if int(age) <= 3:
        print("Free")
    elif int(age) <=12:
        print("10 Dollars")
    else:
        print("15 Dollars")
