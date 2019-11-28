# MODULE:  query_handler.py                used by PROJECT: A6WorldDataQueries
# AUTHOR: Andrew Kroll                     DESIGNER:  Dr. Kaminski
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


def do_query_processing(db, id_index, code_index, cont_index):
    infile = open('A6Queries.csv', 'r')
    outfile = open('A6Log.txt', 'w')
    for line in list(infile):
        query = line.replace("\n", "").split(",")
        outfile.write(query[0] + "," + query[1] + ": ")
        call_a_query_processor(db, outfile, id_index, code_index, cont_index,
                               query)
        outfile.write("\n")
    infile.close()
    outfile.close()


# ----------------------------------------------------------------------------
# this "decider" function calls 1 of the do_..._query functions,
#               depending on trans_type
def call_a_query_processor(db, outfile, id_index, code_index, cont_index, query):
    type = query[0]
    arg = query[1]
    if type == "name":
        return do_name_query(db, outfile, arg)
    elif type == "id":
        return do_id_query(db, outfile, id_index, arg)
    elif type == "code":
        return do_code_query(db, outfile, code_index, arg)
    elif type == "cont":
        return do_cont_query(db, outfile, cont_index, arg)
    elif type == "pop":
        return do_pop_query(db, outfile, arg, query[2])
    return None


# ----------------------------------------------------------------------------
def do_name_query(db, outfile, name) -> [str, int, str, float, int]:
    # add parameter(s)
    # NOTE:  name from query file should be converted to all CAPS before...
    #           since db's name is all CAPS
    name = name.upper()
    if name in db:
        show_a_country(outfile, name, db[name])
    else:
        outfile.write("Sorry, target is not valid\n")


def do_id_query(db, outfile, id_index, id):          # add parameter(s)
    if id in id_index:
        name = id_index[id]
        do_name_query(db, outfile, name)
    else:
        outfile.write("Sorry, target is not valid\n")


def do_code_query(db, outfile, code_index, code):        # add parameter(s)
    if code in code_index:
        name = code_index[code]
        do_name_query(db, outfile, name)
    else:
        outfile.write("Sorry, target is not valid\n")


def do_cont_query(db, outfile, cont_index, cont):        # add parameter(s)
    if cont in cont_index:
        for country in cont_index[cont]:
            do_name_query(db, outfile, country)
    else:
        outfile.write("Sorry, target is not valid\n")


def do_pop_query(db, outfile, direction, query_pop):    # add parameter(s)
    count = 0
    for name in db.keys():
        pop = db[name][4]
        if direction == ">":
            if pop > int(query_pop[1:]):
                count += 1
                do_name_query(db, outfile, name)
        elif direction == "<":
            if pop < int(query_pop[1:]):
                count += 1
                do_name_query(db, outfile, name)
    if count == 0:
        outfile.write("Sorry, target is not valid\n")


# ----------------------------------------------------------------------------

# do_..._query functions all use this to actually WRITE a country to OUTFILE
def show_a_country(outfile, name, entry):
    code = entry[0]
    id = entry[1]
    cont = entry[2]
    size = entry[3]
    pop = entry[4]
    if len(name) > 15:
        name = name[0:15]
    else:
        name = name.ljust(15, ' ')
    name = name.capitalize()
    f_str = '{:3d} {:3s} {:15s} ({:13s}) {:10,d} sq.miles, pop {:14,d}'
    line = f_str.format(id, code, name, cont, size, pop)
    outfile.write(line + '\n')

