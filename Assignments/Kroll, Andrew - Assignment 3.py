# PROGRAM: Assignment 3: Chunky Sign
# AUTHOR: Andrew Kroll
# DATE: 10/22/2019
# DESCRIPTION: This app produces a vertical sign of chunky characters (using
# EXACT font shown below) based on a message supplied by the user.  The sign
# is printed to IDE’s console.  The user specifies height and width for the
# characters (all are the same size).


from Assignments import char_des


def main():
    message = get_message()
    dimensions = get_char_dimen()
    for char in message:
        decide_which_char(char, dimensions[0], dimensions[1])
        print()


def get_message():
    return str(input("Sign Text: ")).upper()


def get_char_dimen():
    width, height = int(input("Character Width (8-18, EVEN): ")), \
                    int(input("Character Height (10-20, EVEN): "))
    if width % 2 == 1:
        width += 1
    if height % 2 == 1:
        height += 1
    if width < 8:
        width = 8
    elif width > 18:
        width = 18
    if height < 10:
        height = 10
    elif height > 20:
        height = 20
    return width, height


def decide_which_char(char, width, height):
    if char == "0":
        char_des.des0(width, height)
    elif char == "1":
        char_des.des1(width, height)
    elif char == "2":
        char_des.des2(width, height)
    elif char == "3":
        char_des.des3(width, height)
    elif char == "4":
        char_des.des4(width, height)
    elif char == "5":
        char_des.des5(width, height)
    elif char == "6":
        char_des.des6(width, height)
    elif char == "7":
        char_des.des7(width, height)
    elif char == "8":
        char_des.des8(width, height)
    elif char == "9":
        char_des.des9(width, height)
    elif char == " ":
        char_des.desSPACE(height)
    elif char == "C":
        char_des.desC(width, height)
    elif char == "E":
        char_des.desE(width, height)
    elif char == "F":
        char_des.desF(width, height)
    elif char == "H":
        char_des.desH(width, height)
    elif char == "I":
        char_des.desI(width, height)
    elif char == "L":
        char_des.desL(width, height)
    elif char == "O":
        char_des.desO(width, height)
    elif char == "P":
        char_des.desP(width, height)
    elif char == "S":
        char_des.desS(width, height)
    elif char == "T":
        char_des.desT(width, height)
    elif char == "U":
        char_des.desU(width, height)
    else:
        char_des.desODD(width, height)

main()
