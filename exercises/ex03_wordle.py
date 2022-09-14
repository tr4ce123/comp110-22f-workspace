"""EX 03 - Structured Wordle - The final step."""

__author__ = "730567386"


def contains_char(word_being_searched: str, single_character: str) -> bool:
    """Shows whether the single character is present in the word being searched or not."""
    assert len(single_character) == 1

    i: int = 0 
    while i < len(word_being_searched):
        if word_being_searched[i] == single_character: 
            return True 
        else:
            i += 1
    
    return False 


def emojified(player_guess: str, secret_word: str) -> str:
    """Prints a color coded line of boxes to show the player if they have the correct letters and if they are at the correct index."""
    assert len(player_guess) == len(secret_word) 

    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    boxes: str = ""
    i: int = 0

    while i < len(player_guess):
        if player_guess[i] == secret_word[i]:
            boxes = boxes + GREEN_BOX
        elif contains_char(secret_word, player_guess[i]):
            boxes = boxes + YELLOW_BOX
        else: 
            boxes = boxes + WHITE_BOX
        
        i += 1
    
    return boxes


def input_guess(expected_length: int) -> str:
    """Repeats prompt until the length of the input matches the expected length of the secret word."""
    player_guess = input(f"Enter a {expected_length} character word: ")

    while expected_length != len(player_guess):
        player_guess = input(f"That wasn't {expected_length} chars! Try again: ")
    
    return player_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    turn_count: int = 1
    player_guess: str = ""

    while turn_count <= 6 and player_guess != secret_word:
        print(f"=== Turn {turn_count}/6 ===")
        player_guess = input_guess(len(secret_word))
        print(emojified(player_guess, secret_word))
    
        turn_count += 1

    if player_guess == secret_word:
        turn_count -= 1
        print(f"You won in {turn_count}/6 turns!")

    if turn_count > 6:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()