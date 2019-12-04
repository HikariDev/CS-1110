# MODULE:  trans_handler                        used by PROJECT:  PureMichigan
# AUTHOR: Andrew Kroll                          DESIGNER:  Dr. Kaminski
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Assign7 import Destination
# module to have access to the Destination CLASS

def do_transactions(destinations):
    infile = open('DestinationsTrans.csv', 'r')
    print('\nDoing Transactions . . ')
    for line in infile:
        fields = line.split(',')
        trans_type = fields[0]
        if trans_type == 'showPlace':
            show_place(fields[1], destinations)
        elif trans_type == 'showPenn':
            show_penninsula(fields[1], destinations)
        elif trans_type == 'showCat':
            show_category(fields[1], destinations)
        elif trans_type == 'showClose':
            show_close_to_KZO(int(fields[1]), destinations)
        else:    # must be showAll
            show_all(destinations)
    infile.close()


def show_place(target, destinations):             # show data for target place
    print('\nDESTINATION:', target)


def show_penninsula(target, destinations):   # show data for target:  LP or UP
    print('\nDESTINATIONS IN THE', target, 'PENNINSULA')

                               # show data for target:  nature or city or town
def show_category(target, destinations):
    print('\nDESTINATIONS IN', target, 'CATETORY')

                                        # show data <= distance from Kalamazoo
def show_close_to_KZO(distance, destinations):
    print('\nDESTINATIONS WITHIN', distance, 'MILES OF Kalamazoo')


def show_all(destinations):                # show all destinations in the list
    print('\nALL DESTINATIONS')
