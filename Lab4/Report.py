F_STR = "${0:>10,.2f}"


def do_report(sales, taxes):
    print("MONTHLY SALES TAX REPORT:")
    print("Total sales for the month: ", F_STR.format(sales))
    print("Amount of county sales tax:", F_STR.format(taxes[0]))
    print("Amount of state sales tax: ", F_STR.format(taxes[1]))