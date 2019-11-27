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
        result = call_a_query_processor(db, id_index, code_index, cont_index,
                                        query)
        outfile.write(line)
        if result is None:
            print("Sorry, target is not valid\n")
        elif type == "pop":
            for entry in result:
                show_a_country(outfile, result)
        else:
            show_a_country(outfile, result)
        outfile.write("\n")
    infile.close()
    outfile.close()


# ----------------------------------------------------------------------------
# this "decider" function calls 1 of the do_..._query functions,
#               depending on trans_type
def call_a_query_processor(db, id_index, code_index, cont_index, query):
    type = query[0]
    arg = query[1]
    if type == "name":
        return do_name_query(db, arg)
    elif type == "id":
        return do_id_query(db, id_index, arg)
    elif type == "code":
        return do_code_query(db, code_index, arg)
    elif type == "cont":
        return do_cont_query(db, cont_index, arg)
    elif type == "pop":
        return do_pop_query(db, arg)
    return None


# ----------------------------------------------------------------------------
def do_name_query(db, name) -> [str, int, str, float, int]:  # add parameter(s)
    # NOTE:  name from query file should be converted to all CAPS before...
    #           since db's name is all CAPS
    if name.upper() in db:
        return db[name.upper()]
    return None


def do_id_query(db, id_index, id):          # add parameter(s)
    if id in id_index:
        return do_name_query(db, id_index[id])
    return None


def do_code_query(db, code_index, code):        # add parameter(s)
    if code in code_index:
        return do_name_query(db, code_index[code])
    return None


def do_cont_query(db, cont_index, cont):        # add parameter(s)
    if cont in cont_index:
        return do_name_query(db, cont_index[cont])
    return None


def do_pop_query(db, query_pop):          # add parameter(s)
    temp = []
    for name in db.keys():
        pop = db[name][4]
        spec = query_pop[0:1]
        if spec == ">":
            if pop > int(query_pop[1:]):
                temp.append(db[name])
        elif spec == "<":
            if pop < int(query_pop[1:]):
                temp.append(db[name])
    return temp


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

