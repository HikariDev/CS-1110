# PROJECT: A6WorldDataQueries               uses MODULES:  see imports
# AUTHOR:                                   DESIGNER:  Dr. Kaminski
# DESCRIPTION:  (see main for the big picture of what the project does).
#           Project creates a "database" (DB) containing data for the countries
#       of the world, using country name as the access key. It also creates
#       3 indexes to provide additional ways to access the DB, using country
#       id or country code or continent as access keys.
#           The DB and 3 indexes are all implemented as dictionaries.
#           On the first run (Startup mode), the DB and indexes are built using
#       data from a data file.  On subsequent runs (Normal mode), the 4
#       dictionaries are loaded from a backup file using pickle's load
#       function.  (The 4 dictionaries are thus dumped to that backup file at
#       the end of the run - for use in a subsequent run).  (NOTE:  Don't
#       run Normal mode until you've run Startup mode successfully, as backup
#       file won't yet exist).
#           Project provides the ability to query the data - at this point
#       only "test mode" works (i.e., hardcoded queries in a transaction file,
#       with output going to a log file).  There is no "interactive mode"
#       (i.e., queries from an interactive user using a menu of options and
#       output to the console).
# ----------------------------------------------------------------------------

from Assign6 import create_db_indexes as create
from Assign6 import dump_load as backup
from Assign6 import query_handler as querying


def main():
    db, id_index, code_index, cont_index = create.build_4_dictionaries()
    querying.do_pop_query(db, ">", 500)

    mode = input('Enter run mode:  N for Normal, S for Startup:  ')
    if mode.upper() == 'S':
        db, id_index, code_index, cont_index = create.build_4_dictionaries()
        print('\nOK, initial db & indexes CREATED')
    # else:
    #     db, id_index, code_index, cont_index = backup.load_4_dictionaries()
    #     print('\nOK, db & indexes LOADED from backup')

    # querying.process_queries(db, id_index, code_index, cont_index)
    # print('\nOK, all queries in transaction file processed')
    # print('\tsee A6Log.txt for results')

    # backup.dump_inventory(db, id_index, code_index, cont_index)
    # print('\nOK, db & indexes SAVED to backup')

    print('\nTHE END')


main()
