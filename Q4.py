# Question Description :

# Salesperson Rita drives 2,052 miles in N days, stopping at 2 towns each day.
# How many miles does she average between the setups.
# Write a program in python for the same where value of N is provided by user

total_miles = 2052
number_of_days = int(input("Enter number of days you have drive : "))
print("Days Rita Drives : ", number_of_days, " Days")
each_day = total_miles / number_of_days
print("Each day Rita drives : ", each_day, "Miles")
stops_in_a_day = 2
total_stops = 2 * number_of_days
print("Total towns she stopped is : ", total_stops, " Towns")
average = each_day / stops_in_a_day
print("Rita travels average of : ", average, "Miles for each town")

