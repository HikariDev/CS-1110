# MODULE:  Destination                          used by PROJECT:  PureMichigan
#           contains Destination CLASS
# AUTHOR: Andrew Kroll                          DESIGNER:  Dr. Kaminski
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Destination:
    # ----------------------------------------------------- INSTANCE VARIABLES
    #  __place (str) - name
    #  __near_town (str) - will come in as '' for category:  town & city,
    #                   in which case STORE the town/city category in here too
    #  __category (str) - town or city or nature
    #  __penn (str) - penninsula:  UP or ''
    #               - if it comes in as '', STORE 'LP' in here
    #  __distance (int) - distance from Kalamazoo in miles
    #                   will come in as a STRING as fields[4]
    #  __time (int) - drive time from Kalamazoo
    #               will come in as hours:minutes (e.g., 4:35, a STRING)
    #               STORE as total minutes (use : to split, then 4 * 60, . . .)
    # ------------------------------------------- ATTRIBUTE INITIALIZER METHOD
    # TODO: - place and category can be simple assignments
    #       - for the other 4, call their setters to do the "special handling"
    # NOTE:  fields is a list of STRINGS - 2 of the setters have to convert
    #       them to int's

    def __init__(self, fields):
        pass

    # ---------------------------------------------------- RETURN STATE METHOD
    def __str__(self):
        f_str = ('{:21s} (near {:12s}) in {:2s} {:3d} from KZO ' +
                 '({:4d} min drive), CATEGORY: {:s}')
        state = ''                          # TODO fix this - use f_str
        return state

    # --------------------------------------------------------- SETTER METHODS
    # TODO: add setters for all 6 - 2 are simple ones, 4 have some extra code


    # --------------------------------------------------------- GETTER METHODS
    # TODO:  add getters for all 6


    # ---------------------------------------------------------- OTHER METHODS
