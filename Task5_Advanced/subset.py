from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = [[]]
        
        for num in nums:
            curRes = [val for val in result]
            for cur in curRes:
                result += [cur+[num]]
        
        return result

if __name__=="__main__":
    sol=Solution()
    arr=input().split(" ")
    arr=list(map(int,arr))
    print(arr)
    res_arr=sol.subsets(arr)
    print(res_arr)
