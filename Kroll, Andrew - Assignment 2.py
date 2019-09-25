# PROGRAM: Assignment 2: The Laptop Shop
# AUTHOR: Andrew Kroll
# DATE: 09/024/2019
# DESCRIPTION: This program gives a monthly payroll report for the sales staff
# at The Laptop Shop

import re

TIERS = {0: 'Low', 1: 'Med', 2: 'High'}
PRICES = {'basic': 450.90, 'mid-range': 850.50, 'high-end': 1350.95}
COMMISSION = {'basic': 25, 'mid-range': 50, 'high-end': 75}

SUPER_BONUS = 400
MAX_BASE_SALARY = 10000
MAX_VALID_UNITS = 40
F_STR = "${0:>10,.2f}"


def sales(arr):
    return arr[0]*PRICES['basic'] + arr[1]*PRICES['mid-range'] + \
           arr[2]*PRICES['high-end']


def commission(arr):
    return arr[0]*COMMISSION['basic'] + arr[1]*COMMISSION['mid-range'] + \
           arr[2]*COMMISSION['high-end']


def bonus(sales):
    if sales > 2000:
        return sales * 0.01
    elif sales > 4000:
        return (sales - 4000) * 0.01 + 75
    elif sales > 7500:
        return (sales - 7500) * 0.015 + 75
    elif sales > 10000:
        return 300
    return 0


while True:  # Doing Stuff
    print("Enter Salesperson Data:")
    name = None
    base_salary = -1
    tier = -1
    laptops_sold = [-1, -1, -1]
    while True:  # User Input
        if name is None:
            name = str(input("Name: "))
        if base_salary < 0:
            try:
                a = float(input("Base Salary: $"))
                if 0 < a <= MAX_BASE_SALARY:
                    base_salary = a
                else:
                    print("Invalid base salary!",
                          "(Must be positive!)" if a < 0 else
                          "(Must be less than $" + str(MAX_BASE_SALARY) + ")")
                    continue
            except ValueError:
                print("Invalid base salary!")
                continue
        if tier < 0:
            a = str(input("Tier ('L', 'M', or 'H'): ")).upper()
            if len(a) > 0 and a.startswith('L'):
                tier = 0
            elif len(a) > 0 and a.startswith('M'):
                tier = 1
            elif len(a) > 0 and a.startswith('H'):
                tier = 2
            else:
                print("Invalid Tier! (Enter 'L', 'M', or 'H')")
                continue
        if laptops_sold[0] < 0:
            try:
                a = int(input("Basic Laptops Sold: "))
                if 0 < a <= MAX_VALID_UNITS:
                    laptops_sold[0] = a
                else:
                    print("Invalid basic laptop amount!")
                    continue
            except ValueError:
                print("Invalid basic laptop amount!")
                continue
        if laptops_sold[1] < 0:
            try:
                a = int(input("Mid-Range Laptops Sold: "))
                if 0 < a <= MAX_VALID_UNITS:
                    laptops_sold[1] = a
                else:
                    print("Invalid mid-range laptop amount!")
                    continue
            except ValueError:
                print("Invalid mid-range laptop amount!")
                continue
        if laptops_sold[2] < 0:
            try:
                a = int(input("High-End Laptops Sold: "))
                if 0 < a <= MAX_VALID_UNITS:
                    laptops_sold[2] = a
                else:
                    print("Invalid high-end laptop amount!")
                    continue
            except ValueError:
                print("Invalid high-end laptop amount!")
                continue
        break
    print(name, base_salary, tier, laptops_sold, sep='\n')
    new_tier = tier
    sales = sales(laptops_sold)
    commission = commission(laptops_sold)
    bonus = bonus(sales)
    super_bonus = 0
    promoted = False
    if commission > base_salary/2:
        new_tier += 1
        promoted = True
        if new_tier > 2:
            new_tier = 2
            super_bonus = SUPER_BONUS
    print("Salesperson:  ", name.upper())
    print("Starting Tier:", TIERS[tier])
    print("New Tier:     ", TIERS[new_tier])
    print("Laptops Sold: ", laptops_sold[0], "basic,", laptops_sold[1],
          "mid-range,", laptops_sold[2], "high-end")
    print()
    print("Base Salary:   ", F_STR.format(base_salary))
    print("Commission:    ", F_STR.format(commission))
    print("Bonus:         ", F_STR.format(bonus))
    print("Super Bonus:   ", F_STR.format(super_bonus))
    print("                -----------")
    print("Monthly Pay:   ", F_STR.format(base_salary + commission +
                                          bonus + super_bonus))
    print()
    if promoted and tier == 0:
        print("Congrats, you got promoted to the Middle tier!")
    elif promoted and tier == 1:
        print("Congrats, you got promoted to the High tier!")
    elif promoted and tier == 2:
        print("Congrats, you got the SUPER BONUS since you were already at"
              "the High tier!")
    else:
        print("Sorry, you didn't get promoted to the next tier this month")
    if not input("Would you like to enter another salesperson? (YES or NO) "
                 ).upper().startswith('Y'):
        break
