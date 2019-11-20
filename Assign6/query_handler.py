# MODULE:  query_handler.py                used by PROJECT: A6WorldDataQueries
# AUTHOR:                                  DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Processes queries from a transaction file and writes results
#       to a log file.
# INPUT:  A6Queries.csv - each record contains:     trans_type,target
#       (Some requests are successful, some are unsuccessful).
# OUTPUT:  A6Log.txt - each query results in:
#       1) echo the query itself (e.g., name,United States)
#       2) show results (i.e., use show_a_country function)
#           (NOTE:  successful cont queries show MULTIPLE countries)
#           OR, for unsuccessful requests: show:  "Sorry, target not valid"
#       3) a blank line
# STRUCTURE OF THE 4 DICTIONARIES:
#       db		    key is name
#                   value is a tuple containing (code,id,cont,size,pop)
#       id_index	key is id       value is name
#       code_index	key is code	    value is name
#       cont_index	key is cont
#                   value is a list containing all names in this cont
# ----------------------------------------------------------------------------


def do_query_processing():          # add parameter(s)
    infile = open('A6Queries.csv', 'r')
    outfile = open('A6Log.txt', 'w')

    infile.close()
    outfile.close()


# ----------------------------------------------------------------------------
# this "decider" function calls 1 of the do_..._query functions,
#               depending on trans_type
def call_a_query_processor():       # add parameter(s)
    pass


# ----------------------------------------------------------------------------
def do_name_query(db, name) -> [str, int, str, float, int]:  # add parameter(s)
    # NOTE:  name from query file should be converted to all CAPS before...
    #           since db's name is all CAPS
    return db[name.upper()]


def do_id_query(db, id_index, id) -> str:          # add parameter(s)
    return do_name_query(db, id_index[id])


def do_code_query(db, code_index, code) -> str:        # add parameter(s)
    return do_name_query(db, code_index[code])


def do_cont_query(db, cont_index, cont) -> [str]:        # add parameter(s)
    return do_name_query(db, cont_index[cont])


def do_pop_query(db, spec, spec_pop):          # add parameter(s)
    ret = []
    for name in db.keys():
        pop = db[name][4]
        if spec == ">":
            if pop > spec_pop:
                ret.append(db[name])
        elif spec == "<":
            if pop < spec_pop:
                ret.append(db[name])
    return ret


# ----------------------------------------------------------------------------

# do_..._query functions all use this to actually WRITE a country to OUTFILE
def show_a_country(outfile, id, code, name, cont, size, pop):
    if len(name) > 15:
        name = name[0:15]
    else:
        name = name.ljust(15, ' ')
    name = name.capitalize()
    f_str = '{:3d} {:3s} {:15s} ({:13s}) {:10,d} sq.miles, pop {:14,d}'
    line = f_str.format(id,code,name,cont,size,pop)
    outfile.write(line + '\n')

