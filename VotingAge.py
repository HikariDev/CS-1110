VOTING_AGE = 18
age = 19

print("Voting age in Michigan is", VOTING_AGE)
print()

if age >= 18:
    print("you can vote since you're", age)
    print("  (but must register before that)")
else:
    print("you can't vote yet since you're", age)
    print("  but you can vote in", VOTING_AGE - age, "years")
print()

print("TRY AGAIN with a different age")
age = 16
if age >= 18:
    print("you can vote since you're", age)
    print("  (but must register before that)")
else:
    print("you can't vote yet since you're", age)
    print("  but you can vote in", VOTING_AGE - age, "years")
print()

print("THE END")
