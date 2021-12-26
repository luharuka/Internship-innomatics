# Maximum Product of Two Elements in an Array
from typing import List
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max1=0
        max2=0
        for i in nums:
            if i>max1:
                max2=max1
                max1=i
            elif i>max2:
                max2=i
        return (max1-1)*(max2-1)


if __name__=="__main__":
    sol=Solution()
    print("Input array")
    arr = list(map(int, input().split()))
    res=sol.maxProduct(arr)
    print("Resut: ")
    print(res)