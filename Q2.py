# Question Description :

# The mumbai city local train system carries 2,75,000 people each day.
# The train system observes 15% growth in rainy season only for a particular period (in months) entered by user.
# How many people does the train system carry each year? Write a program in python for the same
# Solution :

total_travelers = 275000
print("Total Travelers on each day :", total_travelers)
months_by_user = str(input("Enter the month : "))

if(months_by_user == "January" or "March" or "May" or "July" or "August" or "October" or "December"):
    number = 31
    print(number)
    increase_percent = 0.15 * total_travelers
    print("Increased travelers in one day are : ", increase_percent)
    total_month_increment = total_travelers + increase_percent * number
    days_left = 365 - number
    print("Days left in year :", days_left)
    print("Increased travelers in one month are : ", total_month_increment)
    total_left = (total_travelers * days_left) + total_month_increment
    print("Total Travelers including 15% increment are : ", total_left)

if(months_by_user == "February"):
    numbelen_of_second = 28
    print(numbelen_of_second)
    increase_percent = 0.15 * total_travelers
    print("Incresed travelers in one day are : ", increase_percent)
    total_month_increment = total_travelers + increase_percent * numbelen_of_second
    print("Incresed travelers in one month are : ", total_month_increment)
    days_left = 365 - numbelen_of_second
    print("Days left in year :", days_left)
    total_left = (total_travelers * days_left) + total_month_increment
    print("Total Travelers including 15% increment are : ", total_left)

if(months_by_user == "April" or "June" or "September" or "November"):
    number3 = 30
    print(number3)
    increase_percent = 0.15 * total_travelers
    print("Increased travelers in one day are : ", increase_percent)
    total_month_increment = total_travelers + increase_percent * number3
    print("Increased travelers in one month are : ", total_month_increment)
    days_left = 365 - number3
    print("Days left in year :", days_left)
    total_left = (total_travelers * days_left) + total_month_increment
    print("Total Travelers including 15% increment are : ", total_left)

