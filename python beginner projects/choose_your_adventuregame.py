name = input("Type Your Name: ")
print("Welcome", name, "to this adventure! ")

answer = input(
    "You are on a dirt road, it has come to an end and you can go to left or right.  Which way you would like to go ?").lower()

if answer == "left":
    answer= input("You come to river, you can walk around it or swim accross? Type walk to walk around and swim to swim accros: ")
    if answer == "swim":
        print("You Swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("you walk many miles, ran out of water and you lose the game")
    else: 
        print('Not a valid option. you lose')
elif answer == "right":
    answer = input("you come to bridge , it looks wobbly , do you want to cross it or head back (cross/back)?  ")
    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input("You cross the bridge and meet a stranger. Do you talk to them (Yes/ No) ? ")
        
        if answer == "yes":
            print("you talk to the stranger they give you gold. You WON!")
        elif answer == "no":
            print("Yuo ignore the strager and they are offended and You Lose!")
        else:
            print("not a valid option you lose")
    else: 
        print('Not a valid option. you lose')

else:
    print("Nota  valid option.")


print("Thank you for playing", name)