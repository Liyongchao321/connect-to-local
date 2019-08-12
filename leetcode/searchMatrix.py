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
a = len(matrix)
b = len(matrix[0])
for i in range(0, a):
    if matrix[i][0]>target:
        a = i+1
        break
for i in range(0, b):
    if matrix[0][i]>target:
        b = i+1
        break
l = min(a, b)
print(a,b)
m = 0
for i in range(0,l):
    if matrix[i][i] > target:
        m = i
        break
print('m=',m)      
print(11)
for row in matrix[:m]:
    print(row[:b])
    if target in row[:b]:
        print(True)
        print(3)
        os._exit(0)
print(22)
for row in matrix[m:a]:
    print(row[:m])
    if target in row[:m]:
        print(True)
        print(4)
        os._exit(0)

print(False)
print(5)