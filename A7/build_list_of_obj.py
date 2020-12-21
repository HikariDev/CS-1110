# MODULE:  build_list                           used by PROJECT:  PureMichigan
# AUTHOR: Andrew Kroll                          DESIGNER:  Dr. Kaminski
# NOTE:  Data lines have a ',' at the end besides the '\n' which both need
#       removing before splitting the line into fields.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from A7 import Destination


def load_file_data():
    infile = open('PureMichiganData.csv', 'r')
    infile.readline()  # skip 2 header records
    infile.readline()
    destinations = []
    line = infile.readline()
    while line != '':
        destinations.append(Destination.Destination(line))
        line = infile.readline()

    infile.close()
    return destinations
