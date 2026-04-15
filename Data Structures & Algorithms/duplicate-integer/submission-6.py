class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums_set=set(nums)
      number_of_occurence = []
      if(len(nums_set)==len(nums)):
        return False
      else:
        return True