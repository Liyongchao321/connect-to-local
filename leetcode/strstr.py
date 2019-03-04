haystack = "hellollll"
# needle = "lll"
needle = ''
n = len(haystack)
m = len(needle)
if m == 0:
    print(0)
l = n-m
print(n,m,l)
res = n
for i in range(l+1):
    # print(i)
    # print(haystack[n-m-i:n-i]) 
    if haystack[n-m-i:n-i] == needle:
        res = n-m-i

if res == n:
    print(-1)
else:
    print(res)