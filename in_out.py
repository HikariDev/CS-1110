import random
# ---- Input Section ----


def get_mode():
    mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    while not (mode == "game" or mode == "test"):
        print("Invalid mode!")
        mode = input("Would you like to run TEST mode or GAME mode? ").lower()
    return mode


def get_game_match_count(mode, file):
    if mode == "game":
        games = int(input("How many games would you like to play (4+)? "))
        while games < 4:
            print("Invalid number of games!")
            games = int(input("How many games would you like to play (4+)? "))
        matches = int(input("How many matches would you like to play (2+)? "))
        while matches < 2:
            print("Invalid number of matches!")
            matches = int(input("How many matches would you \
            like to play (2+)? "))
        return games, matches
    else:
        games, matches = list(file)[0].replace('\n', '').split(',')
        return int(games), int(matches)


def get_human_move(mode, game_num, human_moves):
    if mode == "game":
        move = input("(R)ock, (P)aper, or (S)cissors? ").lower()
        while not (move == "r" or move == "p" or move == "s"):
            print("Invalid move! Please only enter one letter")
            move = input("(R)ock, (P)aper, or (S)cissors? ")
        if move == "r":
            return "Rock"
        elif move == "p":
            return "Paper"
        else:
            return "Scissors"
    else:
        return human_moves[game_num]


def get_human_moves(file):
    moves = list(file)
    moves.remove(moves[0])
    for i in range(len(moves)):
        moves[i] = moves[i].replace("\n", "")
    return moves


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
    return


def output_line(file, mode, line):
    if mode == "test":
        file.write(line + "\n")
    else:
        print(line)
