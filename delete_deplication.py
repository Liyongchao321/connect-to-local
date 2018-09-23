A=[1,1,2,2,3,3,3,4,5,5]
for i in range(len(A)-1):
    print(A[i])
i=0
print(A[i])
l=len(A)-1
while i < l:
    temp = A[i]
    if A[i+1] == temp:
        A.remove(A[i+1])
        l -= 1
        print(i,l,A[i])
    else:
        i += 1
        print(i,l,A[i])
print(A)

#def removeDuplicates(self, nums):




    
