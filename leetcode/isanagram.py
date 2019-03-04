from collections import Counter
# s = "anagram"
# t = "nagaram"
s = "rat" 
t = "car"
count_s = Counter(s)
count_t = Counter(t)

print(count_s)
print(count_t)
if count_s == count_t:
    print('haha')
else:
    print('fuck')