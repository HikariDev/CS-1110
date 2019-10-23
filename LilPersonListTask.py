def main():
    names = []
    ages = []
    salaries = []

    with open("LilPeople4Lines.txt") as file:
        data = list(file)
        i = 0
        for line in data:
            if i % 4 == 0:
                names += [line.replace("\n", "")]
            elif i % 4 == 2:
                ages += [line.replace("\n", "")]
            elif i % 4 == 3:
                salaries += [line.replace("\n", "")]
            i += 1
        for i in range(len(ages)):
            ages[i] = int(ages[i])
        for i in range(len(salaries)):
            salaries[i] = float(salaries[i])

        total_salary = 0
        average_salary = 0
        average_age = 0
        temp_min = -1
        temp_mins_name = ""
        temp_max = -1
        temp_maxs_name = ""

        for i in range(len(ages)):
            if temp_min == -1 or ages[i] < temp_min:
                temp_min = ages[i]
                temp_mins_name = names[i]
            if temp_max == -1 or ages[i] > temp_max:
                temp_max = ages[i]
                temp_maxs_name = names[i]
            average_age += ages[i]
        average_age = average_age // len(ages)
        for salary in salaries:
            total_salary += salary
        average_salary = total_salary / len(salaries)

    print("Lil Person List Task\n")
    print("{0:<8}\t{1:>4}\t{2:>10}".format("NAME", "AGE", "SALARY"), "\n")
    f_str = "{0:<8}\t{1:>4}\t{2:>10.2f}"
    for i in range(len(names)):
        print(f_str.format(names[i], ages[i], salaries[i]))
    print("------------------------------")
    print("{0:>14}\t{1:>14}\t{2:>12}\t{3}\t\t\t{4}".format("TOTAL SALARY",
        "AVERAGE SALARY","AVERAGE AGE","MIN AGE","MAX AGE"))
    print("{0:>14.2f}\t{1:>14.2f}\t{2:>12}\t{4}: {3}\t\t{6}: {5}".format(
        total_salary, average_salary, average_age, temp_min, temp_mins_name,
        temp_max, temp_maxs_name))


main()
