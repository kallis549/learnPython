#Given an array of integers, find out whether there are two distinct indices #i and j in the array such that the absolute difference between nums[i] and #nums[j] is at most t and the absolute difference between i and j is at most #k.
#Example 1:
#Input: nums = [1,2,3,1], k = 3, t = 0
#Output: true
#Example 2:
#Input: nums = [1,0,1,1], k = 1, t = 2
#Output: true
#Example 3:
#Input: nums = [1,5,9,1,5,9], k = 2, t = 3
#Output: false


from typing import List

def containsNearbyDuplicate(nums: List[int], k: int, t: int) -> bool:
	unq = set();
	for i, n in enumerate(nums):
		print("vals i:n - "+str(i)+":"+str(n))
		for x in range(t+1):
			print("vals x:n - "+str(x)+":"+str(n))
			if n-x in unq:
				print(str(n-x)+"|"+str(n))
				return True;
			unq.add(n-x);
		if len(unq) > k:
			unq.remove(nums[i-k])
	return False;

nums = [11,4,7,20,2,6]
k = 3
t = 2


print(containsNearbyDuplicate(nums, k, t))