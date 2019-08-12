from collections import Counter

nums = [1,2,3,3,3,3,3,4,5,6,3,3]
# nums = [3,2,3]
l = len(nums)
limit = int(l/2)
keys = set(nums)
values = [0]*len(keys)
num_dict = dict(zip(keys, values))

for i in nums:
    num_dict[i] = num_dict[i]+1
    if num_dict[i] > limit:
        print(i)
        break
    
