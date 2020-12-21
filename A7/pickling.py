# MODULE:  pickling                             used by PROJECT:  PureMichigan
# AUTHOR: Andrew Kroll                          DESIGNER:  Dr. Kaminski
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

import pickle
from A7 import Destination

FILE_NAME = 'Destinations.bin'


def save_list_of_obj(data):
    with open(FILE_NAME, 'wb') as file:
        pickle.dump(data, file)


def load_list_of_obj() -> [Destination]:
    with open(FILE_NAME, 'rb') as file:
        return pickle.load(file)
