"""EX02_one_shot_wordle"""
__author__ = "730400592"
#set up variables needed for the exercise
SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
index: int = 0
correctness: int = 0
box: str = ""
#guess input
guess: str = input("What is your " + str(len(SECRET)) + "-letter guess? ")
#set up while loop for playing the game
playing: bool = True
while playing:
    #if incorrect number of letters is given, player will be prompted to give a guess of correct length
    if len(guess) != len(SECRET):
        guess = input("That was not " + str(len(SECRET)) + " letters! Try again: ")
    #if correct number of letters is given, player will be prompted to continue to play
    else:
    #set up while loop to check each index for correct match
        while index < len(SECRET):
            #if the the index of the input word matches the same index of the secret word, a green box will be attached
            if guess[index] == SECRET[index]:
                correctness = correctness + 1
                box = f"{box}{GREEN_BOX}"
            else: 
                index_check: int = 0
                other_location : bool = False
                #set up while loop to check whether the current index matches other indices of the secret word
                while index_check < len(SECRET) and other_location is False:    
                    if  guess[index] == SECRET[index_check]:
                        other_location = True
                    else:
                        index_check = index_check + 1
                #if the letter can be found somehwere else in the secret word, yellow box will be attached
                if other_location is True:
                    box = f"{box}{YELLOW_BOX}"
                #if the letter can't be found anywhere in the secret word, white box will be attached
                else:
                    box = f"{box}{WHITE_BOX}"
            index = index + 1
        print(box)
        #if guessed word matches secret word, print "Woo! You got it!"
        if correctness == len(SECRET):
            print("Woo! You got it!")
            playing = False
        #if guessed word doesn't match secret word, print "Not quite. Play again soon!"
        else:
            print("Not quite. Play again soon!")
            playing = False