"""EX06 - Creating your own text-driven adventure."""

__author__ = "730567386"

points: int = 0
player: str = ""

MELTING_FACE = "\U0001FAE0"
CELEBRATION_FACE = "\U0001F973"
SAD_FACE = "\U0001F97A"


def greet() -> None:
    """Asks the player to enter a name and greets them."""
    global player
    player = (input("Enter player name here: "))
    print("")
    print(f"Hello {player}, welcome to Coin Flip! Let's see how many times you can guess heads or tails correctly in a row.")


def game() -> None:
    """Starts the game loop if the player types '1'."""
    global points
    global final_score
    print("")
    print(f"Game started. Ready to play {player}?")
    from random import randint

    points = 0
    final_score = 0
    game_lost: bool = False

    while not game_lost:
        
        coin_flip: int = randint(1, 2)
        answer: str = ""

        if coin_flip == 1:
            answer = "Heads"
        else:
            answer = "Tails"

        player_response: str = (input("Heads or Tails? "))

        if player_response == answer:
            points += 1
            print(f"Great job! {CELEBRATION_FACE} Score = {points}")
        else: 
            print("")
            print(f"I'm sorry {player}, that's incorrect. Game over. {MELTING_FACE} {SAD_FACE}")
            print(f"{player}'s points earned: {points}")
            print(f"{player}'s EXP earned: {exp(points)}")
            print("")
            game_lost: bool = True
    
    if game_lost:
        chosen_path: str = (input("Type '1' to try again. Type '2' for help on how to play. Type '3' to quit. "))
        if chosen_path == "1":
            game()
        elif chosen_path == "2": 
            how_to_play()
        elif chosen_path == "4":
            end_game()
            

def how_to_play() -> None:
    """Gives a string that describes how the game works."""
    print("")
    print("Welcome to Coin Flip Frenzy!")
    print("In this game a coin will be flipped and you have to guess whether it is heads or tails.")
    print("If you guess correctly, you get a point. If you guess incorrectly, the game is over.")
    print("** Make sure to capitalize the first letter when typing 'Heads' or 'Tails' as your guess **")
    print("Let's see how many points you can get!")
    print("")
    chosen_path = (input("Type '1' to start the game. Type '2' to quit. "))
    if chosen_path == "1":
        game()
    elif chosen_path == "2":
        end_game()


def exp(points: int) -> int:
    """Gives the player experience points."""
    experience: int = points * 5
    return experience


def end_game() -> None:
    """Ends the game if the player types '3' and gives a goodbye message."""
    print(f"Thank you for playing {player}, have a great day!")


def main() -> None:
    """Entrypoint of the program."""
    global points
    global player

    greet()

    chosen_path: str = (input("Type '1' to start the game. Type '2' for help on how to play. Type '3' to quit game. "))
    if chosen_path == "1":
        game()
    elif chosen_path == "2": 
        how_to_play()
    elif chosen_path == "3":
        end_game()


if __name__ == "__main__":
    main()