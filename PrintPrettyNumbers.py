import re
print("Please enter your WMU WIN number, 11-digit phone number",
    "5 digit zip code, or Michigan drivers license number: ", end='')
user_input = str(input(""))
user_input = re.sub('[^0-9a-zA-Z]','',user_input)
if len(user_input) == 9:
    print("WMU WIN: ", int(user_input[0:3]), "-", int(user_input[3:5]), "-",
          int(user_input[5:9]), " (or ",int(user_input[0:3]), "-",
          int(user_input[3:6]), "-", int(user_input[6:9]), ")", sep='')
elif len(user_input) == 11:
    print("PHONE: +", int(user_input[0:1]), " (", int(user_input[1:4]), ") ",
          int(user_input[4:7]), "-", int(user_input[7:11]), sep='')
elif len(user_input) == 5:
    d1 = int(user_input[0:1])
    d2 = int(user_input[1:2])
    d3 = int(user_input[2:3])
    d4 = int(user_input[3:4])
    d5 = int(user_input[4:5])
    print("DIGITS:", d1, "-", d2, "-", d3, "-", d4, "-", d5)
elif len(user_input) == 13 and not str(user_input[0:1]).isdigit():
    print("LICENSE:", str(user_input[0:1]).upper(),int(user_input[1:4]),
          int(user_input[4:7]),int(user_input[7:10]),int(user_input[10:13]))
else:
    print("Please double check your number input!")
input("Press ENTER to exit!")
