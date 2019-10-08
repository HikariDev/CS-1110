# PROGRAM: Assignment 1: Ride Sharing
# AUTHOR: Andrew Kroll
# DATE: 09/04/2019
# DESCRIPTION: This application allows users to easily calculate the cost of
#    commuting to/from the Parkview campus for their classes.

## Input

days_per_week = int(input("How many days per week do you have classes? "))
weeks_per_semester = int(input("How many weeks long is the semester? "))
price_per_gallon = float(input("How much does a gallon of gas cost? $"))
average_mpg = float(input("What is your car's average miles per gallon? "))
distance = float(input("How many miles away from Parkview do you live? "))

## Constants

COST_PER_MILE = 0.25

## Processing

trips_per_semester = days_per_week*weeks_per_semester
miles_per_semester = distance*2*trips_per_semester
round_trip_cost = 2*distance/average_mpg*price_per_gallon
round_trip_cost += COST_PER_MILE*2*distance

def formatNum(num): #Drops .0 from decimals.
    return int(num) if num % 1 == 0 else num

## Output

print("\n********** RIDE SHARING APP **********\n")

print("DATA YOU PROVIDED")
print("Gas costs $", format(price_per_gallon, '.2f'), " per gallon", sep='')
print("Car averages", formatNum(average_mpg), "mpg")
print("Class meets", days_per_week, "days/week,", weeks_per_semester,
      "weeks/semester")
print("Distance to Parkview:", formatNum(distance), "miles 1-way")

print("\nFIXED GENERIC COST\n$", COST_PER_MILE, " per mile", sep='')

print("\nFYI RESULTS")
print(format(trips_per_semester,'.0f'), "round trips/semester")
print(format(miles_per_semester,'.0f'), "total miles/semester")
print("$", format(round_trip_cost,'.2f'), " total for 1 round trip ($",
      format(price_per_gallon, '.2f'), " for gas)", sep='')

print("\nCOST FOR THE SEMESTER")
print("1 person alone:    $", format(round_trip_cost*trips_per_semester,
                                     '.2f'), sep='')
print("2 people sharing:  $", format(round_trip_cost*trips_per_semester/2,
                                     '.2f'), " per person", sep='')
print("3 people sharing:  $", format(round_trip_cost*trips_per_semester/3,
                                     '.2f'), " per person", sep='')

print("\n*************** THE END ***************")
