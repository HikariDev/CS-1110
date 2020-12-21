COUNTY_SALES_TAX = 0.025
STATE_SALES_TAX = 0.06


def calc_taxes(sales):
    return [sales*COUNTY_SALES_TAX, sales*STATE_SALES_TAX]