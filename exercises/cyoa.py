"""Choose Your Own Adventure Experience."""
__author__ = "730400592"
SMILE: str = "\U0001F600"
CELEBRATE: str = "\U0001F973"
points: int = None
player: str = ""


def main() -> None:
    """Main code of program."""
    global points
    points = 0
    greet()
    option: str = input("\nYou have three options.\nOption1: Guess an integer between 1 and 15.\nOption2: Guess an integer between 16 and 30.\nOption3: Stop the game and exit.\nAdventure points are set to 0 initially. If your guess mataches the secret number, you will get 20 adventure points.\nIf the (absolute) difference between your guess and secret number is 1, you will get 10 adventure points.\nIf the (absolute) difference between your guess and secret number is 2, you will get 8 adventure points.\nIf the (absolute) difference between your guess and secret number is 3, you will get 5 adventure points.\nIf the (absolute) difference between your guess and secret number is 4, you will get 3 adventure points.\nIf the (absolute) difference between your guess and secret number is greater than 4, you will get 2 adventure points.\nWhich option do you like to choose?\nType 1 if you choose Option1. Type 2 if you choose Option2. Type 3 if you choose Option3.\n")
    play: bool = True
    while play:
        if option == "3":
            print(f" The end of the game. Your total advanture points are {points}. Thank you for your participation. Goodbye!")
            play = False
        else:
            if option == "1":
                print("The secret number is an integer between 1 and 15.")
                points_calculation()
                print(f"Your total adventure points are currently {points}.")
            if option == "2":
                print("The secret number is an integer between 16 and 30.")
                points = points_cal(points)
                print(f"Your total adventure points are currently {points}.")
            option = input(f"Play again? Which option do you like to choose, {player}?\nOption1: Guess an integer between 1 and 15.\nOption2: Guess an integer between 16 and 30.\nOption3: Stop the game and exit.\nType 1 if you choose Option1. Type 2 if you choose Option2. Type 3 if you choose Option3.\n")


def greet() -> None:
    """Greet. Welcome."""
    global player
    player = input("What is your name? ")
    print(f"Hi{SMILE}, {player}! Welcome to the number guessing game. In this game, you will guess an integer within a specific range. You can keep playing the game if you want.")


def points_calculation() -> None:
    """Advanture points calculation."""
    guess: str = input(f"{player}, What is your guess? ")
    from random import randint
    secret = randint(1, 15)
    playing: bool = True
    global points
    while playing:
        if int(guess) != secret:
            if abs(int(guess) - secret) == 1:
                points += 10
                print("Your guess is 1 different from the secret number!")
            if abs(int(guess) - secret) == 2:
                points += 8
                print("Your guess is 2 different from the secret number!")
            if abs(int(guess) - secret) == 3:
                points += 5
                print("Your guess is 3 different from the secret number!")
            if abs(int(guess) - secret) == 4:
                points += 3
                print("Your guess is 4 different from the secret number!")
            if abs(int(guess) - secret) > 4:
                points += 2
                print("Your guess is at least 5 different from the secret number!")
            guess = input("Try again: ")
        else:
            points += 20
            print(f"You get it{CELEBRATE}!")
            playing = False   


def points_cal(total_points: int) -> int:
    "Advanture points calculation."
    guess: str = input(f"{player}, What is your guess? ")
    from random import randint
    secret2 = randint(16, 30)
    playing: bool = True
    while playing:
        if int(guess) != secret2:
            if abs(int(guess) - secret2) == 1:
                total_points += 10
                print("Your guess is 1 different from the secret number!")
            if abs(int(guess) - secret2) == 2:
                total_points += 8
                print("Your guess is 2 different from the secret number!")
            if abs(int(guess) - secret2) == 3:
                total_points += 5
                print("Your guess is 3 different from the secret number!")
            if abs(int(guess) - secret2) == 4:
                global points
                total_points += 3
                print("Your guess is 4 different from the secret number!")
            if abs(int(guess) - secret2) > 4:
                total_points += 2
                print("Your guess is at least 5 different from the secret number!")
            guess = input("Try again: ")
        else:
            total_points += 20
            print(f"You get it{CELEBRATE}!")
            playing = False
    return total_points


if __name__ == "__main__":
    main()