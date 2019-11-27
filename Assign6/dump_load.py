# MODULE:  dump_load.py                    used by PROJECT: A6WorldDataQueries
# AUTHOR: Andrew Kroll                     DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Contains 2 "mini-main's" - one to DUMP the 4 dictionaries to
#       the 4 backup files, and one to LOAD the 4 dictionaries from the 4
#       backup files.
# ----------------------------------------------------------------------------
import pickle

def dump_4_dictionaries(db, id_index, code_index, cont_index):
    dump_db(db)
    dump_id_index(id_index)
    dump_code_index(code_index)
    dump_cont_index(cont_index)


def dump_db(db):
    file_name = 'WorldDB.bin'
    with open(file_name, 'w') as file:
        pickle.dump(db, file)


def dump_id_index(id_index):
    file_name = 'IdIndex.bin'
    with open(file_name, 'w') as file:
        pickle.dump(id_index, file)


def dump_code_index(code_index):
    file_name = 'CodeIndex.bin'
    with open(file_name, 'w') as file:
        pickle.dump(code_index, file)


def dump_cont_index(cont_index):
    file_name = 'ContIndex.bin'
    with open(file_name, 'w') as file:
        pickle.dump(cont_index, file)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def load_4_dictionaries():
    db = load_db()
    id_index = load_id_index()
    code_index = load_code_index()
    cont_index = load_cont_index()
    return db, id_index, code_index, cont_index


def load_db():
    file_name = 'WorldDB.bin'
    with open(file_name, 'r') as file:
        return pickle.load(file)


def load_id_index():
    file_name = 'IdIndex.bin'
    with open(file_name, 'r') as file:
        return pickle.load(file)


def load_code_index():
    file_name = 'CodeIndex.bin'
    with open(file_name, 'r') as file:
        return pickle.load(file)


def load_cont_index():
    file_name = 'ContIndex.bin'
    with open(file_name, 'r') as file:
        return pickle.load(file)
