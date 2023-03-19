from typing import List

def search(nums: List[int], target: int, start: int, end: int) -> int:
	if (start-end == 1):
		if(nums[start] == target):
			return start
		else:
			return -1
	mid = (end + start) // 2
	print ("LOW =",start ,"| HIGH=", end)
	print ("MID =",mid,"|NUM[MID]=",nums[mid])
	print ("START+MID =",start+mid,"|NUM[START+MID]=",nums[start+mid])
	if nums[start+mid] > target:
		return search(nums, target, start, end-mid)
	else:
			return search(nums, target, start+mid, end)

def binarysearch(nums, target):
	return search(nums, target, 0, len(nums))
		
num = [2,3,4,5,6,7,8,9,20]
x = 10
print ("Index of ", x, "IS :")
print (binarysearch(num, x))