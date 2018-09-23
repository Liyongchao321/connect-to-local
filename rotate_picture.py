# a=[1,2,3,4]
# b=[5,6,7,8]
# c=[9,10,11,12]
# d=[13,14,15,16]
# a = [1,2,3]
# b = [4,5,6]
# c = [7,8,9]
a = [1,2,3,4,5,6]
b=[6,7,8,9,10,11]
c = [1,2,3,4,5,6]
d=[6,7,8,9,10,11]
e = [1,2,3,4,5,6]
f=[6,7,8,9,10,11]
A=[a,b,c,d,e,f]
for a in A:
    print(a)
print(len(A)/2)
k = len(A)
count = 0
i=0
while i < k/2:
    j = 0
    l = k - i*2-2
    print('l:',l)
    
    while j <= l:
        print('round')
        print('i:',i,'j:',j)

        temp = A[i][i+j]
        
        A[i][i+j] = A[k-i-j-1][i]
        A[k-i-j-1][i] = A[k-i-1][k-i-j-1]
        A[k-i-1][k-i-j-1] = A[i+j][k-i-1]
        A[i+j][k-i-1] = temp
        j = j+1

        for a in A:
            print(a)
        print('round end')
    i =i+1


for a in A:
    print(a)

