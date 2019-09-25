from Lab4 import User, Tax, Report


def main():
    sales = User.get_input()
    taxes = Tax.calc_taxes(sales)
    Report.do_report(sales, taxes)


main()
