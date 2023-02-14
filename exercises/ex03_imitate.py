"""EX03__Structured_Wordle."""
__author__ = "730400592"


def contains_char(string: str, single_character: str) -> bool:
    # Define a function to check whether a string contains the single character
    # Return True if the string contains the single character and return Flase if a string doesn't contain it
    """Check whether the string contains the single character."""
    assert len(single_character) == 1
    index: int = 0
    have_character: bool = False
    while index < len(string) and have_character is False:
        if string[index] != single_character:
            index = index + 1
        else: 
            have_character = True
    if have_character is True:
        return True
    else: 
        return False


def emojified(guess: str, secret: str) -> str:
    # Define a function that gives colored emoji box to give users hints
    """Returns emoji to give hint of guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    index_check: int = 0
    box: str = ""
    while index_check < len(secret):
        if guess[index_check] == secret[index_check]:
            box = f"{box}{GREEN_BOX}"
            # if the the index of the input word matches the same index of the secret word, a green box will be attached
        else:
            if contains_char(secret, guess[index_check]) is False:
                box = f"{box}{WHITE_BOX}"
            # if the character can't be found anywhere in the secret word, a white box will be attached
            else:
                box = f"{box}{YELLOW_BOX}"
                # if the character can be found somewhere else in the secret word, a yellow box will be attached
        index_check = index_check + 1
    return box


def input_guess(length: int) -> str:
    # Define a function that prompts the user to give a guess of the expected length
    """Prompt the user to provide a guess of the expected length."""
    word_enter: str = input(f"Enter a {length} character word: ")
    playing: bool = True
    while playing is True:
        if len(word_enter) != length:
            word_enter = input(f"That wasn't {length} chars! Try again: ")
        else: 
            playing = False
    return word_enter
