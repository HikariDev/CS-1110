# FLOH SIGN PROJECT
#
# Do a vertical sign for the FLOH company, "turning on appropriate LED
# lights" (in effect) by printing '*' for ON and '.' for OFF.
#
# F
#
# L
#
# O
#
# H
#
# (only each letter is the BIG version, like DoBigE.py program's output)
#
# NOTE:  Individual lights are NOT directly addressable to turn ON or OFF.
#     Instead, assume the LED sign board acts like IDLE's console where you
# 	have to print
# 	1) from top to bottom
# 	2) and, for a particular row, from left to right.
#
# All 4 letters are the same height & width - specified by the user.
# [No error-checking needed - you're the user, so just be accurate and
# 	provide reasonable sizes for your entries].
#
# Put 1 "blank line" after each big letter prints.
#
# The O is rectangular with squared corners, not rounded.
#
# F and L use variations on what I did for E, EXCEPT now you have to actually
# print '.' instead of just leaving right-ends of lines blank.
#
# H and O need a different kind of row (vs. what was shown for big E):
# goalposts (which you've seen a variation of in NestedForLoops example
# for a hollow rectangle).
#
# CAVEAT:  After we cover methods next week, you'll see a much better way
# to write this program.  For now, however, this will be a LONG linear
# program, drawing various line-segments for the F, then for the L, then for
# the O, then for the H.  There'll be a significant amount of "copy & paste"
# (Ctrl-C, Ctrl-V) since a full-horizontal line-segment (for example) is used
# in all 4 big letters.

# PROGRAM:  DoBigE.py
# AUTHOR:  Kaminski
# DESCRIPTION:  Uses for loops to draw a big letter E based on user-supplied
#       parameters for height, width, pen.
# RULES FOR E's
#      - top & bottom horizontals are both full width
#      - middle horizontal is 1/2 width
#      - top & bottom verticals are the same size when height is odd,
#          but for even heights, the bottom vertical is slightly taller
#
# REMINDER:  "draw" top to bottom, and within a row, left to right
# PLANNING:
#       - E made of 5 line-segments: top horizontal,  top leftside vertical,
#           middle horizontal,  bottom leftside vertical,  bottom horizontal.
#       - Draw each line-segment independently, allowing that a segment that's
#           already drawn may've already done part of the next line-segment.
#       - Loops here are based on COUNTS ("how many") not LABELS (row_num &
#           col_num), so I'll just use names row & col to mean "how many".
#
# CAUTION:  don't hardcoded values to control a loop (e.g., middle horiz.).
#       Instead, calculate such values as functions of width and/or height.
#
# DETERMINING SIZES OF 2 VERTICALS:
#       - part of E's total height taken up by the 3 horizontal line-segments
#       - remaining rows of the full letter's height are used by the
#           2 leftside verticals, each getting half of those remaining rows
#       - but if remaining rows is an odd number,
#           top vertical is smaller (truncate the float),
#           bottom vertical is bigger (remaining rows minus top vert. height)
#
# CAVEAT:  IDEALLY, should do checks for user-specified dimensions for
#       reasonableness (e.g., 2 x 2?) and relative sizes of height & width
#       (e.g., 5 x 100?).  That is NOT DONE IN THIS EXAMPLE.
# -----------------------------------------------------------------------------

CHAR_INFO = {"F":{"H":14,"W":15}, "L":{"H":14,"W":15}, "O":{"H":14,"W":15}, "H":{"H":14,"W":15}}

class Letter:
    HEIGHT = 5
    WIDTH = 8
    CHAR = ''

    def __init__(self, height, width):
        Letter.HEIGHT = height
        Letter.WIDTH = width

    @staticmethod
    def parse(message):
        for a in str(message):
            break

    @staticmethod
    def F():
        out = ""
        for a in range(Letter.HEIGHT):
            for b in range(Letter.WIDTH):
                out += "*" if a == 0 or (a == (Letter.HEIGHT-1)//2 and b < Letter.WIDTH//2) or b == 0 else "."
            out += '\n'
        return out

    @staticmethod
    def L():
        out = ""
        for a in range(Letter.HEIGHT):
            for b in range(Letter.WIDTH):
                out += "*" if a == Letter.HEIGHT-1 or b == 0 else "."
            out += '\n'
        return out

    @staticmethod
    def O():
        out = ""
        for a in range(Letter.HEIGHT):
            for b in range(Letter.WIDTH):
                out += "*" if a == 0 or a == Letter.HEIGHT-1 or b == 0 or b == Letter.WIDTH-1 else "."
            out += '\n'
        return out

    @staticmethod
    def H():
        out = ""
        for a in range(Letter.HEIGHT):
            for b in range(Letter.WIDTH):
                out += "*" if b == 0 or b == Letter.WIDTH-1 or a == (Letter.HEIGHT-1)//2 else "."
            out += '\n'
        return out


l = Letter(14,15)
print(l.F(), '\n', l.L(), '\n', l.O(), '\n', l.H(), sep='')