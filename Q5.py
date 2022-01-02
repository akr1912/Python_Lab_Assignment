# Question Description :

# Sanorita rented two movies to watch last night. The first was 100 minutes long, the second was 150 minutes long.
# Sanorita has to pay D dollars for each 50 minutes.
# How many hours did it take for Sanorita to watch the two movies and how much she has to pay (in dollars).
# Write a program in Python for the same where D is entered by user

movie_duration_1 = 100
movie_duration_2 = 150
total_duration = movie_duration_1 + movie_duration_2
duration_in_hour = total_duration / 60
rent = int(input("Enter the rent for 50 minutes in Dollars : "))
rent_for_min = rent/50
total_rent = total_duration * rent_for_min
print("Total Hours Taken : ", duration_in_hour, "Hours")
print("She Has to Pay $", total_rent, "Dollars")
