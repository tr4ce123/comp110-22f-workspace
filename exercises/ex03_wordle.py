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
        elif contains_char(secret_word, player_guess[i]) == True:
                boxes = boxes + YELLOW_BOX
        else: 
            boxes = boxes + WHITE_BOX
        
        i += 1
    
    return boxes
    