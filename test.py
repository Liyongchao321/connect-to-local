from collections import Counter

A = ''
c = Counter(A)
for i in c:
    if c.get(i) != 1:
        print(type(i))
        print(i)
        A = A.replace(i,' ')
for i in range(len(A)):
    if A[i] != ' ':
        print(i)
        break
    print('-1')   
print(A)
# A.replace(c.elem,'')
# print(B)
    
