def main():
    print_header()
    data = [[0]*5 for i in range(7)]
    with open("WorldLifeExpData.csv", 'r') as file:
        line = file.readline().split(',')
        while len(line) > 1:
            if not use_record(line):
                line = file.readline().split(',')
                continue
            row = which_row(line[1], line[2], line[3])
            col = which_col(float(line[5]))
            data[row][col] += 1
            line = file.readline().split(',')
    print_detail_lines(data)
    calc_and_print_totals(data)
    print_categories()


def which_row(country, continent, region) -> int:
    rows = [['Europe', 'United States', 'Canada', 'Australia', 'New Zealand', 'Japan', 'South Korea'],
          ['North America'], ['Oceania'], ['South America'], ['Southeast Asia', 'Eastern Asia'],
          ['Middle East', 'Southern Asia and Central Asia'], ['Africa']]
    for row in range(len(rows)):
        if country in rows[row] or continent in rows[row] or region in rows[row]:
            return row
    return -1


def which_col(life_exp) -> int:
    if life_exp <= 60:
        return 0
    elif life_exp <= 68:
        return 1
    elif life_exp <= 75:
        return 2
    elif life_exp <= 80:
        return 3
    else:
        return 4


def use_record(life_exp_str) -> bool:
    if len(life_exp_str) < 13 or which_row(life_exp_str[1], life_exp_str[2], life_exp_str[3])\
            == -1 or life_exp_str[5] == "N.A.":
        return False
    return True


def print_header():
    print('          --LIFE EXPECTANCY CATEGORY--')
    print('CATEGORY  <=60  <=68  <=75  <=80   >80')
    print('--------------------------------------')


def print_detail_lines(counters):
    f_str = "{:>5}{:>9}{:>6}{:>6}{:>6}{:>6}"
    for row in range(7):
        print(f_str.format(row, counters[row][0], counters[row][1],
                           counters[row][2], counters[row][3],
                           counters[row][4]))
    print('--------------------------------------')


def calc_and_print_totals(counters):
    f_str = "TOTALS{:>8}{:>6}{:>6}{:>6}{:>6}   >> {} countries\n"
    totals = [0]*5
    for row in range(7):
        for col in range(5):
            totals[col] += counters[row][col]
    print(f_str.format(totals[0], totals[1], totals[2], totals[3], totals[4], sum(totals)))


def print_categories():
    print('CATEGORIES')
    print('0) Europe, United States, Canada, Australia, New Zealand, Japan, South Korea')
    print('1) other North America (not Canada or United States)')
    print('2) other Oceania (not Australia or New Zealand)')
    print('3) South America')
    print('4) Southeast Asia, other Eastern Asia (not Japan or South Korea)')
    print('5) Middle East, Southern and Central Asia')
    print('6) Africa')


main()
