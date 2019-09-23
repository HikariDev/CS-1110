# PROGRAM:  ValidateStudentData.py
# AUTHOR:  Andrew Kroll      DESIGNER:  Dr. Kaminski
# DESCRIPTION:  Gets student data from user for multiple students.
#       Data fields are validated (see DataValidation.py):
#           name - no checking possible
#           gpa - must be between  0.0 and 4.0
#           age - must be between 15 and 80
#           zip - must start with 49 (i.e., 49???)
#           year - must be FR, SO, JR, SR
#       For each student, print out their data using the f_str below for
#           data fields in the above order.
# NOTE:  Program runs right now, as is.  When you add some code, re-run it and
#       keep program in a valid state.
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
f_str = "{:s}, gpa: {:.2f}, age: {:2d}, zip: {:5d}, year: {:s}"
done = "no"
while done == "no":
    # - - - - - - - - - - - - - - - - - - - - - - - input with data validation
    name = input("What is the student's name? ")
    gpa = None
    age = None
    zip = None
    year = None
    while gpa == None:
        try:
            temp = float(input("What is the student's GPA? "))
            if 0.0 <= temp <= 4.0:
                gpa = temp
            else:
                print("Error: GPA must be between 0.0 and 4.0!")
        except:
            print("Error: GPA must be a number!")
    while age == None:
        try:
            temp = int(input("What is the student's age? "))
            if 15 <= temp <= 80:
                age = temp
            else:
                print("Error: Age must be between 15 and 80!")
        except:
            print("Error: Age must be a whole number!")
    while zip == None:
        try:
            temp = int(input("What is the student's 5-digit zipcode? "))
            if 49000 <= temp < 50000:
                zip = temp
            else:
                print("Error: 5-Digit zipcode must start with 49!")
        except:
            print("Error: 5-Digit zipcode must be a whole number!")
    while year == None:
        temp = input("What is the student's year? ").upper()
        if temp == "FR" or temp == "SO" or temp == "JR" or temp == "SR":
            year = temp
        else:
            print("Error: Year must be FR, SO, JR, or SR!")
    # - - - - - - - - - - - - - - - - - - - - - - - - -  print student's data
    print(f_str.format(name, gpa, age, zip, year))
    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    done = input("Done entering scores?  (yes or no):  ")

print("\nTHE END")