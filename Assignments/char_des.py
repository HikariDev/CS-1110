from Assignments import line_drawer


def des0(width, height):
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_LR_ver(width, height - 4)
    line_drawer.draw_mix_hor(2, width - 4)


def des1(width, height):
    line_drawer.draw_M_ver(width, height)


def des2(width, height):
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_R_ver(width, (height - 6) // 2)
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_L_ver((height - 6) // 2)
    line_drawer.draw_hor(width)


def des3(width, height):
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_R_ver(width, (height - 6) // 2)
    line_drawer.draw_mix_hor((width - 2) // 2, (width - 2) // 2)
    line_drawer.draw_R_ver(width, (height - 6) // 2)
    line_drawer.draw_hor(width - 2)


def des4(width, height):
    line_drawer.draw_LR_ver(width, (height - 2) // 2)
    line_drawer.draw_hor(width)
    line_drawer.draw_R_ver(width, (height - 2) // 2)


def des5(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_L_ver((height - 6) // 2)
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_R_ver(width, (height - 6) // 2)
    line_drawer.draw_hor(width - 2)


def des6(width, height):
    line_drawer.draw_L_ver((height - 4) // 2)
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_LR_ver(width, (height - 4) // 2)
    line_drawer.draw_mix_hor(2, width - 4)


def des7(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_R_ver(width, height - 2)


def des8(width, height):
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_LR_ver(width, (height - 6) // 2)
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_LR_ver(width, (height - 6) // 2)
    line_drawer.draw_mix_hor(2, width - 4)


def des9(width, height):
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_LR_ver(width, (height - 4) // 2)
    line_drawer.draw_mix_hor(2, width - 2)
    line_drawer.draw_R_ver(width, (height - 4) // 2)


def desC(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_L_ver(height - 4)
    line_drawer.draw_hor(width)


def desE(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_L_ver((height - 6) // 2)
    line_drawer.draw_hor(width // 2)
    line_drawer.draw_L_ver((height - 6) // 2)
    line_drawer.draw_hor(width)


def desF(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_L_ver((height - 4) // 2)
    line_drawer.draw_hor(width // 2)
    line_drawer.draw_L_ver((height - 4) // 2)


def desH(width, height):
    line_drawer.draw_LR_ver(width, (height - 2) // 2)
    line_drawer.draw_hor(width)
    line_drawer.draw_LR_ver(width, (height - 2) // 2)


def desI(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_M_ver(width, height - 4)
    line_drawer.draw_hor(width)


def desL(width, height):
    line_drawer.draw_L_ver(height - 2)
    line_drawer.draw_hor(width)


def desO(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_LR_ver(width, height - 4)
    line_drawer.draw_hor(width)


def desP(width, height):
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_LR_ver(width, (height - 4) // 2)
    line_drawer.draw_hor(width - 2)
    line_drawer.draw_L_ver((height - 4) // 2)


def desS(width, height):
    line_drawer.draw_mix_hor(2, width - 2)
    line_drawer.draw_L_ver((height - 6) // 2)
    line_drawer.draw_mix_hor(2, width - 4)
    line_drawer.draw_R_ver(width, (height - 6) // 2)
    line_drawer.draw_hor(width - 2)


def desT(width, height):
    line_drawer.draw_hor(width)
    line_drawer.draw_M_ver(width, height - 2)


def desU(width, height):
    line_drawer.draw_LR_ver(width, height - 2)
    line_drawer.draw_mix_hor(2, width - 4)


def desSPACE(height):
    line_drawer.draw_space(height)


def desODD(width, height):
    for row in range(height//2):
        line_drawer.draw_hor(width)
