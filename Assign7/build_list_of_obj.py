# MODULE:  build_list                           used by PROJECT:  PureMichigan
# AUTHOR:                                       DESIGNER:  Dr. Kaminski
# NOTE:  Data lines have a ',' at the end besides the '\n' which both need
#       removing before splitting the line into fields.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Assign7 import Destination             # MODULE which contains Destination CLASS

def load_file_data():
    infile = open('PureMichiganData.csv', 'r')
    infile.readline()               # skip 2 header records
    infile.readline()

    destinations = []







    infile.close()
    return destinations                     # the LIST of OBJECTS