import random

with open("RanStudData.csv", 'w') as file:
    for i in range(50):
        ssn = random.randint(300000000, 399999999)
        win = random.randint(100000000, 999999999)
        age = random.randint(17, 35)
        zip_code = random.randint(49000, 49999)
        city = ""
        if zip_code % 2 == 0:
            city = "Kalamazoo"
        elif ssn % 10 == 5 or ssn % 10000000 == 7:
            city = "Portage"
        elif ssn % 10 == 1:
            city = "Grand Rapids"
        elif 320000000 >= ssn >= 300000000:
            city = "Plainwell"
        gpa = random.uniform(0, 4)
        file.write("{0},{1},{2},{3},{4},{5:.2f}\n".format(ssn, win,
                                                age, zip_code, city, gpa))
