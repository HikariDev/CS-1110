# Input
def get_n():
    i = int(input("Enter a positive integer: "))
    while i < 0:
        i = int(input("Enter a positive integer: "))
    return i


def get_input_pair():
    pair = [-1, -1]
    for i in range(2):
        pair[i] = get_n()
    if pair[0] < pair[1]:
        pair[0], pair[1] = pair[1], pair[0]
    return pair

# Output


def print_header(pair_count):
    print("Exam1 STATS REPORT for", pair_count, "number pairs")
    print("--------------------------------------")


def print_all_part(pair_count, total, minimum, maximum, average):
    print("FOR ALL NUMBERS - N: ", pair_count * 2)
    print("\t  TOTAL: ", total)
    print("\t  MINIMUM: ", minimum)
    print("\t  MAXIMUM: ", maximum)
    print("\t  AVERAGE: ", average)


def print_larger_part(pair_count, total, minimum, maximum, average):
    print("FOR JUST THE LARGER NUMBERS - N: ", pair_count)
    print("\t  TOTAL: ", total)
    print("\t  MINIMUM: ", minimum)
    print("\t  MAXIMUM: ", maximum)
    print("\t  AVERAGE: ", average)


def print_magic_part(pair_count, total, even, odd, mixed):
    print("FOR MAGIC OPERATIONS RESULTS - N: ", pair_count)
    print("\t  TOTAL: ", total)
    print("\t  Num EVEN/EVEN pairs: ", even)
    print("\t  Num ODD/ODD pairs: ", odd)
    print("\t  Num MIXED pairs: ", mixed)


def print_footer():
    print("\nEND OF REPORT")
