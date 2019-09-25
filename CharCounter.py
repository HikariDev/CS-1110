import re

count = [0, 0, 0, 0, 0, 0]
F_STR = """category count
a-z \t{0:>6n}
A-Z \t{1:>6n}
0-9 \t{2:>6n}
spaces  {3:>6n}
+ - * / {4:>6n}
other   {5:>6n}
\t\t  ----
TOTAL   {6:>6n}"""


def main():
    msg = str(input("Please enter a message! "))
    for c in msg:
        if re.match("[a-z]", c):
            count[0] += 1
        elif re.match("[A-Z]", c):
            count[1] += 1
        elif re.match("[0-9]", c):
            count[2] += 1
        elif re.match("[ ]", c):
            count[3] += 1
        elif re.match("[+\\-*/]", c):
            count[4] += 1
        else:
            count[5] += 1
    total = 0

    for i in count:
        total += i

    display(count, total)


def display(char_count, total):
    print(F_STR.format(char_count[0], char_count[1], char_count[2], char_count[3], char_count[4], char_count[5], total))


main()
