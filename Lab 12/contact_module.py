# MODULE:  contact_module                   used by PROJECT:  ContactsProgram
#          contains Contact CLASS
# AUTHOR:  Andrew Kroll                     DESIGNER:  Dr. Kaminski
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class Contact:
    # ----------------------------------------------------- INSTANCE VARIABLES
    # PRIVATE
    # __name     : str
    # __phone    : str
    # ------------------------------------------- ATTRIBUTE INITIALIZER METHOD
    def __init__(self, name='', phone=''):  # uses default values if
        # "caller" not provide parameters
        self.__name = name
        self.__phone = str(phone)
        print('OK, added a new Contact instance (without data values)')

    # -------------------------------------------- STATE REPRESENTATION METHOD
    def __str__(self):
        state = 'Contact:  ' + self.__name
        return state

    # --------------------------------------------------------- SETTER METHODS
    def set_name(self, name):
        self.__name = name

    def set_phone(self, phone):
        self.__phone = str(phone)

    # --------------------------------------------------------- GETTER METHODS

    def get_name(self) -> str:
        return self.__name

    def get_phone(self) -> str:
        return self.__phone

    # ---------------------------------------------------------- OTHER METHODS
    def get_initial(self):
        return self.__name[0:1]

    def get_area_code(self):
        return self.__phone[0:3]

    def get_local_num(self):
        return self.__phone[3:10]

    def get_local_prefix(self):
        prefix = self.__phone[3:6]
        return prefix

    def is_sw_michigan(self):
        if self.get_area_code() == '269':
            return True
        return False

    def is_wmu(self):
        if self.is_sw_michigan() and (self.get_local_prefix() == '387' or
                                      self.get_local_prefix() == '276'):
            return True
        return False

    def make_nice_phone(self):
        return "({}) {}-{}".format(self.get_area_code(),
                                   self.get_local_prefix(),
                                   self.get_local_num()[3:7])
