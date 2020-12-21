# PROGRAM: Assignment 5: World Population Report
# AUTHOR: Andrew Kroll
# DATE: 11/13/2019
# DESCRIPTION: This project prepares the tables and stats needed, then prints
# The Population Report (3 tables) from data stored internally in a list of
# tuples. The internal data was first loaded (stored in the list of tuples)
# from an external .csv file before doing any processing for the report.


def main():
    temp_data = []
    data = []
    with open('CountryData.csv', 'r') as file:
        temp_data = list(file)
    for i in range(len(temp_data)):
        line = temp_data[i]
        if line.startswith('INSERT'):
            line = clean_up_data(line)
            if use_this_record(line):
                line = format_record(line)
        data.append(line)
    print_header()
    do_table1(data)
    do_table2(data)
    do_table3(data)
    print_footer()


def clean_up_data(data):
    data = data.replace("INSERT INTO Country VALUES (", '') \
        .replace('\'', '').replace(');', '').replace('\n', '') \
        .split(",")
    if len(data[1]) > 16:
        data[1] = data[1][0:16]
    if len(data[5]) > 16:
        data[5] = data[5][0:16]
    data[2] = int(data[2])
    data[6] = int(data[6])
    data[3] = float(data[3])
    return data


def use_this_record(data):
    if data[2] <= 0 or data[3] <= 0 or data[4] == "Antarctica":
        return False
    return True


def format_record(data):
    return [data[0], data[1], data[2], data[3], data[4], data[5], data[6]]


def get_in_continent(data, continent):
    temp = []
    for line in data:
        if continent.lower() in line[4].lower():
            temp.append(line)
    return temp


def print_header():
    print("WORLD POPULATION REPORT\n")


def do_table1(data):
    f_str = "{0:4s} {1:16s} {2:16s} {3:^7.1f}"
    print("\nTABLE 1:  AFRICA:  LIFE EXPECTANCY BY COUNTRY\n")
    print("Code Name             Region           LifeExp")
    print("---- ---------------- ---------------- -------")
    for record in get_in_continent(data, "Africa"):
        print(f_str.format(record[0], record[1], record[5], record[3]))
    print()


def do_table2(data):
    euro_countries = get_in_continent(data, "Europe")
    temp_min = [-1, ""]
    temp_max = [-1, ""]
    total = 0
    print("\nTABLE 2:  EUROPE:  POPULATION & LAND AREA (",
          len(euro_countries), " countries)\n", sep='')
    print("POPULATION")
    print("----------")
    for record in euro_countries:
        if record[2] > temp_max[0] or temp_max[0] == -1:
            temp_max = record[2], record[1]
        if record[2] < temp_min[0] or temp_min[0] == -1:
            temp_min = record[2], record[1]
        total += record[2]
    print("Largest:{0:>16,}\t{1:}".format(temp_max[0], temp_max[1]))
    print("Smallest:{0:>15,}\t{1:}".format(temp_min[0], temp_min[1]))
    print("Average:{0:>16,d}".format(total//len(euro_countries)))
    print("Total:{0:>18,d}\n".format(total))
    print("LAND AREA (sq km)")
    print("-----------------")
    temp_min = [-1, ""]
    temp_max = [-1, ""]
    for record in euro_countries:
        if record[6] > temp_max[0] or temp_max[0] == -1:
            temp_max = record[6], record[1]
        if record[6] < temp_min[0] or temp_min[0] == -1:
            temp_min = record[6], record[1]
        total += record[6]
    print("Largest:{0:>16,}\t{1:}".format(temp_max[0], temp_max[1]))
    print("Smallest:{0:>15,}\t{1:}".format(temp_min[0], temp_min[1]))
    print("Average:{0:>16,d}".format(total//len(euro_countries)))
    print("Total:{0:>18,d}\n".format(total))


def do_table3(data):
    print("\nTABLE 3: LIFE EXPECTANCY BY CONTINENT\n")
    print("Continent        Highest Lowest Wt.Average")
    print("---------------- ------- ------ ----------")
    for continent in ['Africa', 'Asia', 'Europe', 'North America',
                      'Oceania', 'South America']:
        high = -1
        low = -1
        numerator = 0
        denominator = 0
        for country in get_in_continent(data, continent):
            if country[3] > high or high == -1:
                high = country[3]
            if country[3] < low or low == -1:
                low = country[3]
            numerator += country[2] * country[3]
            denominator += country[2]
        life_exp = numerator/denominator
        print("{0:16} {1:^7.1f} {2:^6.1f} {3:^10.1f}".format(continent, high,
                                                             low, life_exp))


def print_footer():
    print("\n<<<< END OF REPORT >>>>")


main()
