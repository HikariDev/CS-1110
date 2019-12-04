# PROJECT:  PureMichigan                        uses MODULES:  see imports
# AUTHOR: Andrew Kroll                          DESIGNER:  Dr. Kaminski
# NAMING NOTE:
#       destinations - the list of objects
#       destination  - a single object (an INTANCE of Destination CLASS type)
#       Destinations - MODULE containing Destinations CLASS
#       Desitnations - CLASS name
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Assign7 import build_list_of_obj, pickling, trans_handler


def main():
    mode = input('Enter run mode:  N for Normal, S for Startup:  ')
    if mode[0].upper() == 'S':
        destinations = build_list_of_obj.load_file_data()
        print('OK, Destinations list BUILT from initial data FILE\n')
    else:
        destinations = pickling.load_list_of_obj()
        print('OK, Destinations list LOADED from BACKUP\n')
    trans_handler.do_transactions(destinations)
    pickling.save_list_of_obj(destinations)
    print('OK, Destinations dictionary SAVED to BACKUP\n')

    print('\nTHE END')


main()
