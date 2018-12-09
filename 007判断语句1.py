
age = int(input("Enter your age:\n"))


if age <= 9:
    print("You cannot play this game.")
elif age > 9 and age <= 18:
    print("You can play 2 hours.")
else:
    print("You can play this game free.")
