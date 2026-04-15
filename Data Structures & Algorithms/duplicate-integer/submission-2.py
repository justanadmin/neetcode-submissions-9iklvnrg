class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      nums_set=set(nums)
      number_of_occurence = []
      if(len(nums_set)==len(nums)):
        return False
      else:
        for i in nums_set:
            number_of_occurence.append(nums.count(i))
        for j in number_of_occurence:
            if(j>1):
                return True
        return False