# MODULE:  dump_load_db.py                  used by PROJECT:  StateDB.py
# AUTHOR:                                           DESIGNER: Dr. Kaminski
# DESCRIPTION:  Does pickling/unpickling of DB (dictionary) to/from
#       StateDB.bin.  Needs load and dump functions.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
import pickle


def load():
    inf = open("StateData.bin", 'rb')
    dictionary = pickle.load(inf)
    inf.close()
    return dictionary


def dump(dictionary):
    outf = open("StateData.bin", 'wb')
    pickle.dump(dictionary, outf)
    outf.close()