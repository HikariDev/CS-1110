# PROJECT: Ex2.py       uses MODULES:  load_data, reports, averages
# AUTHOR: Andrew Kroll                              DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Program
#       1) loads data from input file into 4 parallel lists
#       2) using the parallel LISTS (not the file), does some data & stats to
#               the console (selecting just SOME countries/continents/regions)
#           a) reports:  first 4 show a series of countries that fit criteria
#           b) averages:  next 2 calculate/show the average for the selected
#               areas
#           c) list of countries in South America countries (just their names)
#               in alphabetical order
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
from Exam2 import load_data, reports, averages


def main():
    # call appropriate functions in appropriate places
    name, cont, region, age = load_data.fill_lists()
    print('OK, done loading data from file to lists')
    print('\nthe 5 countries with LOWEST median ages')
    reports.do_lowest(name, cont, region, age)
    print('\nthe 5 countries with HIGHEST median ages')
    reports.do_highest(name, cont, region, age)
    print('\nthe G7 countries')
    reports.do_G7(name, cont, region, age)
    print('\tsome countries in the NEWS')
    reports.do_in_the_news(name, cont, region, age)
    print('\nAVERAGE median age for Europe: ', end='')
    averages.do_ave_europe(name, cont, region, age)
    print('\nAVERAGE median age for Central Africa & Western Africa' +
          '\n\t(2 regions combined): ', end='')
    averages.do_ave_2_africa_regions(name, cont, region, age)
    print('\n\nCountries in South America (in alphabetical order)')
    show_sa_countries_in_order(name, region)


def show_sa_countries_in_order(name, region):   # South America countries' names (in order)
    sa_countries = []
    for i in range(len(name)):
        if region[i] == "South America":
            sa_countries.append(name[i])
    sa_countries.sort()
    for i in range(len(sa_countries)):
        print(sa_countries[i])
    pass


main()
