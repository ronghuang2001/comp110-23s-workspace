"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730400592"
number_of_matching_characters: int = 0
word: str = input("Enter a 5-character word: ")
if (len(word) !=5):
    print ("Error: Word must contain 5 characters")
    exit()
else:
    single_character: str = input("Enter a single character: ")
    if (len(single_character)!=1):
        print("Error: Character must be a single character.")
        exit()
    else:
        print("Searching for " + single_character + " in " + word)
        if (single_character==word[0]):
            print(single_character + " found at index 0")
            number_of_matching_characters = number_of_matching_characters+1
            number_of_matching_characters
        if (single_character==word[1]):
            print(single_character + " found at index 1")
            number_of_matching_characters = number_of_matching_characters+1
            number_of_matching_characters
        if (single_character==word[2]):
            print(single_character + " found at index 2")
            number_of_matching_characters = number_of_matching_characters+1
            number_of_matching_characters
        if (single_character==word[3]):
            print(single_character + " found at index 3")
            number_of_matching_characters = number_of_matching_characters+1
            number_of_matching_characters
        if (single_character==word[4]):
            print(single_character + " found at index 4")
            number_of_matching_characters = number_of_matching_characters+1
            number_of_matching_characters
        if number_of_matching_characters ==0:
            print ("No instances of " + single_character + " found in " + word)
        if number_of_matching_characters ==1:
            print ("1 instance of " + single_character + " found in " + word)
        if number_of_matching_characters ==2:
            print ("2 instances of " + single_character + " found in " + word)
        if number_of_matching_characters ==3:
            print ("3 instances of " + single_character + " found in " + word)
        if number_of_matching_characters ==4:
            print ("4 instances of " + single_character + " found in " + word)
        if number_of_matching_characters ==5:
            print ("5 instances of " + single_character + " found in " + word)