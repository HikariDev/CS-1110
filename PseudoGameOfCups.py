# PROGRAM:  PseudoGameOfCups.py
# AUTHOR: Andrew Kroll (started by Dr. Kaminski)  
# DESCRIPTION:  [Inspired by Chandler's GameOfCups with Joey in "Friends"].
#   Program gets 5-digit zipcode from user.  (Assume user won't make a
#       mistake, and will enter exactly 5 digits).            
#   Program awards points based on a series of rules, and reports the total
#       points earned at the end.
#   The 8 rules are embedded as comments in the code.
#   For each rule, besides adding points (or not) to the total, rule displays
#       Rule ___ got ___ points, so total is now ___"
#       (It prints this even if rule added 0 points to total).

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - DECLARE VARIABLES
zipcode = 0
d1 = 0
d2 = 0
d3 = 0
d4 = 0
d5 = 0
total = 0
pts = 0
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - GET INPUT
zipcode = str(input("What is your 5-digit zipcode? "))

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - SPLIT INTO 5 DIGITS
d1 = int(zipcode[0:1])
d2 = int(zipcode[1:2])
d3 = int(zipcode[2:3])
d4 = int(zipcode[3:4])
d5 = int(zipcode[4:5])
print("FYI: the 5 digits in zipcode: ", d1, d2, d3, d4, d5, '\n')

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - INITIALIZE TOTAL
# Make sure the running total has been initialized - it has!
#----------------------------------------------------------------- APPLY RULES

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 1
#       1 point when sum of 5 digits is between 10 & 20 (inclusive)
#       2 points when sum is 21 to 30
#       3 points when sum is 31 to 40
#       4 points when sum is more than 40
sum = d1+d2+d3+d4+d5
if 20 >= sum >= 10:
    pts = 1
elif 30 >= sum >= 21:
    pts = 2
elif 40 >= sum >= 31:
    pts = 3
elif sum > 40:
    pts = 4
total += pts
        
# RE-USE CODE BELOW FOR EACH RULE (copy/paste, then FIX rule num)
#       [NOTE:  shortcuts for copy & paste:  CTRL-C & CTRL-V ]         
print("Rule 1 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 2
#       5 points when 1st & last digits match
pts = 5 if d1 == d5 else 0
total += pts
print("Rule 2 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 3
#       6 points when 2nd digit is twice the 1st digit AS WELL AS
#           the 3rd digit being greater than 2nd or 4th digit
pts = 6 if d2 == d1*2 and d3 > d2 and d3 > d4 else 0
total += pts 
print("Rule 3 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 4
#       7 points when there's a lucky 7 anywhere in zipCode
pts = 7 if "7" in zipcode else 0
total += pts
print("Rule 4 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 5
#       8 points when there's NO 13 in MIDDLE of zipCode
#           (like 21322 or 88138 would mean NO points for rule 5)
#       (but zipCodes like 13777 or 99913 with 13's at start/end are
#           irrelevant for rule 5)
pts = 8 if not "13" in zipcode[1:4] else 0
total += pts
print("Rule 5 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 6
#       9 points when all 3 middle digits match
pts = 9 if d2 == d3 == d4 else 0
total += pts
print("Rule 6 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 7
#       10 points when 3rd & 4th digits are both 0
pts = 10 if d3 == 0 == d4 else 0
total += pts
print("Rule 7 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - RULE 8
#       11 points when it's a palindrome
#           (i.e., 1st & 5th match as well as 2nd & 4th match)
pts = 11 if d1 == d5 and d2 == d4 else 0
total += pts
print("Rule 8 got", pts, "points, so total is now", total, "\n")

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - PRINT OUTPUT

print("\nzipcode", zipcode, "got", total, "points")
print("THE END")
