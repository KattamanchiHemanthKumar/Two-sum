nums = [2,7,11,15]
target = 9
c=0
k=0
z=0
for i in range(len(nums)):
    c=nums[i]
    for j in range(i+1,len(nums)):
        c+=nums[j]
        if c==target:
            break
        else:
            c=c-nums[j]
    if c==target:
        k=i
        z=j
        break
print(k,j)