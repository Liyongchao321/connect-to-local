matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30],
]
# matrix = [[1,2,3,4,5],
#           [6,7,8,9,10],
#           [11,12,13,14,15],
#           [16,17,18,19,20],
#           [21,22,23,24,25]]
# matrix = [[1,2,3,4,5]]
# matrix = [[1],[2],[3],[4],[5]]
# matrix = [[1,3,5,7,9],
#           [2,4,6,8,10],
#           [11,13,15,17,19],
#           [12,14,16,18,20],
#           [21,22,23,24,25]]
target = 5
import os
if matrix == [] or matrix[0]==[]:
    print(False)
    print(1)
    os._exit(0)
if matrix[0][0] > target:
    print(False)
    print(2)
    os._exit(0)

x = 0
y = 0
a = len(matrix[0])
b = len(matrix)
while True:
    if x != a-1, y!= b-1:
        if matrix[x][y] < target:
            x = x+1
        elif matrix[x][y]>target:
            x = x-1
    elif x=a-1 and y !=b-1:
        if matrix[x][y+1] < target


        if x+1>a and matrix[x][y+1]:
            print('1',False)
            os._exit(0)
    elif matrix[x][y] > target:
        x = x-1
        y = y+1
        if y>=b:
            print('2', False)
            os._exit(0)
    else:
        return True



print(False)
print(5)