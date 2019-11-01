import random
# ---- Input Section ----


def get_mode():
    mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    while not (mode == "game" or mode == "test"):
        print("Invalid mode!")
        mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    return mode


def get_match_game_count(mode, file):
    if mode == "game":
        games = int(input("How many games would you like to play (4+)?"))
        while games < 4:
            print("Invalid number of games!")
            games = int(input("How many games would you like to play (4+)?"))
        matches = int(input("How many matches would you like to play (2+)?"))
        while matches < 2:
            print("Invalid number of matches!")
            matches = int(input("How many matches would you \
            like to play (2+)?"))
        return games, matches
    else:
        return list(file)[0].replace('\n', '').split(',')


def get_move(mode, file, round):
    if mode == "game":
        move = input("(R)ock, (P)aper, or (S)cissors? ").lower()
        while not (move == "r" or move == "p" or move == "s"):
            print("Invalid move!")
            move = input("(R)ock, (P)aper, or (S)cissors? ")
        return move
    else:
        print(round)
        print(list(file))
        return list(file)[round].replace('\n', '')


# ---- Output Section ----


def make_test_file():
    with open("RPSHumanMoves.txt", 'w') as file:
        N_GAMES = 10
        N_MATCHES = 4
        MOVES = ["Rock", "Paper", "Scissors"]
        file.write(str(N_GAMES) + "," + str(N_MATCHES))
        random.seed(456)
        for i in range(N_GAMES*N_MATCHES):
            file.write("\n" + MOVES[random.randint(0, 2)])


def output_turn(mode, file, move):
    print(mode, move)