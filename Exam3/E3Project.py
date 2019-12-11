# PROJECT:  E3Project.py                   uses MODULES:  create.py & query.py
# AUTHOR:  Andrew Kroll
# DESIGNER:  Dr. Kaminski
# PROJECT OVERVIEW:  Creates 2 dictionaries to store income and location data
#       for countries of the world.  Then processes transactions (from a
#       transaction file) using the dictionaries to answer to queries.
# ----------------------------------------------------------------------------

from Exam3 import create, query


def main():
    loc_dict = create.make_loc_dict()
    inc_dict = create.make_inc_dict()

    query.do_trans(loc_dict, inc_dict)

    print('\nTHE END')


main()
