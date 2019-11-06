# MODULE:  averages                                 used in PROJECT: Ex2.py
# AUTHOR: Andrew Kroll                              DESIGNER:  Dr. Kaminski
# DESCRIPTION:  The functions here find/print the average median age
#       to the console for the specified group (showing 1 decimal place)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


def do_ave_europe(name, cont, region, age):
    count = 0
    total = 0
    for i in range(len(age)):
        if cont[i] == "Europe":
            count += 1
            total += age[i]
    print("{:.1f}".format(total/count))


def do_ave_2_africa_regions(name, cont, region, age): #Western and Central Africa
    count = 0
    total = 0
    for i in range(len(age)):
        if region[i] == "Western Africa" or region[i] == "Central Africa":
            total += age[i]
            count += 1
    print("{:.1f}".format(total/count))
