A='  123'
B='  asd123'
C='    -123asd'
D=''

str=A
str = str.lstrip()
print(str)
# if not str[1].isdigit():
#     print('haha')
if str == '':
    print('heihei')
i = 0
sign = 1
if str[0] == '-':
    sign = -1
    str = str[1:]
elif str[0] == '+':
    sign = 1
    str = str[1:]
if str == '':
    print('heihei')
while i < len(str) and str[i].isdigit():
    i += 1
 
if i == 0:
    print('haha')
else:
    str = str[:i]
res = sign*int(str)
res = -2147483648 if res<-2147483648 else res
res = 2147483647 if res>2147483647 else res
print(res)
