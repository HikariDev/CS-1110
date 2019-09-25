def get_input():
    sales = -1
    while sales < 0:
        try:
            sales = float(input("What were the total sales for this month? $"))
        except ValueError:
            print("Invalid sales amount! Only include numbers and a decimal!")
    return sales
