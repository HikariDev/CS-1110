# MODULE:  load_data.py                             used in PROJECT: Ex2.py
# AUTHOR:  Andrew Kroll                             DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Loads data from a data file into 4 parallel lists.
# INPUT DATA FILE:  WorldDataMedAge.csv
#       - no header records
#       - fields in each data record (in this order):
#               name, cont (continent), region, pop, size, age (median age)
#       - DO NOT LOAD records with median_age of 'N.A.' into the lists
#       - ONLY LOAD fields that are used in this project:
#               name, cont, region, age
# IMPORTANT TO NOTE:  File's data is sorted on median age, so the PARALLEL
#       LISTS' data will be in order by median age (low to high)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def fill_lists():
    name = []
    cont = []
    region = []
    age = []

    with open("WorldDataMedAge.csv", 'r') as file:
        lines = list(file)
        for i in range(len(lines)):
            # Niger,Africa,Western Africa,23310715,1266700,15
            lines[i] = lines[i].replace("\n", "")
            temp_name, temp_cont, temp_reg, temp_pop, temp_size, \
                temp_age = lines[i].split(",")
            if temp_age != "N.A.":
                name.append(temp_name)
                cont.append(temp_cont)
                region.append(temp_reg)
                age.append(int(temp_age))
    return name, cont, region, age
