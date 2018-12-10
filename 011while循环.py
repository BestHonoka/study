
places = []
while True:
   
   
    place = input("If you could visit one place in the world, where would you go? \n")
    if place == 'q':
        
        break
    else:
        places.append(place)
print("You want to go "+str(places)+'.')