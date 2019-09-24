import re

msg = str(input("Please enter a message! "))
count = [0,0,0,0,0,0]

for c in msg:
    if re.match("[a-z]", c):
        count[0] += 1
    elif re.match("[A-Z]", c):
        count[1] += 1
    elif re.match("[0-9]", c):
        count[2] += 1
    elif re.match("[ ]", c):
        count[3] += 1
    elif re.match("[+\\-*/]", c):
        count[4] += 1
    else:
        count[5] += 1
total = 0

for i in count:
    total += i

f_str = """category count
a-z \t{0:>6n}
A-Z \t{1:>6n}
0-9 \t{2:>6n}
spaces  {3:>6n}
+ - * / {4:>6n}
other   {5:>6n}
\t\t  ----
TOTAL   {6:>6n}"""
print(f_str.format(count[0],count[1],count[2],count[3],count[4],count[5],total))