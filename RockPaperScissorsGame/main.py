import random

options = {1: "rock", 2: "paper", 3: "scissors"}
player_score = 0
computer_score = 0
counter=0
def result(user_choice, computer_choice):
    global player_score, computer_score, counter
    if user_choice == computer_choice:
        player_score+=1
        computer_score+=1
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        player_score+=1
    else:
        computer_score+=1
    counter+=1
    return player_score, computer_score

while True:
    print("Welcome to Rock Paper Scissors Game")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    try:
        while True:
            choice = str(input("Want to play(yes/no): "))
            if choice.lower() == "no":
                exit()
            elif choice.lower() == "yes":
                player_score = computer_score = counter = 0

                rounds = int(input("How many rounds you want to play: "))
                for i in range(rounds):
                    player_choice = int(input("Enter your choice(1/2/3): "))
                    bot_guessed = random.randint(1,3)
                    bot_choice = options[bot_guessed]

                    if player_choice in [1, 2, 3]:
                        player_choice = options[player_choice]
                        p_score, bot_score = result(player_choice, bot_choice)
                        if rounds == counter:
                            print("--------------- RESULT ---------------\n")
                            print("Your score is:", p_score)
                            print("Computer score is:", bot_score)
                            print(f"You won! by {p_score-bot_score}") if (p_score>bot_score) else print(f"Computer won! by {bot_score-p_score}")
                            print("\n--------------------------------------")


                    else:
                        print("Invalid Choice ")
                        continue
            else:
                print("Invalid Wish. ")

    except ValueError:
        print("Invalid input type.\nEnter choice number from 1 to 3. ")
