# PROGRAM: Exam1
# AUTHOR: Andrew Kroll
# DATE: 10/03/2019
# DESCRIPTION: This app gets a series of n pairs of numbers from the user
# and calculates various stats on those. It prints the output report to
# the console.

from Exam1 import in_out


def main():
    num_pairs = in_out.get_n()
    pairs = [[]*2]*num_pairs
    for i in range(num_pairs):
        pairs[i] = in_out.get_input_pair()
    all_total = 0
    all_minimum = -1
    all_maximum = -1
    larger_total = 0
    larger_minimum = -1
    larger_maximum = -1
    for i in range(num_pairs):
        for sub_i in range(2):
            all_total += pairs[i][sub_i]
            if pairs[i][sub_i] < all_minimum or all_minimum == -1:
                all_minimum = pairs[i][sub_i]
            if pairs[i][sub_i] > all_maximum or all_maximum == -1:
                all_maximum = pairs[i][sub_i]

            if sub_i == 0:
                larger_total += pairs[i][sub_i]
                if pairs[i][sub_i] < larger_minimum or larger_minimum == -1:
                    larger_minimum = pairs[i][sub_i]
                if pairs[i][sub_i] > larger_maximum or larger_maximum == -1:
                    larger_maximum = pairs[i][sub_i]
    all_average = all_total / (num_pairs * 2)
    larger_average = larger_total / num_pairs
    in_out.print_header(num_pairs)
    in_out.print_all_part(num_pairs, all_total, all_minimum, all_maximum,
                          all_average)
    in_out.print_larger_part(num_pairs, larger_total, larger_minimum,
                             larger_maximum, larger_average)
    magic = do_magic_op(num_pairs, pairs)
    in_out.print_magic_part(num_pairs, magic[0], magic[1], magic[2], magic[3])
    in_out.print_footer()


def do_magic_op(num_pairs, pairs):
    total = 0
    even = 0
    odd = 0
    mixed = 0
    for i in range(num_pairs):
        if pairs[i][0] % 2 == 0 and pairs[i][1] % 2 == 0:
            even += 1
            total += pairs[i][0] * pairs[i][1]
        elif pairs[i][0] % 2 != 0 and pairs[i][1] % 2 != 0:
            odd += 1
            total += pairs[i][0] + pairs[i][1]
        else:
            mixed += 1
            total += pairs[i][0] - pairs[i][1]
    return total, even, odd, mixed


main()
