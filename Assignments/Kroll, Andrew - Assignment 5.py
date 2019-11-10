# PROGRAM: Assignment 5: World Population Report
# AUTHOR: Andrew Kroll
# DATE: 11/07/2019
# DESCRIPTION: This project prepares the tables and stats needed, then prints
# The Population Report (3 tables) from data stored internally in a list of
# tuples. The internal data was first loaded (stored in the list of tuples)
# from an external .csv file before doing any processing for the report.


def main():
    data = []
    with open('CountryData.csv', 'r') as file:
        data = list(file)

    for line in data:

        if line.startswith('INSERT'):
            line = line.replace("INSERT INTO Country VALUES (", '')\
                .replace('\'', '').replace(');', '').replace('\n', '')\
                .split(",")
            if len(data[len(data)-1][1]) > 16:
                data[len(data)-1][1] = data[len(data)-1][0:16]



main()
