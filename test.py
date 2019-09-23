test = 321
print(test)
while 1:
    try:
        test += float(input("? "))
        break
    except:
        print("Wrong.")
print(test)
