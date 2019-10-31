# ---- Input Section ----


def get_mode():
    mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    while not (mode == "game" or mode == "test"):
        print("Invalid mode!")
        mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    return mode


def get_match_game_count(mode, infile):
    if mode == "game":
        games = int(input("How many games would you like to play (>=4)?"))
        while games < 4:
            print("Invalid number of games!")
            games = int(input("How many games would you like to play (>=4)?"))
        matches = int(input("How many matches would you like to play (>=2)?"))
        while matches < 2:
            print("Invalid number of matches!")
            matches = int(input("How many matches would you like to play (>=2)?"))
        return games, matches
    else:
        return


def get_move():
    return


def read_move():
    return

# ---- Output Section ----
