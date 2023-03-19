#Given an array of integers and an integer k, find out whether there are two #distinct indices i and j in the array such that nums[i] = nums[j] and the #absolute difference between i and j is at most k.
#Example 1:
#Input: nums = [1,2,3,1], k = 3
#Output: true
#Example 2:
#Input: nums = [1,0,1,1], k = 1
#Output: true
#Example 3:
#Input: nums = [1,2,3,1,2,3], k = 2
#Output: false

from typing import List

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
	unq = set();
	for i, n in enumerate(nums):
		if n in unq:
			return True;
		unq.add(n);
		if len(unq) > k:
			unq.remove(nums[i-k])
	return False;

nums = [1,2,3,1,2,3]
k = 2

print(containsNearbyDuplicate(nums, k))