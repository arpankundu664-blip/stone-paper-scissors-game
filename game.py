import random
points_of_user=0
points_of_comp=0
while True:
    print(f"current score of you: {points_of_user}\n current score of comp {points_of_comp}\n")
    comp=random.randint(1,3)
    user=int(input("1 for stone, 2 for paper, 3 for scissors\n now choose: "))

    if user==1 and comp==3:
        points_of_user+=5
        print("you won the round\n")
    elif user==2 and comp==1:
        points_of_user+=5
        print("you won the round\n") 
    elif user==3 and comp==2:
        points_of_user+=5
        print("you won the round\n") 
    elif user==comp:
        print("Draw Try Again\n")
    else:
        points_of_comp+=5
        print("copm won the round\n")   

    if points_of_comp == 30:
        print("comp won this game 🤣")
    elif points_of_user == 30:
        print("congratulations you won the game 🥳") 
        break                  