# MODULE:  query.py                         used by PROJECT:  E3Project.py
# AUTHOR:  Andrew Kroll
# DESIGNER:  Dr. Kaminski
# INPUT DATA FILE:  E3Queries.csv
#        - remember to rstrip('\n')
# OUTPUT to CONSOLE - for each query:
#       1) echo query,    2) give query result(s),     3) print a blank line
# THE 2 DICTIONARIES:
#       1) loc_dict (location dictionary)       key:  name
#               value:  (continent, region) tuple
#       2) inc_dict (income dictionary)         key:  name
#               value:  (house_inc, per_cap_inc, pop) tuple - stored as 3 int's
#
# IMPORTANT:  Add parameters and return values as needed.
#
# IMPORTANT NOTE:  There are some missing countries in each of the 2
#       dictionaries.  And sometimes a country name is spelled differently in
#       a dictionary.  So there's not going to be a perfect matchup.
#       This project only handles EXACT MATCHES (as described in the comments
#       below).
#
# HELPFUL HINT about grabbing tuple fields from a dictionary:
#       value1, value2, value3 = the_dictionary[the_key]
# ----------------------------------------------------------------------------

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  MINI-MAIN
# Function processes E3Queries file.  It includes the "big decider" which calls
# one of the 3 transaction handlers.


def do_trans(loc_dict, inc_dict):
    print('\nOK, starting transaction processing\n')
    with open("E3Queries.csv", 'r') as file:
        for line in file:
            split = line.replace("\n", "").split(",")
            if split[0] == "country":
                do_country_trans(loc_dict, inc_dict, split[1])
            elif split[0] == "region":
                do_region_trans(loc_dict, inc_dict, split[1])
            elif split[0] == "income":
                do_income_trans(loc_dict, inc_dict, int(split[1]))


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - TRANSACTION HANDLERS
# SUGGESTION:  in   is a useful operator to check if a key is in a dictionary

# country queries
#   - if FIND name in BOTH dictionaries - call show_the_country
#   - if NOT FIND name in one (or both) of the dictionaries
#       	print 'SORRY, missing data for that country'    for query result
def do_country_trans(loc_dict, inc_dict, country):
    if country not in loc_dict or country not in inc_dict:
        print("Sorry, missing data for", country)
    else:
        loc = loc_dict[country]
        inc = inc_dict[country]
        show_the_country(country, loc[0], loc[1], inc[0], inc[1], inc[2])


# region queries
#   - search loc_dict for ALL matching regions
#   - for any MATCH, try to also get data (for that name) from inc_dict
#           - if FIND name there, call show_the_country
#           - if NOT FIND name in inc_dict, just DON'T print that country
def do_region_trans(loc_dict, inc_dict, region):
    for country in loc_dict:
        if loc_dict[country][1] == region:
            if country not in inc_dict:
                continue
            loc = loc_dict[country]
            inc = inc_dict[country]
            show_the_country(country, loc[0], loc[1], inc[0], inc[1], inc[2])


# income queries
#   - search inc_dict for ALL matches:  (house_inc >= value from trans file)
#   - for any MATCH, try to also get data (for that name) from loc_dict
#           - if FIND name there, call show_the_country
#           - if NOT FIND name in loc_dict, just DON'T print that country
# REMINDER:  Convert target_income to an int before comparison
def do_income_trans(loc_dict, inc_dict, income):
    for country in inc_dict:
        if inc_dict[country][0] >= income:
            if country not in loc_dict:
                continue
            loc = loc_dict[country]
            inc = inc_dict[country]
            show_the_country(country, loc[0], loc[1], inc[0], inc[1], inc[2])
    pass


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -  UTILITIES
# SUGGESTION:  use slicing
# REMINDER:  the income dictionary stored these last 3 fields as int's
def show_the_country(name, cont, region, house_inc, per_cap_inc, pop):
    # add code here to truncate NAME to just the 1st 15 characters
    #           if name is longer than 15 characters
    if len(name) > 15:
        name = name[0:15]
    # add code here to truncate REGION to just the 1st 15 characters
    #           if region is longer than 15 characters
    if len(region) > 15:
        region = region[0:15]
    f_str = '{:15s} in {:13s} ({:15s}) pop: {:14,d}   ${:6,d}   ${:6,d}'
    nice_line = f_str.format(name, cont, region, pop, house_inc, per_cap_inc)
    print(nice_line)
