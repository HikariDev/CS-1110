import char_des
import line_drawer


def main():
    message = get_message()
    dimensions = get_char_dimen()


def get_message():
    return str(input("Sign Text: "))


def get_char_dimen():
    return int(input("Character Width: ")), int(input("Character Height: "))


def decide_which_char():
    return

