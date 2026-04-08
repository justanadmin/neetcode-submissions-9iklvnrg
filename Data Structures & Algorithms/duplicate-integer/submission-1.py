class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        distinct_value=set(nums)
        if len(nums)==len(distinct_value):
            return False
        else :
            return True