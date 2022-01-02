# Write a program in python to push all zeroes at the end of the list of N length,
# where list and length is provided by user.

# user_list = []
# N = int(input("Enter the length of the list"))
# for i in range(0, N):
#     num = int(input())
#     user_list.append(num)
# print(user_list)

# def move_zero(num_list):
user_list = []
N = int(input("Enter the length of the list"))
for i in range(0, N):
    num = int(input())
    user_list.append(num)
print(user_list)
acc = [0 for i in range(user_list.count(0))]
zero = [i for i in user_list if i != 0]
zero.extend(acc)
print("Zeros are pushed at the end: ", zero)

# print(move_zero([0,2,3,4,6,7,10]))
# print(move_zero([10,0,11,12,0,14,17]))