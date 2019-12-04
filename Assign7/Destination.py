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
    #  __pen (str) - peninsula:  UP or ''
    #               - if it comes in as '', STORE 'LP' in here
    #  __distance (int) - distance from Kalamazoo in miles
    #                   will come in as a STRING as fields[4]
    #  __time (int) - drive time from Kalamazoo
    #               will come in as hours:minutes (e.g., 4:35, a STRING)
    #               STORE as total minutes (use : to split, then 4 * 60, . . .)
    # ------------------------------------------- ATTRIBUTE INITIALIZER METHOD

    def __init__(self, fields):
        fields = fields.split(",")
        self.set_place(fields[0])
        self.set_near_town(fields[1])
        self.set_category(fields[2])
        self.set_pen(fields[3])
        self.set_distance(fields[4])
        self.set_time(fields[5])

    # ---------------------------------------------------- RETURN STATE METHOD
    def __str__(self):
        f_str = ('{:22s} (near {:15s}) in {:2s} {:3d} mi from KZO ' +
                 '({:4d} min drive), CATEGORY: {:s}')
        state = f_str.format(self.get_place(), self.get_near_town(),
                             self.get_pen(), self.get_distance(),
                             self.get_time(), self.get_category())
        return state

    # --------------------------------------------------------- SETTER METHODS
    def set_place(self, place):
        self.__place = place

    def set_near_town(self, near_town):
        self.__near_town = near_town if near_town != "" else self.__place

    def set_category(self, category):
        self.__category = category

    def set_pen(self, peninsula):
        self.__pen = peninsula if peninsula != "" else "LP"

    def set_distance(self, distance):
        self.__distance = int(distance)

    def set_time(self, time):
        time = time.split(":")
        self.__time = int(time[0])*60 + int(time[1])

    # --------------------------------------------------------- GETTER METHODS
    def get_place(self) -> str:
        return self.__place

    def get_near_town(self) -> str:
        return self.__near_town

    def get_category(self) -> str:
        return self.__category

    def get_pen(self) -> str:
        return self.__pen

    def get_distance(self) -> int:
        return self.__distance

    def get_time(self) -> int:
        return self.__time

    # ---------------------------------------------------------- OTHER METHODS
