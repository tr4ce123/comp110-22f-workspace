"""EX 02 - One Shot Wordle - the next step in completing a wordle bot"""

__author__ = "730567386"

SECRET: str = "python"
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

player_guess: str = input("What is your 6-letter guess? ")
i: int = 0
boxes: str = ""
match_in_wrong_place: bool = False 
alternate_indices: int = 0

while len(player_guess) != len(SECRET):
    player_guess = input("That was not 6 letters! Try again: ")

while i < len(SECRET):
    if player_guess[i] == SECRET[i]:
        boxes = boxes + GREEN_BOX 
    else:
        match_in_wrong_place: bool = False
        alternate_indices: int = 0
        while match_in_wrong_place == False and alternate_indices < len(SECRET):
            if player_guess[i] == SECRET[alternate_indices]:
                match_in_wrong_place = True 
            else:
                alternate_indices += 1 
                
        
        if match_in_wrong_place == False: 
            boxes = boxes + WHITE_BOX
        else: 
            boxes = boxes + YELLOW_BOX
        
        match_in_wrong_place = False 
        
    i += 1



if player_guess != SECRET:
    print(boxes)
    exit(print("Not quite! Play again soon!"))
else:
    (print(boxes))
    exit(print("Woo! You got it!"))
    
