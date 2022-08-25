"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730567386"

five_character_word: str = input("Enter a 5-character word: ")

if len(five_character_word) != int(5):
    exit(print("Error: Word must contain 5 characters"))

single_character_input: str = input("Enter a single character: ")

if len(single_character_input) != int(1):
    exit(print("Error: Character must be a single character."))

print("Searching for " + single_character_input + " in " + five_character_word) 

word_index_0 = five_character_word[0]
word_index_1 = five_character_word[1]
word_index_2 = five_character_word[2]
word_index_3 = five_character_word[3]
word_index_4 = five_character_word[4]

number_of_matching_characters: int = 0

if single_character_input == word_index_0:
    print(single_character_input + " found at index 0")
    number_of_matching_characters += 1

if single_character_input == word_index_1:
    print(single_character_input + " found at index 1")
    number_of_matching_characters += 1

if single_character_input == word_index_2:
    print(single_character_input + " found at index 2")
    number_of_matching_characters += 1 

if single_character_input == word_index_3:
    print(single_character_input + " found at index 3")
    number_of_matching_characters += 1

if single_character_input == word_index_4:
    print(single_character_input + " found at index 4")
    number_of_matching_characters += 1

if number_of_matching_characters > 1:
    print(str(number_of_matching_characters) + " instances of " + single_character_input + " found in " + five_character_word)

if number_of_matching_characters == 1:
    print(str(number_of_matching_characters) + " instance of " + single_character_input + " found in " + five_character_word)

if number_of_matching_characters < 1:
    print("No instances of " + single_character_input + " found in " + five_character_word)
