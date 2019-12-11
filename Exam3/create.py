# MODULE:  create.py                        used by PROJECT:  E3Project.py
# AUTHOR:  Andrew Kroll
# DESIGNER:  Dr. Kaminski
# INPUT DATA FILES:
#   1) E3LocationData.csv (1 header record)
#      - SKIP continent Antarctica
#      - SKIP any country with population < 400000
#      - ONLY USING FIELDS:  2, 3, 4, 6 in this project
#   2) E3IncomeData.csv (2 header records)
#      - CLEAN UP records before splitting to fields - replace with ''
#           1st)  '\n' from end (as usual)
#           2nd)  '0"'
#           3rd)  '"'
#           4th)  '.'
# THE 2 DICTIONARIES:
#   1) loc_dict (location dictionary)
#               key:  name
#               value:  (continent, region) tuple
#       EXAMPLE of what's stored:
#               Andorra         (Europe, Southern Europe)
#               Macao           (Asia, Eastern Asia)
#   2) inc_dict (income dictionary)
#               key:  name
#               value:  (house_inc, per_cap_inc, pop) tuple - stored as 3 int's
#       EXAMPLE of what's stored:
#               Denmark         (44360, 18262, 5771876)
#               United States   (43585, 15480, 329064917)
#
# IMPORTANT:  Add parameters and return values as needed.
# ----------------------------------------------------------------------------


def make_loc_dict():
    loc_dict = {}
    with open("E3LocationData.csv", 'r') as file:
        for line in file:
            if line == "CODE,ID,NAME,CONTINENT,REGION,LAND_SIZE,POPULATION," \
                       "LIFE_EXPECTANCY\n":
                continue
            split = line.replace("\n", "").split(",")
            name = split[2]
            continent = split[3]
            region = split[4]
            population = int(split[6])
            if continent == "Antarctica" or population < 400000:
                continue
            loc_dict.update({name: [continent, region]})
    print('OK, finished making location dictionary')
    return loc_dict


def make_inc_dict():
    inc_dict = {}
    with open("E3IncomeData.csv", 'r') as file:
        for line in file:
            if "," not in line:
                continue
            split = line.replace("\n", "").replace("0\"", "") \
                .replace("\"", "").replace(".", "").split(",")
            name = split[0]
            if name == "name":
                continue
            house_inc = int(split[1])
            per_cap_inc = int(split[2])
            pop = int(split[3])
            inc_dict.update({name: [house_inc, per_cap_inc, pop]})
    print('OK, finished making location dictionary')
    return inc_dict
