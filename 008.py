list_1 = ["1","2","4","5","6"]
list_2 = ["1","3","5","7","9"]
for number in list_2:
    if number in list_1:
        print(number,"It's already in the 1st list.")
    else:
        print(number,"This number is not in 1st list.")
