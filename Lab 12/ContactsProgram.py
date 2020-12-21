# PROJECT:  ContactsProgram                 uses MODULE:  contact_module
#                                                   contains Contact CLASS
# AUTHOR:                                   DESIGNER:  Dr. Kaminski
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Lab12 import contact_module as con

def main():
    print('STARTING THE PROGRAM\n')
    person1 = con.Contact()
    person2 = con.Contact()

    name = 'John Smith'             # hardcoded instead of user input
    phone = 2693871000              # hardcoded instead of user_input

    person1.set_name(name)
    person1.set_phone(phone)

    name = 'Latisha Brown'          # hardcoded instead of user input
    phone = 6163871000              # hardcoded instead of user_input

    person2.set_name(name)
    person2.set_phone(phone)

    # Test some class methods on the 2 objects.
    test_methods(person1)
    test_methods(person2)

    print('\nTHE END')


def test_methods(person: con.Contact):
    print('\nTESTING')
    print(person)

    # Call the methods to get the data needed from the object to print the
    #       test results below (once you've written the class's methods).
    name = person.get_name()
    initial = person.get_initial()
    phone = person.get_phone()
    area_code = person.get_area_code()
    local_number = person.get_local_num()
    local_prefix = person.get_local_prefix()
    nice_phone = person.make_nice_phone()
    is_sw_michigan = person.is_sw_michigan()
    is_wmu = person.is_wmu()

    # print test results
    f_str = '{:s} (starts with {:s}) has phone number: {:s}'
    print(f_str.format(name, initial, phone))

    f_str = '\tarea code: {:s}, local number: {:s}, (local prefix: {:s})'
    print(f_str.format(area_code, local_number, local_prefix))

    print('\tphone number', nice_phone, end='')
    if is_sw_michigan:
        print(' IS from SW Michigan')
    else:
        print(' is NOT from SW Michigan')

    print('\tand the number', end='')
    if is_wmu:
        print(' IS a WMU number')
    else:
        print(' is NOT a WMU number')


main()
