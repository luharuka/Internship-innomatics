# Subset

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[]]
        
        for num in nums:
            curRes = [val for val in result]
            for cur in curRes:
                result += [cur+[num]]
        
        return result

