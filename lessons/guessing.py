"""Ask user for number, give hints about number if wrong"""
SECRET: int = 10
guess: int = int(input("Guess a number!"))
playing: bool = True
while playing is True:
    if guess== SECRET:
        print("good")
        playing = False
    else:
        if guess%2!=0:
            print("wrong, it is not odd")
        if guess < SECRET:
            print("it is too low")
        else:
            print("it is too high")
        guess = int(input("try again"))