import random
from string import whitespace

def rps_str(input : str) -> str:
    return "".join(filter(lambda x : x not in whitespace, input.lower()))

def get_move_p() -> str:
    move = ""
    while move not in ("rock", "paper", "scissors"):
        move = input("Rock, Paper, or Scissors?\n> ")
        move = rps_str(move)
    return move

def get_move_ai() -> str:
    return random.choice(["rock", "paper", "scissors"])

def get_winner(p_move : str, ai_move : str) -> bool:
    move_map = {"rock" : 0, "paper" : 1, "scissors" : 2}
    p_move_num = move_map[p_move]
    ai_move_num = move_map[ai_move]
    
    winner = (3 + p_move_num - ai_move_num) % 3
    
    if winner == 1:
        print("\033[32mYou win!\033[0m")
        return True
    elif winner == 2:
        print("\033[31mAI wins\033[0m")
        return True
    else:
        print("\033[33mIt is a tie\033[0m")
        print()
        return False

def get_play_again() -> bool:
    while True:
        response = rps_str(input("Play again? (yes/no)\n> "))
        if response == "yes":
            print()
            return True
        elif response == "no":
            return False
        else:
            print("\n\033[31mInvalid response\033[0m\n")

def game_loop():
    while True:
        p_move = get_move_p()
        print()
        ai_move = get_move_ai()
        print(f"AI chose {ai_move}")
        ended = get_winner(p_move, ai_move)
        
        if ended:
            break

if __name__ == "__main__":
    playing = True
    while playing:
        game_loop()
        print()
        playing = get_play_again()