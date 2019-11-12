# MODULE:  create_db.py                       used by PROJECT:  StateDB.py
# AUTHOR:                                           DESIGNER: Dr. Kaminski
# DESCRIPTION:  Creates DB (dictionary) using data from StateData.csv file.
#       (NOTE:  There are 2 header records to skip).  The DB contains:
#               KEY:  state name (convert to all caps)
#               VALUE:  tuple of (pop, code, el_votes, reps, senators)
#                       stored as int, str, int, int, int
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import re


def main():
    data = {}
    with open("StateData.csv", 'r') as file:
        for line in list(file):
            if re.match("[A-Za-z ]{1, },[0-9]{1, },[A-Za-z]{1, },[0-9]{1, },"
                        "[0-9]{1, },[0-9]{1, }", line):
                split = line.split(",")
                data[split[0].upper()] = int(split[1]), split[2],\
                    int(split[3]), int(split[4]), int(split[5])
    return data
