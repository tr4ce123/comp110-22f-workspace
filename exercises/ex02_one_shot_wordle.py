"""EX 02 - One Shot Wordle - the next step in completing a wordle bot."""

__author__ = "730567386"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

player_guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
i: int = 0
boxes: str = ""

while len(player_guess) != len(SECRET):
    player_guess = input("That was not 6 letters! Try again: ")

while i < len(SECRET):
    if player_guess[i] == SECRET[i]:
        boxes = boxes + GREEN_BOX 
    else:
        match_in_wrong_place: bool = False
        alternate_indices: int = 0

        while not match_in_wrong_place and alternate_indices < len(SECRET):
            if player_guess[i] == SECRET[alternate_indices]:
                match_in_wrong_place = True 
            else:
                alternate_indices += 1 
                
        if not match_in_wrong_place: 
            boxes = boxes + WHITE_BOX
        else: 
            boxes = boxes + YELLOW_BOX
        
        match_in_wrong_place = False 
        
    i += 1

if player_guess != SECRET:
    print(boxes)
    print("Not quite! Play again soon!")
else:
    (print(boxes))
    print("Woo! You got it!")

