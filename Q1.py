# Question Description :

# A disk drive shows T bytes and U bytes as free and used space respectively.
# If you delete a file of size O bytes and create a new file of size H bytes then how many free bytes will the disk have?
# Here T, U, O and H are user-entered values.
# Write a program in python to find the same
# Solution :

T_bytes = int(input("Enter The number of bytes that are free : \n"))
U_bytes = int(input("Enter the number of bytes that are used :  \n"))
O_bytes = int(input("Enter the size in bytes that you want to delete : \n"))
H_bytes = int(input("Enter the size in bytes that you want to add : \n"))
new_used_bytes = U_bytes - O_bytes
total_free_bytes = T_bytes + O_bytes
new_added_bytes = new_used_bytes + H_bytes
new_free_bytes = total_free_bytes - H_bytes

print("Total Free Bytes remaining is : ")
print(new_free_bytes)
print("Total Used Bytes is : ")
print(new_added_bytes)