def draw_hor(x_count):
    for col in [0, 1]:
        for i in range(x_count):
            print("X", end='')
        print()


def draw_mix_hor(space_count, x_count):
    for col in [0, 1]:
        for i in range(space_count):
            print(" ", end='')
        for i in range(x_count):
            print("X", end='')
        print()


def draw_L_ver(rows):
    for i in range(rows):
        print("XX")


def draw_R_ver(width, rows):
    for row in range(rows):
        for space in range(width-2):
            print(" ", end='')
        print("XX")


def draw_LR_ver(width, rows):
    for row in range(rows):
        print("XX", end='')
        for space in range(width-4):
            print(" ", end='')
        print("XX")


def draw_M_ver(width, rows):
    for row in range(rows):
        for space in range((width-2)//2):
            print(" ", end='')
        print("XX")


def draw_space(height):
    for row in range(height):
        print()
