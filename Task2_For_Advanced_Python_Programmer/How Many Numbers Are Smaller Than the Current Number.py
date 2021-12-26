# How Many Numbers Are Smaller Than the Current Number
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        return [sorted_nums.index(num) for num in nums]

if __name__=="__main__":
    sol=Solution()
    print("Input array")
    arr = list(map(int, input().split()))
    res=sol.smallerNumbersThanCurrent(arr)
    print("Resut: ")
    print(res)
