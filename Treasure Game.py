print("Welcome to Treasure Island!!\nYour mission is to find the Treasure")
way = input("In which way do you want to go?? Left or Right\n")
if way == "Right":
    print("Fell into hole, Sorry the game is Over")
else:
    do = input("How do you want to do?? Swim or Wait\n")
    if do == "Wait":
        print("Attacked by Trout, Sorry the Game is Over")
    else:
        door = input("Which door you want to Open?? Blue or Red or Yellow\n")
        if door == "Red":
            print("Burned by Fire, sorry the Game is Over")
        elif door == "Blue":
            print("Eaten by Animals, Sorry the Game is Over")
        elif door == "Yellow":
            print("Hurray, You Found the Treasure!!!, Congrats You won the game")
        else:
            print("Dumb or What!!! I asked you Choose between 3 Colors, Stupid")