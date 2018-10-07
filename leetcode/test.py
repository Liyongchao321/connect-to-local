A = "A man, a plan, a canal: Panama"
A1 = ''.join([x for x in A if x.isalpha()]).lower()
A2 = A1[::-1]
print(A1)
print(A2)
