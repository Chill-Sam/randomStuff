from player_class import player
from save_class import saves

def main():
    # Give actual choice here
    new_game()
    # load_game()
    # exit()

def new_game():
    global p
    p = player(
        51, 1, 1, 1, 1, 1, 1,
        1, 3, "Choice1()")
    # Run game here    

    save()



if __name__ == "__main__":
    main()
