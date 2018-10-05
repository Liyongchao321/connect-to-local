# A=[6,1,1,2,2,3,3,4,5,6,5]
A=[2,1,2]
B=[]
for i in  range(len(A)):
    print('i=',i)
    if A[i] in B:
        B.remove(A[i])
    else:
        B.append(A[i])
    print('B=',B)
print(B[0])