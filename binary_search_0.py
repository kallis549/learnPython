from typing import List

class Solution:
 	def search(self, nums: List[int], target: int) -> int:
	 	low =0;
	 	high = len(nums)-1;
	 	if nums[low] == target:
 			return low
 		if nums[high] == target:
	 		return high
	 	if high==0 and nums[high] != target:
	 		return -1
	 	if (low==0 and high==1):
	 		return -1
	 	mid = (high+low) // 2
	 	print ("LOW =", low, "| HIGH=", high)
	 	while(low < high):
 			if nums[mid] == target:
	 			return mid
 			elif nums[mid] < target:
 				val = self.search(nums[mid: ], target)
 				if val == -1:
 					return val
	 			else:
	 				return mid + val 
 			else:
	 			return self.search(nums[: mid], target)
	 	return -1

num = [2,3,4,5,6,7,8,9,20]
x = 11	

s= Solution()
print ("Index of ", x, "IS :")
print (s.search(num, x))