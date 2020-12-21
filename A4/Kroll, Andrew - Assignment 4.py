# PROGRAM: Assignment 4: Rock, Paper, Scissors
# AUTHOR: Andrew Kroll
# DATE: 10/29/2019
# DESCRIPTION: “Rock, Paper, Scissors” is a zero-sum game where 2 players,
# a Human vs. the RPS program (which I’ll call Robbie), compete to see who
# can get the most points in a match, the most points in the overall
# tournament, and win the most matches in the tournament.
from A4 import in_out as io
import random


def main():
    io.make_test_file()
    mode = io.get_mode()
    in_file = open("RPSHumanMoves.txt", 'r')
    out_file = open("RPSLog.txt", 'w')
    game_count, match_count = io.get_game_match_count(mode, in_file)
    human_moves = None
    if mode == "game":
        in_file.close()
        out_file.close()
        random.seed()
    else:
        in_file = open("RPSHumanMoves.txt", 'r')
        human_moves = io.get_human_moves(in_file)
        random.seed(123)
    run_tournament(out_file, mode, match_count, game_count, human_moves)


def run_game(mode, game_num, human_moves):
    human_move = io.get_human_move(mode, game_num, human_moves)
    computer_move = get_computer_move()
    if human_move == computer_move:
        return human_move, computer_move, 0
    elif human_move == "Rock" and computer_move == "Paper":
        return human_move, computer_move, 2
    elif human_move == "Rock" and computer_move == "Scissors":
        return human_move, computer_move, 1
    elif human_move == "Paper" and computer_move == "Rock":
        return human_move, computer_move, 1
    elif human_move == "Paper" and computer_move == "Scissors":
        return human_move, computer_move, 2
    elif human_move == "Scissors" and computer_move == "Rock":
        return human_move, computer_move, 2
    elif human_move == "Scissors" and computer_move == "Paper":
        return human_move, computer_move, 1
    else:
        return human_move, computer_move, 0


def run_match(out_file, mode, game_count, match_num, human_moves):
    format_str = "{0}) Human: {1},  Robbie: {2} >>> {3}"
    score = [0, 0, 0]
    io.output_line(out_file, mode, "MATCH #" + str(match_num + 1))
    for game in range(game_count):
        result = run_game(mode, game * (match_num + 1), human_moves)
        if result[2] == 0:
            io.output_line(out_file, mode,
                           format_str.format(game + 1, result[0].upper(),
                                             result[1].upper(), "Draw"))
            score[2] += 1
        elif result[2] == 1:
            io.output_line(out_file, mode,
                           format_str.format(game + 1, result[0].upper(),
                                             result[1].upper(), "Human wins"))
            score[0] += 1
        elif result[2] == 2:
            io.output_line(out_file, mode,
                           format_str.format(game + 1, result[0].upper(),
                                             result[1].upper(), "Robbie wins"))
            score[1] += 1
    return score


def run_tournament(out_file, mode, match_count, game_count, human_moves):
    format_str = "Human: {0},  Robbie: {1},  Draw: {2} >>> {3}\n"
    final_scores = [0, 0, 0]
    match_scores = [[0, 0, 0]] * match_count
    for match in range(match_count):
        match_scores[match] = run_match(out_file, mode, game_count, match,
                                        human_moves)
        if match_scores[match][0] > match_scores[match][1]:
            io.output_line(out_file, mode,
                           format_str.format(match_scores[match][0],
                                             match_scores[match][1],
                                             match_scores[match][2],
                                             "Human wins"))
            final_scores[0] += 1
        elif match_scores[match][0] < match_scores[match][1]:
            io.output_line(out_file, mode,
                           format_str.format(match_scores[match][0],
                                             match_scores[match][1],
                                             match_scores[match][2],
                                             "Robbie wins"))
            final_scores[1] += 1
        else:
            io.output_line(out_file, mode,
                           format_str.format(match_scores[match][0],
                                             match_scores[match][1],
                                             match_scores[match][2],
                                             "Draw"))
            final_scores[2] += 1
    winner = "Human wins" if final_scores[0] > final_scores[1] else \
        "Robbie wins" if final_scores[0] < final_scores[1] else "Draw"
    io.output_line(out_file, mode, "FINAL SCORE\n" + format_str.format(
        final_scores[0], final_scores[1], final_scores[2], winner))


def total_scores(match_scores):
    totals = [0, 0, 0]
    for match in range(len(match_scores)):
        for i in range(2):
            totals[i] += match_scores[i]
    return totals


def get_computer_move():
    rand = random.randint(0, 2)
    return "Rock" if rand == 0 else "Paper" if rand == 1 else "Scissors"


main()
