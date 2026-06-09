import random

options = {1: "rock", 2: "paper", 3: "scissors"}

# Update scores based on choices and return round winner.
def result(user_choice, computer_choice, scores):
    player_score, computer_score = scores
    if user_choice == computer_choice:
        player_score += 1
        computer_score += 1
        winner = "Tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        player_score += 1
        winner = "Player"
    else:
        computer_score += 1
        winner = "Computer"
    return player_score, computer_score, winner

# Play the given number of rounds with detailed output.
def play_round(rounds):
    player_score, computer_score = 0, 0
    counter = 0

    while counter < rounds:
        try:
            player_choice = int(input("Enter your choice (1/2/3): "))
            if player_choice not in options:
                print("Invalid Choice. Try again.")
                continue
            bot_choice = options[random.randint(1, 3)]
            player_choice = options[player_choice]

            player_score, computer_score, winner = result(player_choice, bot_choice, (player_score, computer_score))
            counter += 1

            print(f"Round {counter}: You chose {player_choice}, Computer chose {bot_choice}.")
            print(f"Winner: {winner}")
            print(f"Scores → You: {player_score}, Computer: {computer_score}\n")

        except ValueError:
            print("Invalid input type. Enter a number from 1 to 3.")

    show_result(player_score, computer_score)

# Display the final result.
def show_result(player_score, computer_score):
    print("--------------- FINAL RESULT ---------------\n")
    print("Your score is:", player_score)
    print("Computer score is:", computer_score)
    if player_score > computer_score:
        print(f"You won the game by {player_score - computer_score} points!")
    elif computer_score > player_score:
        print(f"Computer won the game by {computer_score - player_score} points!")
    else:
        print("The game is a tie!")
    print("\n-------------------------------------------")

# Main game loop.
def main():
    while True:
        print("Welcome to Rock Paper Scissors Game")
        print("1. Rock\n2. Paper\n3. Scissors")

        choice = input("Want to play (yes/no): ").strip().lower()
        if choice == "no":
            print("Goodbye!")
            break
        elif choice == "yes":
            try:
                rounds = int(input("How many rounds you want to play: "))
                play_round(rounds)
            except ValueError:
                print("Invalid input. Enter a valid number of rounds.")
        else:
            print("Invalid Wish. Please type yes or no.")

if __name__ == "__main__":
    main()
