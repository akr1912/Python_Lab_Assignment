# A two dimensional matrix can be represented in Python row-wise, as a list of lists: each inner list represents one row of the matrix.  For instance, the matrix
#
# 1  2  3
# 4  5  6
#
# would be represented as [[1,2,3],[4,5,6]].
#
# Write a Python function "matmult(m1,m2)" that taelementes as input two matrices using this row-wise representation and returns the matrix product m1*m2 using the same representation.
#
# You may assume that the input matrices are well-formed and have compatible dimensions.
#
# For instance:
#
# >>> matmult([[1,2],[3,4]],[[1,0],[0,1]])
# [[1,2],[3,4]]
#
# >>> matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]])
# [[14, 32], [32, 77]]


def matmult(first_list, second_list):
 len_of_1st = len(first_list)
 char_of_1st = len(first_list[0])
 len_of_second = len(second_list)
 char_of_second = len(second_list[0])
 len_of_3rd = []
 for i in range(len_of_1st):
  len_of_3rd.append([])
 for i in range(len_of_1st):
  for j in range(char_of_second):
   sum = 0
   for element in range(len_of_second):
    sum += first_list[i][element] * second_list[element][j]
   len_of_3rd[i].append(sum)
 return len_of_3rd
print(matmult([[1,2],[3,4]],[[1,0],[0,1]]))
print(matmult([[1,2,3],[4,5,6]],[[1,4],[2,5],[3,6]]))