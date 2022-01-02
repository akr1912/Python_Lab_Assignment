# Question Description

# Mr. Samuel Gene is purchasing items for his relatives. He has purchased the following items:
# i. 3 shirts, at the rate of 680 rupees
# ii. 1 computer game, at the rate of 750 rupees
# iii. 2 bracelets, at the rate of 230 rupees
# Write a program to find the total cost. Later he returned one of the bracelet for a full refund and one shirt at a loss of 50%.
# Find the total cost after refund using the same program

each_shirt_cost = 680
print("Cost of 1 shirt is : Rs", each_shirt_cost)
each_game_cost = 750
print("Cost of 1 game is : Rs", each_game_cost)
each_bracelet_cost = 230
print("Cost of 1 bracelet is : Rs", each_bracelet_cost)

total_cost = 3*each_shirt_cost + each_game_cost + 2*each_bracelet_cost
bracelet_refund = each_bracelet_cost
shirt_refund = 0.5 * each_shirt_cost
refund = bracelet_refund + shirt_refund
print("Total Refunded Amount : Rs", refund)
print("Total Cost before Refund is : Rs", total_cost)
refund_cost = total_cost - (bracelet_refund + shirt_refund)
print("Total Cost After Refund is : Rs", refund_cost)