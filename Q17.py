# There are 10 students in a class. Some students’ names are same to other students.
# Write a python program to print the names that occur more than one time.
# The file name will be given by user where all names are written in a file as new line

number_of_students = int(input("Enter the strength of Students :\n"))
my_list =[]
for student in range(0, number_of_students):
    student = input("Enter the Name of Student :\n")
    my_list.append(student)
print(my_list)
word_freq = [my_list.count(p) for p in my_list]
print("The frequency of words is ...")
print(dict(zip(my_list, word_freq)))