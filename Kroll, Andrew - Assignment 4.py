# PROGRAM: Assignment 4: Rock, Paper, Scissors
# AUTHOR: Andrew Kroll
# DATE: 10/29/2019
# DESCRIPTION: “Rock, Paper, Scissors” is a zero-sum game where 2 players,
# a Human vs. the RPS program (which I’ll call Robbie), compete to see who
# can get the most points in a match, the most points in the overall
# tournament, and win the most matches in the tournament.
import test_mode
import in_out
import random


def main():
    in_out.make_test_file()
    mode = in_out.get_mode()
    match, game = 0, 0
    in_file = None
    out_file = None
    if mode == "game":
        match, game = in_out.get_match_game_count(mode, None)
        return
    elif mode == "test":
        in_file = open("RPSHumanMoves.txt", 'r')
        out_file = open("RPSLog.txt", 'w')
        match, game = in_out.get_match_game_count(mode, in_file)
    match = int(match)
    game = int(game)
    MOVES = ["Rock", "Paper", "Scissors"]
    random.seed(123)
    player_total = 0
    computer_total = 0
    turn_num = 0
    for match_num in range(match):
        player_score = 0
        computer_score = 0
        for game_num in range(game):
            player_move = in_out.get_move(mode, in_file, turn_num)
            turn_num += 1
            in_out.output_turn(mode, out_file, player_move)
            computer_move = MOVES[random.randint(0,2)]
            in_out.output_turn(mode, out_file, computer_move)
            if player_move == computer_move:
                in_out.output_result(mode, out_file, "Draw")
            elif player_move == "Rock" and computer_move == "Paper":
                computer_score += 1
                in_out.output_result(mode, out_file, "Computer Wins")
            elif player_move == "Rock" and computer_move == "Scissors":
                player_score += 1
                in_out.output_result(mode, out_file, "Player Wins")
            elif player_move == "Paper" and computer_move == "Rock":
                player_score += 1
                in_out.output_result(mode, out_file, "Player Wins")
            elif player_move == "Paper" and computer_move == "Scissors":
                computer_score += 1
                in_out.output_result(mode, out_file, "Computer Wins")
            elif player_move == "Scissors" and computer_move == "Paper":
                player_score += 1
                in_out.output_result(mode, out_file, "Player Wins")
            elif player_move == "Scissors" and computer_move == "Rock":
                computer_score += 1
                in_out.output_result(mode, out_file, "Computer Wins")
        if player_score > computer_score:
            player_total += 1
        elif player_score < computer_score:
            computer_score += 1
    print(player_total, computer_total)
    if mode == "test":
        in_file.close()
        out_file.close()


main()