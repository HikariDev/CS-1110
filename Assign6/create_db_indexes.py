# MODULE:  create_db_indexes.py            used by PROJECT: A6WorldDataQueries
# AUTHOR: Andrew Kroll                     DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Builds the db and 3 indexes using data from the file.
# INPUT FILE:  A6WorldData.csv
#       - (no validity-checking - assume all data in file is valid)
#       - (data from 2000, outdated, but use it anyway)
#       - 1 header record to skip over
#       - fields in data records (in this order):
#               code, id, name, cont, region, size, pop, life_exp
#                   - don't use region or life_exp field in this project
#                   - FYI:  code, id, name are all UNIQUE in the data
#           Before putting these fields in the db or indexes
#               - convert pop and id to int's
#               - convert name to ALL CAPS
#               - convert size to int, then convert sqKm (in file) to sqMiles
#                   by multiplying sqKm by 0.3861 and store sqMiles in db
# STRUCTURE OF THE 4 DICTIONARIES:
#       db		    key is name
#                   value is a tuple containing (code,id,cont,size,pop)
#       id_index	key is id       value is name
#       code_index	key is code	    value is name
#       cont_index	key is cont
#                   value is a list containing all names in this cont
# ----------------------------------------------------------------------------


def build_4_dictionaries():
    infile = open('A6WorldData.csv', 'r')

    db = {}  # name = [code, id, cont, size, pop]
    id_index = {}  # id = name
    code_index = {}  # code = name

    cont_list_of_names = [[] for i in range(0, 6)]  # used to build LOLs
    # which is later used to build cont_index
    for line in infile:
        record = line.replace("\n", "").split(",")
        if use_record(record):            # add parameter(s)
            rec_code = record[0]
            rec_id = int(record[1])
            rec_name = record[2].upper()
            rec_cont = record[3]
            rec_size = int(record[5])*0.3861
            rec_pop = int(record[6])
            db.update({rec_name: [rec_code, rec_id, rec_cont, rec_size,
                                  rec_pop]})
            id_index.update({rec_id: rec_name})
            code_index.update({rec_code: rec_name})
            cont_list_of_names[which_list(rec_cont)].append(rec_name)
    cont_index = build_cont_index(cont_list_of_names)  # add parameter(s)
    infile.close()
    return db, id_index, code_index, cont_index


# decides whether to INCLUDE record in the db/indexes OR NOT
# SKIP THESE RECORDS:
#       any record in cont Antarctica
#       any record with a pop < 1000    (convert to int before checking)
def use_record(record):       # add parameter(s)
    if record[6] == "POPULATION":
        return False
    elif record[3] == "Antarctica" or int(record[6]) < 1000:
        return False
    return True


# decide which of the 6 continent lists to use in the LOL
def which_list(continent):       # add parameter(s)
    continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania',
                  'South America']
    for i in range(0, len(continents)):
        if continent == continents[i]:
            return i
    return -1            # using a temp dummy value - return correct int, 0-5


def build_cont_index(cont_list_of_names):  # add parameter(s)
    continents = ['Africa', 'Asia', 'Europe', 'North America', 'Oceania',
                  'South America']
    cont_index = {}
    for i in range(0, len(continents)):
        cont_name = continents[i]
        country_list = cont_list_of_names[i]
        cont_index.update({cont_name: country_list})
    return cont_index
