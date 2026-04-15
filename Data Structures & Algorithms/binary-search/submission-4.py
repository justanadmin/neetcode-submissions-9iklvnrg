class Solution:
    def search(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):   # iterate using index to avoid index out of range
            if nums[i] == target:
                return i
        
        return -1   # only return after full loop