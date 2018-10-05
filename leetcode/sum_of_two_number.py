

nums=[3,2,4]
target = 6
print(nums)
index = range(len(nums))
print(index)
nums_zip = list(zip(nums,index))
print(nums_zip)
for i in range(len(nums)):
    print(nums_zip[i][1])
nums_zip.sort()
print(nums_zip)
for i in nums_zip:
    print(i[0])

    
end = len(nums)
for i in range(len(nums)):
    j = i+1
    while j < end:
        temp = nums_zip[i][0]+nums_zip[j][0]
        if temp < target:
            j =j+1
        elif temp == target:
            print( [nums_zip[i][1],nums_zip[j][1]])
            break
        elif temp > target:
            end = j
            break

