def twoSum(nums, target):
	h = {};
	for i, x in enumerate(nums):
		n = target - x
		if n not in h:
			h[x] = i
		else:
			return [h[n],i]

nums = [10,11,4,1,3,7,5]
target = 9

print (twoSum(nums, target))