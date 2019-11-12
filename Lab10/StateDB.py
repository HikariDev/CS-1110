# PROJECT:  StateDB.py                     uses MODULES:  see imports below
# AUTHOR: Andrew Kroll                               DESIGNER: Dr. Kaminski
# DESCRIPTION:  Creates a "database" (DB) of state information so it can
#       be queried by the user.  The DB is stored in a dictionary.
#       2 modes - ask user for S or N (capitalize their response for safety):
#       1) Startup (S):
#          a) AT START:  DB created & loaded with data from StateData.csv file
#          b) AT END:    DB dumped (pickled) to StateDB.bin
#       2) Normal (N):
#          a) AT START:  data loaded (unpickled) from StateDB.bin
#          b) AT END:    DB dumped (pickled) to StateDB.bin
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from Lab10 import create_db as create
from Lab10 import dump_load_db as backup
from time import sleep


def main():
    temp = input("(S)tartup or (N)ormal? ").upper()
    data = None
    while temp != "S" and temp != "N":
        temp = input("(S)tartup or (N)ormal? ").upper()
    if temp == "S":
        data = create.main()
    else:
        data = backup.load()
    print("The database has been loaded and is ready for querying.")
    while temp != "DONE":
        temp = input("Enter a state name, or 'DONE' to exit! ").upper()
        if temp in data:
            s_data = data[temp]
            f_str = "Information about {}:\n\tPopulation: {}\n\tCode: {}" \
                    "\n\tElectoral Votes: {}\n\tUS Representatives: {}\n\t" \
                    "US Senators: {}\n"
            print(f_str.format(temp, s_data[0], s_data[1], s_data[2],
                               s_data[3], s_data[4]))
        elif temp != "DONE":
            print(temp, "is not a valid state name!")
    backup.dump(data)
    print("\nDatabase saved!\n\nGood bye!")
    sleep(3)
    # ask user if Startup or Normal
    # depending on response:
    #       do 1a OR 2a (see top-comment) to fill DB (dictionary) with data
    # give user status message that DB is ready to query

    # start query process: - loop til DONE
    # HUMAN ALGORITHM:
    #       user provides state name (convert it to all CAPS)
    #       lookup name in DB (could be successful or unsuccessful)
    #       if it's in the DB, find it and print state's data
    #       else print that it's an invalid state name
    # PROGRAM IMPLEMENTATION:
    #       You're using a while loop with sentinel for done,
    #           so the loop structure is . . . (instead of what's shown above)
    #       Convert name to all caps since that's
    #           1) what's in the DB for the key
    #           2) that's what the while condition's watching for, 'DONE'

    # do 1b (same as 2b) in top_comment)
    # reassure user that you've saved the DB


main()
