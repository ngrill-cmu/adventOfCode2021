f = open("input.txt", "r")
nums = []
for x in f:
    nums.append(int(x))

count = 0

for i in range (len(nums) - 1):
    if (nums[i+1] - nums[i] > 0):
        count = count + 1

print(count)
count = 0

for i in range (len(nums) - 3):
    if (nums[i+3] - nums[i] > 0):
        count = count + 1

print(count)

newSeq = []
for i in range (len(nums) - 3):
    newSeq.append(i)

result = list(map(lambda x: nums[x+3] - nums[x], newSeq))
result2 = list(filter(lambda x: x > 0, result))
print(len(result2))