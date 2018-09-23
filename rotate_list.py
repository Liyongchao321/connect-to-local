
A=[1,2,3,4,5]
k=2

A[0:len(A)-k] = list(reversed(A[0:len(A)-k]))
print(A)
print(A[len(A)-k: len(A)])
A[len(A)-k: len(A)] = list(reversed(A[len(A)-k: len(A)]))
print(A)
A.reverse()
print(A)